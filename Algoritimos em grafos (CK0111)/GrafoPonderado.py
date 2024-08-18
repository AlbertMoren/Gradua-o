def criar_grafo():
    grafo = []
    return grafo

def add_vertex(grafo,V):
    if V not in grafo:
        V = []
        grafo.append(V)
    return grafo
        
def add_edge(grafo,edge1,edge2,peso):
    if edge1 not in grafo[edge2] and edge2 not in grafo[edge1]:
        grafo[edge1].append((edge2,peso))
        grafo[edge2].append((edge1,peso))

def print_graf(grafo):
    for i in range(len(grafo)):
        print(f"[{i}] <- ",end="")
        for j in grafo[i]:
            print(f"[{j}]",end=" ")
        print("")
        



