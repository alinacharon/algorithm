import csv
from time import time


def read_data(file_path):
    with open(file_path, mode='r') as file:
        return [{"name": row["name"], "price": float(row["price"]), "profit": float(row["profit"])}
                for row in csv.DictReader(file) if float(row["price"]) > 0]


def calculate_profit(actions):
    return sum(action['price'] * (action['profit'] / 100) for action in actions)



def greedy_invest(actions, max_budget):
    valid_actions = [action for action in actions if action['price'] > 0]

    sorted_actions = sorted(
        valid_actions, key=lambda x: x['profit'], reverse=True)

    selected_actions = []
    current_budget = max_budget

    for action in sorted_actions:
        if action['price'] <= current_budget:
            selected_actions.append(action)
            current_budget -= action['price']

    return selected_actions


def main():
    file_paths = ['actions.csv','dataset1_Python+P7.csv', 'dataset2_Python+P7.csv']
    max_budget = 500

    for file_path in file_paths:
        print(f"Traitement du fichier : {file_path}")

        start_time = time()
        actions = read_data(file_path)
        best_combination = greedy_invest(actions, max_budget)
        end_time = time()

        print("Meilleure combinaison d'actions pour maximiser le profit :")
        for action in best_combination:
            print(f"{action['name']} - Coût: {action['price']}€ - Bénéfice après 2 ans: {action['profit']}%")

        total_profit = calculate_profit(best_combination)
        total_cost = sum(action['price'] for action in best_combination)

        print(f"Profit total après 2 ans: {total_profit:.2f}€")
        print(f"Coût total: {total_cost:.2f}€")
        print(f"Temps d'exécution: {(end_time - start_time):.4f} secondes\n")


if __name__ == "__main__":
    main()
