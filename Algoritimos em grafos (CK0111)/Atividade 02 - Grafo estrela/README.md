## **Universidade Federal do Ceará** | **Departamento de Computação**
### **Disciplina: Algoritmos em Grafos - CK226** | **Professor:  Pablo Mayckon Silva Farias**

#### Atividade 2 - Verificar se é um grafo estrela

Eescreva um algoritmo que receba como entrada um grafo não-direcionado de pelo menos 3 vértices e que informe, através de um booleano, se se trata ou não de um grafo estrela.


Algoritimo: Grafo_estrela

Entrada: Grafo não direcionado G=(V,E)

Pré-condição: V ∉ &empty; e |N| >= 3

Saída: Booleano

Pós-condição: ∀ y ∈ V; d(y) = n-1 e ∀ x-{y} ∈ V, d(x) = 1 onde V ≠ &empty;