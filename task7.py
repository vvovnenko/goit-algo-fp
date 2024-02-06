import random

import matplotlib.pyplot as plt


def monte_carlo_simulation(num_experiments=15000):
    hits = { key: 0 for key in range(2, 13)}
    for _ in range(num_experiments):
        dice_sum = random.randint(1, 6) + random.randint(1, 6)
        hits[dice_sum] += 1

    return {key: value / num_experiments for key, value in hits.items()}


if __name__ == "__main__":
    analytic_probabilities = {
        2: 1 / 36,
        3: 2 / 36,
        4: 3 / 36,
        5: 4 / 36,
        6: 5 / 36,
        7: 6 / 36,
        8: 5 / 36,
        9: 4 / 36,
        10: 3 / 36,
        11: 2 / 36,
        12: 1 / 36,
    }

    probabilities = monte_carlo_simulation(1000000)

    print(f"| {'Сума':<10} | {'Розрахована імовірність':<25} | {'Аналітична імовірність':<25} |")
    print(f"| :{'-'*9} | :{'-'*24} | :{'-'*24} |")
    for cubes_sum, prob in probabilities.items():
        print(f"| {cubes_sum:<10} | {prob:<25.2%} | {analytic_probabilities[cubes_sum]:<25.2%} |")

    plt.bar(probabilities.keys(), probabilities.values())  # noqa
    plt.show()