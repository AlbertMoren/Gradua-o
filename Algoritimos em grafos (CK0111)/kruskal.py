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


grafo = {
    0: [(1, 4), (2, 1), (6, 3)],  
    1: [(0, 4), (2, 5), (5, 2)],  
    2: [(0, 1), (1, 5), (3, 3), (4, 2)],  
    3: [(2, 3), (4, 6), (5, 4)], 
    4: [(2, 2), (3, 6), (6, 5)],
    5: [(1, 2), (3, 4)],  
    6: [(0, 3), (4, 5)]   
}



agm, custo_total = kruskal(grafo)

print("Arestas na Árvore Geradora Mínima:")
for u, v, peso in agm:
    print(f"{u} - {v}, peso: {peso}")
print(f"Custo total da MST: {custo_total}")

