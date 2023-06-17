from collections import deque
from Casilla import *
from GraficarCamino import *
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
            try:
                visited.add(node)
                queue.extend((neighbor, path + [node]) for neighbor in graph[node])
            except Exception:
                print("problemas con el nodo")
    return None

# Ejemplo de uso

# Definir el grafo como un diccionario de listas de adyacencia
"""
graph = {
    'Sucre': ['Bascope'],
    'Bascope': ['Perez1'],
    'Perez1': ['Perez2','A71'],
    'A71':['Perez1','A72'],
    'A72':['A71','Br24'],
    'Br24':['A72','Perez2','Perez3'],
    'Perez2': ['Perez1','Perez3'],
    'Perez3':['Perez2','Lopez2','Perez4','Lopez1'],
    'Perez4': ['Lopez1','Perez3','Lopez2'],
    'Lopez2': ['BlancoG1','BGalindo2','Lopez3'],
    'Lopez3': ['Bravo3'],
    'Bravo3': ['Bravo2','Juan1'],
    'Bravo2': ['Bravo3','Torrez1','Juan1','Bravo1'],
    'Torrez1': ['Frias','Torrez2','Bravo2','Bravo1'],
    'Juan1': ['Bravo3','Frias','Juan2','Bravo2'],
    }
"""
#
graph = {
    'Gotham1':  ['Gotham2','Melrose4'],
    'Gotham2':  ['Gotham1','Gotham3','Melrose4','Southpark3','Southpark4'],
    'Gotham3':  ['Gotham2','Gotham4','Southpark3','Southpark4','Elmwood1'],
    'Gotham4':  ['Gotham3','Gotham5','Elmwood1','Bourbon2','Bourbon3'],
    'Gotham5':  ['Gotham4','Gotham6','Bourbon2','Bourbon3','Baker3','Baker4'],
    'Gotham6':  ['Gotham5','Baker3','Baker4'],


    'Acacia1':  ['Acacia2','Acme2','Acme3'],
    'Acacia2':  ['Acacia1','Acacia3','Acme2','Acme3','Southpark3','Southpark4',],
    'Acacia3':  ['Acacia2','Acacia4','Southpark3','Southpark4','Elmwood2','Elmwood3'],
    'Acacia4':  ['Acacia3','Acacia5','Elmwood2','Elmwood3','Bourbon4','Bourbon5'],
    'Acacia5':  ['Acacia4','Bourbon4','Bourbon5','Baker4'],

    'Esquina1':  ['Esquina2','Southpark6','Southpark7'],
    'Esquina2':  ['Esquina1','Southpark6','Southpark7','Elmwood4'],
    'Carnaby1':  ['Carnaby2','Acme3'],
    'Carnaby2':  ['Carnaby1','Carnaby3','Acme3','Southpark5','Southpark6'],
    'Carnaby3':  ['Carnaby2','Carnaby4','Southpark5','Southpark6','Elmwood3','Elmwood4'],
    'Carnaby4':  ['Carnaby3','Elmwood3','Elmwood4','Bourbon5'],

    'Acme1':  ['Acme2'],
    'Acme2':  ['Acme1','Acme3','Acacia1','Acacia2'],
    'Acme3':  ['Acme2','Acacia1','Acacia2','Carnaby1','Carnaby2'],

    'B11':  ['B12','Melrose3','Melrose4'],
    'B12':  ['B11','Melrose3','Melrose4','Southpark2','Southpark3'],
    'B13':  ['B12','Southpark2','Southpark3','B23'],

    'Elm':  ['Elmwood1','Elmwood2','Bourbon3','Bourbon4'],

    'Elmwood1':  ['Elmwood2','Gotham3','Gotham4','Elm'],
    'Elmwood2':  ['Elmwood1','Elmwood3','Elm','Acacia3','Acacia4'],
    'Elmwood3':  ['Elmwood2','Elmwood4','Acacia3','Acacia4','Carnaby3','Carnaby4'],
    'Elmwood4':  ['Elmwood4','Carnaby3','Carnaby4','Esquina2'],

    'Bourbon1':  ['Bourbon2','Elmore10','Elmore11','Mendoza1'],
    'Bourbon2':  ['Bourbon1','Bourbon3','Mendoza1','Gotham4','Gotham5'],
    'Bourbon3':  ['Bourbon2','Bourbon4','Gotham4','Gotham5','Elm'],
    'Bourbon4':  ['Bourbon3','Bourbon5','Elm','Acacia4','Acacia5'],
    'Bourbon5':  ['Bourbon4','Acacia4','Acacia5','Carnaby4'],

    'Baker1':  ['Baker2','Wallstreet4','Wallstreet5'],
    'Baker2':  ['Baker1','Baker3'],
    'Baker3':  ['Baker2','Baker4','Gotham5','Gotham6'],
    'Baker4':  ['Baker3','Gotham5','Gotham6','Acacia5'],
    'Melrose1':  ['Melrose2','Nogal1','Nogal2'],
    'Melrose2':  ['Melrose1','Melrose3','Nogal1','Nogal2','Elmore7','Elmore8'],
    'Melrose3':  ['Melrose2','Melrose4','Elmore7','Elmore8','B11','B12'],
    'Melrose4':  ['Melrose3','Elmore8','B11','B12','Gotham1','Gotham2'],
    'Southpark1':  ['Southpark2','Nogal2','Nogal3','Elmore8','Elmore9'],
    'Southpark2':  ['Southpark1','Southpark3','Elmore8','Elmore9','B12','B13'],
    'Southpark3':  ['Southpark2','Southpark4','B12','B13','Gotham2','Gotham3'],
    'Southpark4':  ['Southpark3','Southpark5','Gotham2','Gotham3','Acacia2','Acacia3'],
    'Southpark5':  ['Southpark4','Southpark6','Acacia2','Acacia3','Carnaby2','Carnaby3'],
    'Southpark6':  ['Southpark5','Southpark7','Carnaby2','Carnaby3','Esquina1','Esquina2'],
    'Southpark7':  ['Southpark6','Southpark8','Esquina1','Esquina2'],
    'Southpark8':  ['Southpark7'],
    'B21':  ['B22','Nogal3','Nogal4'],
    'B22':  ['B21','B23','Nogal3','Nogal4','Elmore9','Elmore10'],
    'B23':  ['B22','Elmore9','Elmore10','B13'],
    'Wallstreet1':  ['Wallstreet2','Nogal4'],
    'Wallstreet2':  ['Wallstreet1','Wallstreet3','Nogal4','Elmore11','Elmore12'],
    'Wallstreet3':  ['Wallstreet2','Wallstreet4','Elmore11','Elmore12','Mendoza1','Mendoza2'],
    'Wallstreet4':  ['Wallstreet2','Wallstreet4','Mendoza1','Mendoza2','Baker1'],
    'Wallstreet5':  ['Wallstreet4','Baker1'],
    'A11':  ['A21','Mendoza2','Mendoza3'],
    'A21':  ['A11','Springfield15','Springfield16'],
    'Arkham1':  ['Arkham2','Elmore4','Elmore5','Piedradura2','Piedradura3'],
    'Arkham2':  ['Arkham1','Arkham3','Piedradura2','Piedradura3','Foster1','Foster2'],
    'Arkham3':  ['Arkham2','Foster1','Foster2','C3'],
    'Foster1':  ['Foster2','Arkham2','Arkham3'],
    'Foster2':  ['Foster1','Arkham2','Arkham3'],
    'Piedradura1':  ['Piedradura2','C1','C2'],
    'Piedradura2':  ['Piedradura1','Piedradura3','C2','Arkham1','Arkham2'],
    'Piedradura3':  ['Piedradura2','Arkham1','Arkham2'],
    'Nogal1':  ['Nogal2','Melrose1','Melrose2'],
    'Nogal2':  ['Nogal1','Nogal3','Melrose1','Melrose2','Southpark1'],
    'Nogal3':  ['Nogal2','Nogal4','Southpark1','B21','B22'],
    'Nogal4':  ['Nogal3','B21','B22','Wallstreet1','Wallstreet2'],
    'C1':  ['Elmore1','Elmore2','Piedradura1'],
    'C2':  ['Elmore2','Elmore3','Piedradura1','Piedradura2'],
    'C3':  ['Arkham3'],
    'Mar1':  ['Mar2','Olmos3','Olmos4'],
    'Mar2':  ['Mar1','Mar3','Olmos3','Olmos4','Siempreviva3','Siempreviva4'],
    'Mar3':  ['Mar2','Siempreviva3','Siempreviva4','Metroville2','Millaverde6','Millaverde7'],
    'Olmos1':  ['Olmos2','Elmwood21','España6'],
    'Olmos2':  ['Olmos1','Olmos3','Elmwood21','Aroma5','Aroma6'],
    'Olmos3':  ['Olmos2','Olmos4','Aroma5','Aroma6','Mar1','Mar2'],
    'Olmos4':  ['Olmos3','Olmos5','Mar1','Mar2','LosLaureles3','LosLaureles4'],
    'Olmos5':  ['Olmos4','LosLaureles3','LosLaureles4','Elmore3','Elmore4'],
    'Siempreviva1':  ['Siempreviva2','Elmwood21','Elmwood22'],
    'Siempreviva2':  ['Siempreviva1','Siempreviva3','Elmwood21','Elmwood22','Aroma6','Aroma7'],
    'Siempreviva3':  ['Siempreviva2','Siempreviva4','Aroma6','Aroma7','Mar2','Mar3'],
    'Siempreviva4':  ['Siempreviva3','Mar2','Mar3','LosLaureles4','LosLaureles5'],
    'Metroville1':  ['Metroville2','Elmwood22','Elmwood23','Aroma7','Aroma8'],
    'Metroville2':  ['Metroville1','Aroma7','Aroma8','Mar3','Millaverde6','Millaverde7'],
    'Coronado1':  ['Coronado2','Peachtree1'],
    'Coronado2':  ['Coronado1','Coronado3','Peachtree1','Elmwood23','Elmwood24'],
    'Coronado3':  ['Coronado2','Coronado4','Elmwood23','Elmwood24','Aroma8','Millaverde5','Millaverde6'],
    'Coronado4':  ['Coronado3','Coronado5','Aroma8','Millaverde4','Millaverde5','AbbeyRoad1'],
    'Coronado5':  ['Coronado4','AbbeyRoad1'],
    'Salero1':  ['Elmwood24','Peachtree1','Peachtree2'],
    'Salero2':  ['Salero3','Millaverde2','Millaverde3','AbbeyRoad2','AbbeyRoad3'],
    'Salero3':  ['Salero2','AbbeyRoad2','AbbeyRoad3'],
    'Nintendo1':  ['Nintendo2','Peachtree2','Peachtree3','Millaverde1','Millaverde2'],
    'Nintendo2':  ['Nintendo1','Nintendo3','Millaverde1','Millaverde2'],
    'Nintendo3':  ['Nintendo2','Springfield9','Springfield10'],
    'AbbeyRoad1':  ['AbbeyRoad2','Coronado4','Coronado5','D1'],
    'AbbeyRoad2':  ['AbbeyRoad1','AbbeyRoad3','D1','Salero2','Salero3'],
    'AbbeyRoad3':  ['AbbeyRoad2','AbbeyRoad4','Salero2','Salero3','Luna'],
    'AbbeyRoad4':  ['AbbeyRoad3','AbbeyRoad5','Luna','Springfield10','Springfield11'],
    'AbbeyRoad5':  ['AbbeyRoad4','AbbeyRoad6','Springfield10','Springfield11','Brisa1'],
    'AbbeyRoad6':  ['AbbeyRoad5','AbbeyRoad7','Brisa1'],
    'AbbeyRoad7':  ['AbbeyRoad6','Belfort1'],
    'Elmwood21':  ['Elmwood22','Olmos1','Olmos2','Siempreviva1','Siempreviva2'],
    'Elmwood21':  ['Elmwood22','Olmos1','Olmos2','Siempreviva1','Siempreviva2'],
    'Elmwood22':  ['Elmwood21','Elmwood23','Siempreviva1','Siempreviva2','Metroville1'],
    'Elmwood23':  ['Elmwood22','Elmwood24','Metroville1','Coronado2','Coronado3'],
    'Elmwood24':  ['Elmwood23','Coronado2','Coronado3','Salero1'],
    'Peachtree1':  ['Peachtree2','Coronado1','Coronado2','Salero1'],
    'Peachtree2':  ['Peachtree1','Peachtree3','Salero1','Nintendo1'],
    'Peachtree3':  ['Peachtree2','Peachtree4','Nintendo1','Springfield5','Springfield6'],
    'Peachtree4':  ['Peachtree3','Peachtree5','Springfield5','Springfield6','Luz'],
    'Peachtree5':  ['Peachtree4','Peachtree6','Luz','Nube1','Nube2'],
    'Peachtree6':  ['Peachtree5','Peachtree7','Nube1','Nube2','Vida'],
    'Peachtree7':  ['Peachtree6','Vida','Belfort1'],
    'Luna':  ['AbbeyRoad3','AbbeyRoad4'],
    'Luz':  ['Peachtree4','Peachtree5'],
    'D1':  ['AbbeyRoad1','AbbeyRoad2','Millaverde3','Millaverde4'],
    'Vida':  ['Peachtree6','Peachtree7'],
    'Nube1':  ['Nube2','Springfield7','Springfield8','Peachtree5','Peachtree6'],
    'Nube2':  ['Nube1','Peachtree5','Peachtree6'],
    'Alba':  ['Brisa1','Brisa2'],
    'Brisa1':  ['Brisa2','Alba','AbbeyRoad5','AbbeyRoad6'],
    'Brisa2':  ['Brisa1','Alba'],
    'Aroma1':  ['Aroma2'],
    'Aroma2':  ['Aroma1','Aroma3'],
    'Aroma3':  ['Aroma2','Aroma4'],
    'Aroma4':  ['Aroma3','Aroma5'],
    'Aroma5':  ['Aroma4','Aroma6','Olmos2','Olmos3'],
    'Aroma6':  ['Aroma5','Aroma7','Olmos2','Olmos3','Siempreviva2','Siempreviva3'],
    'Aroma7':  ['Aroma6','Aroma8','Siempreviva2','Siempreviva3','Metroville1','Metroville2'],
    'Aroma8':  ['Aroma7','Metroville1','Metroville2','Coronado3','Coronado4','Millaverde4','Millaverde5'],
    'Elmore1':  ['Elmore2','C1'],
    'Elmore2':  ['Elmore1','Elmore3','C1','C2','Ayacucho1'],
    'Elmore3':  ['Elmore2','Elmore4','C2','Ayacucho1','Olmos5'],
    'Elmore4':  ['Elmore3','Elmore5','Olmos5','Arkham1'],
    'Elmore5':  ['Elmore4','Elmore6','Arkham1','Arkham1','Millaverde8'],
    'Elmore6':  ['Elmore5','Elmore7','Millaverde8'],
    'Elmore7':  ['Elmore6','Elmore8','Melrose2','Melrose3'],
    'Elmore8':  ['Elmore7','Elmore9','Melrose2','Melrose3','Southpark1','Southpark2'],
    'Elmore9':  ['Elmore8','Elmore10','Southpark1','Southpark2','B22','B23'],
    'Elmore10':  ['Elmore9','Elmore11','B22','B23','Bourbon1'],
    'Elmore11':  ['Elmore10','Elmore12','Bourbon1','Wallstreet2','Wallstreet3'],
    'Elmore12':  ['Elmore11','Wallstreet2','Wallstreet3','Springfield13','Springfield14'],
    'Springfield1':  ['Springfield2'],
    'Springfield2':  ['Springfield1','Springfield3'],
    'Springfield3':  ['Springfield2','Springfield4'],
    'Springfield4':  ['Springfield3','Springfield5'],
    'Springfield5':  ['Springfield4','Springfield6','Peachtree3','Peachtree4'],
    'Springfield6':  ['Springfield5','Springfield7','Peachtree3','Peachtree4','Millaverde1'],
    'Springfield7':  ['Springfield6','Springfield8','Millaverde1','Nube1'],
    'Springfield8':  ['Springfield7','Springfield9','Nube1','Belfort1'],
    'Springfield9':  ['Springfield8','Springfield10','Belfort1','Nintendo3'],
    'Springfield10':  ['Springfield9','Springfield11','Nintendo3','AbbeyRoad4','AbbeyRoad5'],
    'Springfield11':  ['Springfield10','Springfield12','AbbeyRoad4','AbbeyRoad5'],
    'Springfield12':  ['Springfield11','Springfield13'],
    'Springfield13':  ['Springfield12','Springfield14','Elmore12'],
    'Springfield14':  ['Springfield13','Springfield15','Elmore12','Mendoza','Mendoza'],
    'Springfield15':  ['Springfield14','Springfield16','Mendoza','Mendoza','Allende','A21'],
    'Springfield16':  ['Springfield15','Allende','A21'],
    'Millaverde1':  ['Millaverde2','Springfield6','Springfield7','Nintendo1','Nintendo2'],
    'Millaverde2':  ['Millaverde1','Millaverde3','Nintendo1','Nintendo2','Salero2'],
    'Millaverde3':  ['Millaverde2','Millaverde4','Salero2','D1'],
    'Millaverde4':  ['Millaverde3','Millaverde5','D1','Coronado3','Coronado4','Aroma8'],
    'Millaverde5':  ['Millaverde4','Millaverde6','Coronado3','Coronado4','Aroma8'],
    'Millaverde6':  ['Millaverde5','Millaverde7','Metroville2','Mar3'],
    'Millaverde7':  ['Millaverde6','Millaverde8','Metroville2','Mar3','LosLaureles'],
    'Millaverde8':  ['Millaverde7','LosLaureles','Elmore5','Elmore6'],
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

#agregamos para graficar
cargarGrafico(lista)

