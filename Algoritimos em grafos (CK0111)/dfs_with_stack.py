import grafo



def dfs(grafo,V):
    visited = []
    no_visited = []
    for i in range(len(grafo)):
        no_visited.append(i)
    stack = []#declared a stack
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

ordem = dfs(g,0)

for i in range(len(ordem)):
    if i < len(ordem) - 1:
        print(f"{ordem[i]} -> ",end="")
    else:
        print(f"{ordem[i]}")