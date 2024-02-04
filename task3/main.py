import heapq


def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex, in graph}
    processed = []
    heap = [(0, start)]

    while heap:
        dist, node = heapq.heappop(heap)

        # не опрацьовуємо вузол якщо його вже опрацьовано
        # так як ми в першу чергу опрацьовуємо вузли з найменшою вістаню від почтакової вершини
        # то в нас немає необхідності перезаписувати відстань якщо вона вже була записана
        if node in processed:
            continue

        distances[node] = dist
        for neighbor, weight in graph[node]:
            if neighbor not in processed:
                # додаємо вузол в купу з відстанню до нього від початкової вершини
                heapq.heappush(heap, (dist + weight, neighbor))

        processed.append(node)

    return distances


if __name__ == "__main__":
    graph_ = {
        'A': (('B', 5), ('C', 10)),
        'B': (('A', 5), ('D', 3)),
        'C': (('A', 10), ('D', 2)),
        'D': (('B', 3), ('C', 2), ('E', 4)),
        'E': (('D', 4), ),
        'F': (),
    }

    print(dijkstra(graph_, "A"))