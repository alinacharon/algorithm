# Investment Portfolio Optimization

This repository contains two Python scripts for optimizing investment portfolios based on a given budget and a set of actions (stocks) with their associated costs and profits.

## Files

1. `bruteforce.py`: A brute-force approach to find the best combination of actions.
2. `optimized.py`: An optimized greedy algorithm approach for faster results.

## bruteforce.py

This script uses a brute-force approach to find the best combination of actions within a given budget.

### Features:
- Reads action data from a CSV file
- Calculates profit for all possible combinations of actions
- Finds the best combination that maximizes profit within the budget
- Prints the best combination, total cost, and total profit
- Measures and displays execution time

## optimized.py

This script uses a greedy algorithm to quickly find a near-optimal combination of actions within a given budget.

### Features:
- Reads action data from multiple CSV files
- Uses a greedy approach to select actions
- Calculates profit for the selected combination
- Prints the selected combination, total cost, and total profit
- Measures and displays execution time
- Processes multiple datasets sequentially

### Usage:
## Input Data

Both scripts expect CSV files with the following structure:
- `name`: Name of the action (stock)
- `price` or `cost`: Cost of the action in euros
- `profit`: Expected profit percentage after 2 years

## Requirements

- Python 3.x
- CSV module (built-in)
- itertools module (built-in)
- time module (built-in)

## Note

The optimized version may not always find the absolute best combination but provides a good balance between execution speed and result quality, especially for larger datasets.
