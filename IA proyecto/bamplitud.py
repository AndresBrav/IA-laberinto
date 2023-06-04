from collections import deque
from Casilla import *
lista=[]

def bfs(graph, start, goal):
    visited = set()
    queue = deque([(start, [])])

    while queue:
        node, path = queue.popleft()
        if node == goal:
            return path + [node]
        print(path)
        if node not in visited:
            visited.add(node)
            queue.extend((neighbor, path + [node]) for neighbor in graph[node])
            
    return None

# Ejemplo de uso

# Definir el grafo como un diccionario de listas de adyacencia
"""graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E','G'],
    'G':['F']
}"""
Sucre=Casilla("Sucre",1,"50",3)
graph = {
    'Sucre': ['Bascope'],
    'Bascope': ['Perez1'],
    'Perez1': ['Perez2','A71'],
    'A71':['Perez1','A72'],
    'A72':['A71','Br24'],
    'Perez2': ['Perez1','Perez3'],
    'Perez3':['Perez2','Perez4','Lopez1','Lopez2']
    }
def ingresarALista(cola):
    i=cola.__len__()-1
    while (i>=0):
        #añade el camino del final al inicio
        lista.append(cola.pop(i))
        i=i-1
    print(lista)

start_node =input("ingresa el inicio ") #A
goal_node =input("ingresa el destino ") #G

path = bfs(graph, start_node, goal_node)

if path:
    print(f"Se encontró un camino de {start_node} a {goal_node}: {path}")
    
    ingresarALista(path)

else:
    print(f"No se encontró un camino de {start_node} a {goal_node}.")


