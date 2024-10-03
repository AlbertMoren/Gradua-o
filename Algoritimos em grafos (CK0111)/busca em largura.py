from queue  import Queue

# função de busca em largura em grafo não-direcionado
def bfs(grafo, V):
    no_visited = []
    visited = []
    for i in range(len(grafo)):
        no_visited.append(i)
    fila = Queue()
    fila.put(V)
    no_visited.remove(V)
    while not fila.empty():
        U = fila.get()
        visited.append(U)
        for i in grafo[U]:
            if i in no_visited:
                fila.put(i)
                no_visited.remove(i)
    return visited

grafo = {
    0: [1, 2, 6],
    1: [0, 2, 5],
    2: [0, 1, 3, 4],
    3: [2, 4, 5],
    4: [2, 3, 6],
    5: [1, 3],
    6: [0, 4]
}


ordem = bfs(grafo, 0)

for i in range(len(ordem)):
    if i < len(ordem) - 1:
        print(f"{ordem[i]} -> ", end="")
    else:
        print(f"{ordem[i]}")
