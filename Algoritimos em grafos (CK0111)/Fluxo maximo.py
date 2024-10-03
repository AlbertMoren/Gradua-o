from collections import  deque
# Busca em largura para encontrar um caminho aumentante.
def bfs(grafo, fonte, sink, pais):
    visitado = set()
    fila = deque([fonte])
    visitado.add(fonte)

    while fila:
        u = fila.popleft()

        for v in grafo[u]:
            if v not in visitado and grafo[u][v] > 0:
                visitado.add(v)
                fila.append(v)
                pais[v] = u  
                if v == sink:
                    return True
    return False

# Calcula o fluxo máximo usando o algoritmo de Ford-Fulkerson.
def fluxo_maximo(grafo, fonte, sink):
    
    max_fluxo = 0
    pais = {}

    while bfs(grafo, fonte, sink, pais):
        caminho_fluxo = float('Inf')
        v = sink
        while v != fonte:
            u = pais[v]
            caminho_fluxo = min(caminho_fluxo, grafo[u][v])
            v = u
        v = sink
        while v != fonte:
            u = pais[v]
            grafo[u][v] -= caminho_fluxo
            grafo[v][u] += caminho_fluxo
            v = u
        max_fluxo += caminho_fluxo
    return max_fluxo


grafo = {
    0: {1: 16, 2: 13},
    1: {0: 0, 2: 10, 3: 12},
    2: {0: 0, 1: 4, 4: 14},
    3: {1: 0, 2: 9, 5: 20},
    4: {2: 0, 3: 7, 5: 4},
    5: {3: 0, 4: 0}
}


fluxo = fluxo_maximo(grafo, 0, 4)
print(f"O fluxo máximo é: {fluxo}")
