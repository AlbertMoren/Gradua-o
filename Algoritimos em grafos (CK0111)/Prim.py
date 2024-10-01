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


import GrafoPonderado
grafo = GrafoPonderado.criar_grafo()
grafo = GrafoPonderado.add_vertex(grafo,0)
grafo = GrafoPonderado.add_vertex(grafo,1)
grafo = GrafoPonderado.add_vertex(grafo,2)
grafo = GrafoPonderado.add_vertex(grafo,3)
grafo = GrafoPonderado.add_vertex(grafo,4)
grafo = GrafoPonderado.add_vertex(grafo,5)
grafo = GrafoPonderado.add_vertex(grafo,6)

GrafoPonderado.add_edge(grafo,0, 1, 7)
GrafoPonderado.add_edge(grafo,0, 2, 5)
GrafoPonderado.add_edge(grafo,1, 2, 10)
GrafoPonderado.add_edge(grafo,1, 4, 2)
GrafoPonderado.add_edge(grafo,1, 3, 18)
GrafoPonderado.add_edge(grafo,2, 6, 16)
GrafoPonderado.add_edge(grafo,2, 4, 3)
GrafoPonderado.add_edge(grafo,3, 4, 12)
GrafoPonderado.add_edge(grafo,3, 5, 4)
GrafoPonderado.add_edge(grafo,4, 6, 30)
GrafoPonderado.add_edge(grafo,5, 6, 26)
GrafoPonderado.add_edge(grafo,5, 4, 14)
GrafoPonderado.add_edge(grafo,1, 3, 18)

GrafoPonderado.print_graf(grafo)


agm, custo_total = prim(grafo)

print("\nÁrvore Geradora Mínima (MST):")
for u, v, peso in agm:
    print(f"{u} - {v}, peso: {peso}")
print(f"Custo total da MST: {custo_total}")
