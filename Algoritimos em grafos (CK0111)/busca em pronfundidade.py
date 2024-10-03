import grafo

#função de busca em profundidade em grafo não-direcionado usando pilha
def dfs(grafo,s):
    visited = []
    no_visited = []
    for i in range(len(grafo)):
        no_visited.append(i)
    stack = []
    stack.append(s)
    no_visited.remove(s)
    while len(stack) != 0 :
        v = stack.pop()
        visited.append(v)
        for u in grafo[v]:
            if u in no_visited:
                stack.append(u)
                no_visited.remove(u)
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