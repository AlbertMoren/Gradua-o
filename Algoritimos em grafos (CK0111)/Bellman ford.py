# Algoritmo de Bellman-Ford para encontrar o caminho mais curto de um vértice fonte a todos os outros vértices.
def bellman_ford(grafo, s):
    distancias = {v: float('inf') for v in range(len(grafo))} # info, representa infinito
    distancias[s] = 0
    pai = {v: None for v in range(len(grafo))}

    # Relaxação das arestas
    for _ in range(len(grafo) - 1):
        for u, v, peso in grafo:
            if distancias[u] != float('inf') and distancias[u] + peso < distancias[v]:
                distancias[v] = distancias[u] + peso
                pai[v] = u

    # Verificação de ciclos negativos
    for u, v, peso in grafo:
        if distancias[u] != float('inf') and distancias[u] + peso < distancias[v]:
            raise ValueError("O grafo contém um ciclo negativo.")

    return distancias, pai

grafo = [
    (0, 1, 4),
    (0, 2, 1),
    (1, 2, -3),
    (1, 3, 2),
    (2, 1, 3),
    (2, 3, 5),
    (3, 0, 1)
]

# impressões de resultado
s = 0
distancias, pais = bellman_ford(grafo, s)
print("\nResultado do Algoritmo de Bellman-Ford:")
print(f"{'Vértice':<10} {'Distância':<10} {'Pai':<10}")
print("-" * 30)
for v in range(len(grafo)):
    distancia = distancias[v] if distancias[v] != float('inf') else '∞'
    print(f"{v:<10} {distancia:<10} {pais[v] if pais[v] is not None else 'None':<10}")

