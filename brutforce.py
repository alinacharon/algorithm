import csv
from itertools import combinations
import time

def read_actions(file_path):
    actions = []
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            actions.append({
                'name': row['name'],
                'cost': float(row['price']),
                'profit': float(row['profit'])
            })
    return actions

def calculate_profit(combination):
    total_cost = sum(action['cost'] for action in combination)
    total_profit = sum(action['cost'] * (action['profit'] / 100)
                       for action in combination)
    return total_cost, total_profit

def find_best_combination(actions, max_budget):
    best_combination = []
    best_profit = 0

    for r in range(1, len(actions) + 1):
        for combination in combinations(actions, r):
            cost, profit = calculate_profit(combination)
            if cost <= max_budget and profit > best_profit:
                best_combination = combination
                best_profit = profit

    return best_combination, best_profit

def main():
    start_time = time.time() 

    actions = read_actions('actions.csv')
    max_budget = 500

    best_combo, best_profit = find_best_combination(actions, max_budget)

    print("Meilleure combinaison d'actions :")
    for action in best_combo:
        print(f"{action['name']} - Coût: {action['cost']}€ - Profit: {action['profit']}%")

    total_cost = sum(action['cost'] for action in best_combo)
    print(f"\nCoût total: {total_cost:.2f}€")
    print(f"Profit total: {best_profit:.2f}€")

    end_time = time.time()  
    execution_time = end_time - start_time
    print(f"\nTemps d'exécution: {execution_time:.2f} secondes")

if __name__ == "__main__":
    main()