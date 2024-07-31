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


def dfs(grafo,v,visited=None):
    if visited == None:
        visited = []
    if v not in visited:
        visited.append(v)
        for i in grafo[v]:
            if i not in visited:
                dfs(grafo,i,visited)
    return visited

ordem = dfs(g,0)

for i in range(len(ordem)):
    if i < len(ordem) - 1:
        print(f"{ordem[i]} -> ",end="")
    else:
        print(f"{ordem[i]}")   
    