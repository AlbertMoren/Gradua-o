import heapq

# Algoritmo de Prim para encontrar a Árvore Geradora Mínima (AGM) de um grafo ponderado.
def prim(grafo,vertici_inicial=0):
    n = len(grafo)
    visited = [False] * n
    agm = []
    custo_total = 0

    heap = [(0,vertici_inicial,vertici_inicial)]

    while heap:
        peso,u,v = heapq.heappop(heap)
        if not visited[v]:
            visited[v] = True
            if u != v :
                agm.append((u,v,peso))
                custo_total += peso
            
            for vizinho,peso in grafo[v]:
                if not visited[vizinho]:
                    heapq.heappush(heap, (peso,v,vizinho))
            
    return agm, custo_total


grafo = {
    0: [(1, 4), (2, 1), (6, 3)],  
    1: [(0, 4), (2, 5), (5, 2)],  
    2: [(0, 1), (1, 5), (3, 3), (4, 2)],  
    3: [(2, 3), (4, 6), (5, 4)], 
    4: [(2, 2), (3, 6), (6, 5)],
    5: [(1, 2), (3, 4)],  
    6: [(0, 3), (4, 5)]   
}


agm, custo_total = prim(grafo)

print("\nÁrvore Geradora Mínima (MST):")
for u, v, peso in agm:
    print(f"{u} - {v}, peso: {peso}")
print(f"Custo total da MST: {custo_total}")
