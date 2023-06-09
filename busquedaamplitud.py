from collections import deque

def bfs(graph, start, goal):
    visited = set()
    queue = deque([(start, [])])

    while queue:
        node, path = queue.popleft()
        if node == goal:
            return path + [node]
        if node not in visited:
            visited.add(node)
            queue.extend((neighbor, path + [node]) for neighbor in graph[node])

    return None

# Ejemplo de uso

# Definir el grafo como un diccionario de listas de adyacencia
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E','G'],
    'G':['F']
}

start_node =input("ingresa el inicio ") #A
goal_node =input("ingresa el destino ") #G

path = bfs(graph, start_node, goal_node)
if path:
    print(f"Se encontró un camino de {start_node} a {goal_node}: {path}")
else:
    print(f"No se encontró un camino de {start_node} a {goal_node}.")
