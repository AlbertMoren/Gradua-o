# Uma estrutura de dados eficiente utilizada para gerenciar e unir conjuntos disjuntos
class UnionFind:
    def __init__(self,n):
        self.pai = list(range(n))
        self.rank =  [0] * n
    
    # Encontra a raiz do conjunto ao qual o elemento u pertence, aplicando compressão de caminho.
    def find(self,u):
        if self.pai[u] != u:
            self.pai[u] = self.find(self.pai[u])
        return self.pai[u]
    
    # Une os conjuntos que contêm os elementos u e v.
    def union(self,u,v):
        raiz_u = self.find(u)
        raiz_v = self.find(v)

        if raiz_u != raiz_v:
            if self.rank[raiz_u] > self.rank[raiz_v]:
                self.pai[raiz_v] = raiz_u
            elif self.rank[raiz_u] < self.rank[raiz_v]:
                self.pai[raiz_u] = raiz_v
            else:
                self.pai[raiz_v] = raiz_u
                self.rank[raiz_u] += 1

# Implementa o algoritmo de Kruskal para encontrar a Árvore Geradora Mínima (AGM) de um grafo ponderado.  
def kruskal(grafo):
    n = len(grafo)
    arestas = []
    for u in range(n):
        for v, peso in grafo[u]:
            if u < v:  
                arestas.append((peso, u, v))
    arestas.sort()
    uf = UnionFind(n)
    agm = []
    custo_total = 0
    for peso, u, v in arestas:
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            agm.append((u, v, peso))
            custo_total += peso
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


agm, custo_total = kruskal(grafo)

print("Arestas na Árvore Geradora Mínima:")
for u, v, peso in agm:
    print(f"{u} - {v}, peso: {peso}")
print(f"Custo total da MST: {custo_total}")

