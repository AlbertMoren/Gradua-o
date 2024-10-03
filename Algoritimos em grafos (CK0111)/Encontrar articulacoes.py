import grafo

# Função recursiva de busca em profundidade (DFS) para encontrar pontos de articulação em um grafo.
def dfs_articulacao(grafo, vertice, visitado, pai, tempo, low, disc, pontos_articulacao):
    
    filhos = 0
    visitado[vertice] = True
    disc[vertice] = low[vertice] = tempo[0]
    tempo[0] += 1
    
    for vizinho in grafo[vertice]:
        if not visitado[vizinho]:
            pai[vizinho] = vertice
            filhos += 1
            dfs_articulacao(grafo, vizinho, visitado, pai, tempo, low, disc, pontos_articulacao)
            
            
            low[vertice] = min(low[vertice], low[vizinho])
            
            
            if pai[vertice] is None and filhos > 1:
                pontos_articulacao.add(vertice)
            elif pai[vertice] is not None and low[vizinho] >= disc[vertice]:
                pontos_articulacao.add(vertice)
        elif vizinho != pai[vertice]:  
            low[vertice] = min(low[vertice], disc[vizinho])

# Função principal para encontrar os pontos de articulação em um grafo.
def encontrar_pontos_de_articulacao(grafo):
    num_vertices = len(grafo)
    visitado = [False] * num_vertices
    disc = [-1] * num_vertices
    low = [-1] * num_vertices
    pai = [None] * num_vertices
    pontos_articulacao = set()
    tempo = [0]
    
    for i in range(num_vertices):
        if not visitado[i]:
            dfs_articulacao(grafo, i, visitado, pai, tempo, low, disc, pontos_articulacao)
    
    return pontos_articulacao

grafo = {
    0: [1, 2, 6],
    1: [0, 2, 5],
    2: [0, 1, 3, 4],
    3: [2, 4, 5],
    4: [2, 3, 6],
    5: [1, 3],
    6: [0, 4]
}

pontos_articulacao = encontrar_pontos_de_articulacao(grafo)
print(f"Pontos de Articulação: {pontos_articulacao}")