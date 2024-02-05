import uuid
import heapq
from collections import deque

import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, key, color="#1296F0"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла

    def get_total_nodes_number(self) -> int:
        number = 1
        if self.left:
            number += self.left.get_total_nodes_number()
        if self.right:
            number += self.right.get_total_nodes_number()
        return number


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)  # Використання id та збереження значення вузла
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}  # Використовуйте значення вузла для міток

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()


def build_heap_tree(heap_array: list, i = 0) -> Node | None:
    if len(heap_array) < i + 1:
        return None

    n = Node(heap_array[i])
    n.left = build_heap_tree(heap_array, 2*i + 1)
    n.right = build_heap_tree(heap_array, 2*i + 2)

    return n


def generate_color(step, total_steps):
    base_color = [135, 206, 250]
    darken_factor = step / (2 * total_steps)
    new_color = [int(c * (1 - darken_factor)) for c in base_color]
    return f'#{new_color[0]:02x}{new_color[1]:02x}{new_color[2]:02x}'


def color_tree_with_bfs_visualization(graph: Node):
    # Ініціалізація поточного кроку
    step = 0
    # Підраховуємо загальну кількість кроків
    total_steps = graph.get_total_nodes_number()
    # Ініціалізація черги з початковою вершиною
    queue = deque([graph])
    while queue:  # Поки черга не порожня, продовжуємо обхід
        # Вилучаємо першу вершину з черги
        vertex = queue.popleft()
        # Якщо отримали вершина None то закінчуємо фарбування
        if vertex is None:
            break
        # Збільшуємо крок
        step += 1
        # Генеруємо колір для поточної вершини
        vertex.color = generate_color(step, total_steps)
        # Додаємо всіх невідвіданих сусідів вершини до кінця черги
        queue.extend([vertex.left, vertex.right])


def color_tree_with_dfs_visualization(graph: Node):
    # Ініціалізація поточного кроку
    step = 0
    # Підраховуємо загальну кількість кроків
    total_steps = graph.get_total_nodes_number()
    # Використовуємо стек для зберігання вершин
    stack = [graph]
    while stack:
        # Вилучаємо вершину зі стеку
        vertex = stack.pop()
        # Якщо отримали вершину None то пропускаємо її
        if vertex is None:
            continue
        # Збільшуємо крок
        step += 1
        # Генеруємо колір для поточної вершини
        vertex.color = generate_color(step, total_steps)
        # Додаємо сусідні вершини до стеку
        stack.extend([vertex.right, vertex.left])


heap_array = [1, 3, 5, 7, 9, 2, 4, 34, 2, 1, 2]
heapq.heapify(heap_array)

tree = build_heap_tree(heap_array)

color_tree_with_bfs_visualization(tree)
# color_tree_with_dfs_visualization(tree)

draw_tree(tree)

