import grafo

#função de busca em profundidade em grafo não-direcionado usando recursividade
def dfs(grafo,v,visited=None):
    if visited == None:
        visited = []
    if v not in visited:
        visited.append(v)
        for i in grafo[v]:
            if i not in visited:
                dfs(grafo,i,visited)
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

ordem = dfs(grafo, 0)

for i in range(len(ordem)):
    if i < len(ordem) - 1:
        print(f"{ordem[i]} -> ", end="")
    else:
        print(f"{ordem[i]}")