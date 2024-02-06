def greedy_algorithm(items: dict, budget: int):
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories']/x[1]['cost'], reverse=True)
    picked_items = []
    for name, item in sorted_items:
        if budget >= item['cost']:
            budget -= item['cost']
            picked_items.append(name)
    return picked_items


def dynamic_programming(items: dict, budget: int):
    n = len(items)
    cost = list(map(lambda d: d['cost'], items.values()))
    calories = list(map(lambda d: d['calories'], items.values()))

    # створюємо таблицю K для зберігання оптимальних значень підзадач та наборів продуктів
    K = [[(0, set([])) for w in range(budget + 1)] for i in range(n + 1)]

    # будуємо таблицю K знизу вгору
    for i in range(1, n + 1):
        for w in range(1, budget + 1):
            if cost[i - 1] <= w:
                current_optimal = (calories[i - 1] + K[i - 1][w - cost[i - 1]][0], set.union(K[i - 1][w - cost[i - 1]][1], {i}))
                previous_optimal = K[i - 1][w]
                K[i][w] = max([current_optimal, previous_optimal], key=lambda item: item[0])
            else:
                K[i][w] = K[i - 1][w]

    names = list(items.keys())
    return list(map(lambda i: names[i -1], K[n][budget][1]))


if __name__ == "__main__":
    items = {
        "pizza": {"cost": 50, "calories": 300},
        "hamburger": {"cost": 40, "calories": 250},
        "hot-dog": {"cost": 30, "calories": 200},
        "pepsi": {"cost": 10, "calories": 100},
        "cola": {"cost": 15, "calories": 220},
        "potato": {"cost": 25, "calories": 350}
    }

    max_cost = 35

    print('items: ')
    for name, data in items.items():
        print('\t', name, ':', data)
    print('max_cost: ', max_cost)
    print('greedy_algorithm: ', greedy_algorithm(items, 35))
    print('dynamic_programming: ', dynamic_programming(items, 35))
