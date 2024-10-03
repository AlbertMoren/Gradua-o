import heapq

# Algoritmo de Dijkstra
def dijkstra(grafo, s):
    n = len(grafo)
    dist = {i: float('inf') for i in grafo}  
    dist[s] = 0  
    pai = {i: None for i in grafo}  
    heap = [(0, s)]  

    while heap:
        distancia_atual, u = heapq.heappop(heap)  
        if distancia_atual > dist[u]:
            continue

        # Relaxamento das arestas
        for vizinho, peso in grafo[u]:
            nova_dist = dist[u] + peso
            if nova_dist < dist[vizinho]:  
                dist[vizinho] = nova_dist
                pai[vizinho] = u  #
                heapq.heappush(heap, (nova_dist, vizinho))

    return dist, pai



# Função para criar o grafo a partir da lista de arestas
def criar_grafo(arestas):
    grafo = {}
    for u, v, peso in arestas:
        if u not in grafo:
            grafo[u] = []
        if v not in grafo:
            grafo[v] = []
        grafo[u].append((v, peso))
        grafo[v].append((u, peso))  
    return grafo

arestas = [
    (0, 1, 4),
    (0, 2, 1),
    (1, 2, 3),
    (1, 3, 2),
    (2, 3, 5),
    (3, 4, 1)
]

grafo = criar_grafo(arestas)  # Cria o grafo
s = 0  


distancias, pais = dijkstra(grafo, s)

# Exibe as distâncias mínimas e os caminhos
print("Distâncias a partir do vértice origem:")
for vertice, distancia in distancias.items():
    print(f"Vértice {vertice}: {distancia}")

