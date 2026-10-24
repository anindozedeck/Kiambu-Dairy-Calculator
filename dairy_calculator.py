"""Calculate farmer payments using the co-op's current buying price."""

import sys
from decimal import Decimal, InvalidOperation
from pathlib import Path


PRICE_FILE = Path(__file__).with_name("price.txt")


def get_current_price() -> Decimal:
    """Read and validate the current price from the price file."""
    try:
        price_text = PRICE_FILE.read_text(encoding="utf-8").strip()
    except OSError as error:
        raise RuntimeError(f"Could not read {PRICE_FILE}: {error}") from error

    try:
        price = Decimal(price_text)
    except InvalidOperation as error:
        raise ValueError(f"{PRICE_FILE} must contain a valid price.") from error

    if not price.is_finite() or price <= 0:
        raise ValueError(f"{PRICE_FILE} must contain a price greater than zero.")

    return price


def calculate_payment(litres: Decimal, price_per_litre: Decimal) -> Decimal:
    return litres * price_per_litre


def run() -> int:
    print("Kiambu Dairy Co-op Payment Calculator")
    print("--------------------------------------")

    try:
        price = get_current_price()
    except (RuntimeError, ValueError) as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1

    print(f"Current buying price: KES {price:.2f} per litre")
    print()

    name = input("Farmer name: ").strip()
    if not name:
        print("Name is required.")
        return 1

    try:
        litres = Decimal(input("Litres supplied today: ").strip())
    except InvalidOperation:
        print("Please enter a valid number for litres.")
        return 1

    if not litres.is_finite() or litres <= 0:
        print("Litres must be a number greater than zero.")
        return 1

    total = calculate_payment(litres, price)

    print()
    print(f"Farmer : {name}")
    print(f"Litres : {litres}")
    print(f"Price  : KES {price:.2f}/litre")
    print(f"Total  : KES {total:,.2f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(run())