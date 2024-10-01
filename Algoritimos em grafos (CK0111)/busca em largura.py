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

import grafo

g = grafo.criar_grafo()
g = grafo.add_vertex(g,0)
g = grafo.add_vertex(g,2)
g = grafo.add_vertex(g,1)
g = grafo.add_vertex(g,3)
g = grafo.add_vertex(g,4)
grafo.add_edge(g,0,1)
grafo.add_edge(g,2,1)
grafo.add_edge(g,0,1)
grafo.add_edge(g,3,1)
grafo.add_edge(g,4,2)
grafo.print_graf(g)


ordem = bfs(g,0)

for i in range(len(ordem)):
    if i < len(ordem) - 1:
        print(f"{ordem[i]} -> ",end="")
    else:
        print(f"{ordem[i]}")