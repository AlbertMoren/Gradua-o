import grafo

#função de busca em profundidade em grafo não-direcionado usando pilha
def dfs(grafo,V):
    visited = []
    no_visited = []
    for i in range(len(grafo)):
        no_visited.append(i)
    stack = []
    stack.append(V)
    no_visited.remove(V)
    while len(stack) != 0 :
        U = stack.pop()
        visited.append(U)
        for i in grafo[U]:
            if i in no_visited:
                stack.append(i)
                no_visited.remove(i)
    return visited

#Imprimi a ordem de como o grafo é visitado
def print_grafo(g):
    for i in range(len(g)):
        if i < len(g) - 1:
            print(f"{g[i]} -> ",end="")
        else:
            print(f"{g[i]}")


g = grafo.criar_grafo()
g = grafo.add_vertex(g,0)
g = grafo.add_vertex(g,2)
g = grafo.add_vertex(g,1)
g = grafo.add_vertex(g,3)
g = grafo.add_vertex(g,4)
g = grafo.add_vertex(g,5)
g = grafo.add_vertex(g,6)
grafo.add_edge(g,0,1)
grafo.add_edge(g,2,1)
grafo.add_edge(g,0,1)
grafo.add_edge(g,3,1)
grafo.add_edge(g,4,2)
grafo.add_edge(g,5,6)
grafo.print_graf(g)

ordem = dfs(g,0)
print_grafo(ordem)
for i in range(len(g)):
    if i not in ordem:
        ordem = dfs(g,i)
        print_grafo(ordem)