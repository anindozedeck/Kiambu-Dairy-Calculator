# Kiambu Dairy Co-op Payment Calculator

A small command-line calculator that totals a farmer's payment using the
co-op's current buying price.

## Requirements

- Python 3.8 or later
- No third-party packages

## Setup and run

1. Keep `dairy_calculator.py` and `price.txt` in the same folder.
2. Ensure `price.txt` contains only the current price per litre, for example:

   ```text
   55.0
   ```

3. Open a terminal in that folder and run:

   ```bash
   python dairy_calculator.py
   ```

   On some systems, use `python3 dairy_calculator.py` instead.

The co-op manager can update the weekly rate by changing the number in
`price.txt`. The price must be a valid number greater than zero.

## Example

```text
Kiambu Dairy Co-op Payment Calculator
--------------------------------------
Current buying price: KES 55.00 per litre

Farmer name: Amina
Litres supplied today: 20

Farmer : Amina
Litres : 20
Price  : KES 55.00/litre
Total  : KES 1,100.00
```
