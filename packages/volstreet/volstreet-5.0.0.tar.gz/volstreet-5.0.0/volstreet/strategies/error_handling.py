import functools
import traceback
from inspect import signature
from volstreet import config
from volstreet.angel_interface.interface import (
    fetch_book,
    fetch_quotes,
    lookup_and_return,
)
from volstreet.angel_interface.orders import place_order
from volstreet.trade_interface.order_placement import cancel_pending_orders
from volstreet.utils import custom_round, notifier


def prepare_exit_params(
    positions: list[dict],
    max_lot_multiplier: int = 30,
    ltp_missing: bool = True,
) -> list[dict]:
    order_params_list = []
    if ltp_missing:
        prices = fetch_quotes(
            [position["symboltoken"] for position in positions], structure="dict"
        )
        positions = [
            {**position, "ltp": prices[position["symboltoken"]]["ltp"]}
            for position in positions
        ]
    for position in positions:
        net_qty = int(position["netqty"])
        lot_size = int(position["lotsize"])
        max_order_qty = max_lot_multiplier * lot_size

        if net_qty == 0:
            continue
        action = "SELL" if net_qty > 0 else "BUY"
        total_qty = abs(net_qty)

        execution_price = (
            float(position["ltp"]) * 1 - config.LIMIT_PRICE_BUFFER
            if action == "SELL"
            else float(position["ltp"]) * 1 + config.LIMIT_PRICE_BUFFER
        )
        execution_price = custom_round(execution_price)

        while total_qty > 0:
            order_qty = min(total_qty, max_order_qty)
            params = {
                "symbol": position["tradingsymbol"],
                "token": position["symboltoken"],
                "qty": order_qty,
                "action": action,
                "price": execution_price,
            }
            order_params_list.append(params)
            total_qty -= order_qty

    return order_params_list


def get_active_qty_for_strategy(orderbook: list, index: str, order_tag: str) -> list:
    """
    Returns the current active quantities, symboltokens, and trading symbols for a given ordertag.
    Active quantity is increased for 'BUY' transactions and decreased for 'SELL' transactions.

    :param orderbook: List of orderbook entries.
    :param index: The index to search for.
    :param order_tag: The order tag to search for.
    :return: A list of dictionaries, each containing the active quantity, symboltoken, and trading symbol.
    """
    active_quantities = {}

    for order in orderbook:
        if order["ordertag"] == order_tag and order["tradingsymbol"].startswith(index):
            symbol = order["tradingsymbol"]
            filled_shares = (
                int(order["filledshares"]) * -1
                if order["transactiontype"] == "SELL"
                else int(order["filledshares"])
            )

            if symbol not in active_quantities:
                active_quantities[symbol] = {
                    "netqty": 0,
                    "symboltoken": order["symboltoken"],
                    "tradingsymbol": symbol,
                    "lotsize": int(order["lotsize"]),
                }

            active_quantities[symbol]["netqty"] += filled_shares
    active_positions = [
        position for position in active_quantities.values() if position["netqty"]
    ]
    return active_positions


def place_exit_orders(exit_params: list[dict]):
    for param in exit_params:
        place_order(**param, order_tag="Error induced exit")


def exit_strategy(strategy, *args, **kwargs) -> None:
    sig = signature(strategy)
    bound = sig.bind_partial(*args, **kwargs)
    bound.apply_defaults()
    order_tag = bound.arguments.get("strategy_tag")
    index = bound.arguments.get("underlying").name
    order_book = fetch_book("orderbook", from_api=True)
    pending_orders = lookup_and_return(
        order_book, ["ordertag", "status"], [order_tag, "open"], "orderid"
    )
    if pending_orders:
        cancel_pending_orders(pending_orders, variety="NORMAL")
    active_positions = get_active_qty_for_strategy(order_book, index, order_tag)
    if not active_positions:
        return
    exit_params = prepare_exit_params(active_positions, ltp_missing=True)
    place_exit_orders(exit_params)


def exit_on_error(strategy):
    @functools.wraps(strategy)
    def wrapper(*args, **kwargs):
        try:
            return strategy(*args, **kwargs)
        except Exception as e:
            user_prefix = config.ERROR_NOTIFICATION_SETTINGS.get("user")
            user_prefix = f"{user_prefix} - " if user_prefix else ""
            notifier(
                f"{user_prefix}"
                f"Error in strategy {strategy.__name__}: {e}\nTraceback:{traceback.format_exc()}\n\n"
                f"Exiting existing positions...",
                config.ERROR_NOTIFICATION_SETTINGS["url"],
                "ERROR",
                send_whatsapp=True,
            )
            try:
                exit_strategy(strategy, *args, **kwargs)
                notifier(
                    f"{user_prefix}Exited existing positions in {strategy.__name__}.",
                    send_whatsapp=True,
                )
            except Exception as e:
                message = f"{user_prefix}Error while exiting strategy {strategy.__name__}: {e}\nTraceback:{traceback.format_exc()}"
                notifier(message, config.ERROR_NOTIFICATION_SETTINGS["url"], "ERROR")

    return wrapper
