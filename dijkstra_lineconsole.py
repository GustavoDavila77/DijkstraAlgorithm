def entrada_nodos():
    print('Para terminar un proceso oprima %')
    print('Ingrese los nodos a utilizar')
    nodo = '$' #se asigna un val any
    nodes = []
    while nodo != '%':
        nodo = input()
        if nodo is not '%':
            nodes.append(nodo)
    print(nodes)
    return nodes

def entrada_distances():
    print('Entrada de distancias')
    node = '$'
    distances = {}

    while node != '%':     
        distance = None
        #print('ingrese el nodo')
        node = input("ingrese el nodo: ")
        if node is not '%':
            nodo_vecino = '$'
            vecinos = {}

            while nodo_vecino != '%':
                nodo_vecino = input("ingrese el vecino: ")

                if nodo_vecino is not '%':
                    distance = int(input("ingrese la distancia al nodo: "))
                    vecinos[nodo_vecino] = distance
                    print(vecinos)
            distances[node] = vecinos
    
    print(distances)
    return distances

def entrada_current(nodes):
    return input('Ingrese el nodo referencia/actual: ')

def main():

    nodes = entrada_nodos()
    current = entrada_current(nodes)
    if current not in nodes:
        print('no esta en los nodos')
    else:
        distances = entrada_distances()

        dis_unvisited = {node: None for node in nodes} #se usa None como +inf, en principio todos tienen inf como distancia
        #print(dis_unvisited)
        visited = {}
        currentDistance = 0 #distancia del nodo actual
        dis_unvisited[current] = currentDistance  #para los nodos no visitados se almacena las distancias actuales
        print('************')
        print(dis_unvisited)

        stop = False
        while not stop:
            #se hace un recorrido por cada uno de los vecinos
            for neighbour, distance in distances[current].items():
                if neighbour not in dis_unvisited:  continue #si ya ha sido visitado, continue con la siguiente iteración en caso que no este dentro de los no visitados
                
                newDistance = currentDistance + distance
                if dis_unvisited[neighbour] is None or dis_unvisited[neighbour] > newDistance: #si la distancia es inf o la distancia actual del vecino es mayor, entonces actualizar la distancias actual por la nueba
                    dis_unvisited[neighbour] = newDistance

            visited[current] = currentDistance #se almacena la distancia actual para cada nodo 
            del dis_unvisited[current] #se borra del diccionario de no visitados el respectivo nodo 
            if not dis_unvisited: #si no hay nodos para visitar, salirse
                stop = True
                break
            
            #se obtienen cada uno de los candidatos para ser el nuevo nodo actual -- current
            candidates = [node for node in dis_unvisited.items() if node[1]]
            
            #Si no se escribio ninguna condición, los candidatos tienden a quedar vacios
            #se evita que el programa falle en el ordenado
            if candidates:
                print(candidates)
                current, currentDistance = sorted(candidates, key= lambda x: x[1])[0]  #key es para extraer una comparación de una lista (candidatos) y luego se ordenan esos candidatos
                print('Nuevo nodo actual')
                print(current)
            else:
                break

        #print('visitados')  
        print(visited)

if __name__ == "__main__":
    main()

    """
    #ejem 2
    nodes = ('A', 'B', 'C', 'D', 'E')
    current = 'C' #declaramos el nodo actual
    distances = {
        'C': {'A': 1, 'B': 7, 'D': 2},
        'A': {'C': 1, 'B': 3},
        'B': {'A': 3, 'C': 7, 'D': 5, 'E': 1},   
        'D': {'C': 2, 'B': 5},
        'E': {'B': 1, 'D': 7}}

    #ejem1
    nodes = ('A', 'B', 'C', 'D', 'E', 'F', 'G')
    current = D
    distances = {
        'B': {'A': 5, 'D': 1, 'G': 2},
        'A': {'B': 5, 'D': 3, 'E': 12, 'F' :5},
        'D': {'B': 1, 'G': 1, 'E': 1, 'A': 3},
        'G': {'B': 2, 'D': 1, 'C': 2},
        'C': {'G': 2, 'E': 1, 'F': 16},
        'E': {'A': 12, 'D': 1, 'C': 1, 'F': 2},
        'F': {'A': 5, 'E': 2, 'C': 16}}
         """

