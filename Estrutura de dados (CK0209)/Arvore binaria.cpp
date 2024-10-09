#include <iostream>

using namespace std;

// Definição da estrutura de um nó da árvore
struct No {
    int valor;
    No* esquerdo;
    No* direito;

    // Construtor para criar um nó com um valor
    No(int v) {
        valor = v;
        esquerdo = nullptr;
        direito = nullptr;
    }
};

// Classe que implementa a árvore binária
class ArvoreBinaria {
private:
    No* raiz;

    // Função recursiva para inserir um novo valor
    No* inserirRecursivo(No* no, int valor) {
        if (no == nullptr) {
            return new No(valor); 
        }

        if (valor < no->valor) {
            no->esquerdo = inserirRecursivo(no->esquerdo, valor);  
        } else if (valor > no->valor) {
            no->direito = inserirRecursivo(no->direito, valor);  
        }

        return no;
    }

    // Função recursiva para exibir os valores em ordem (esquerda, raiz, direita)
    void emOrdemRecursivo(No* no) {
        if (no != nullptr) {
            emOrdemRecursivo(no->esquerdo);
            cout << no->valor << " ";
            emOrdemRecursivo(no->direito);
        }
    }

    // Função recursiva para buscar um valor na árvore
    No* buscarRecursivo(No* no, int valor) {
        if (no == nullptr || no->valor == valor) {
            return no;  
        }

        if (valor < no->valor) {
            return buscarRecursivo(no->esquerdo, valor);  
        }

        return buscarRecursivo(no->direito, valor); 
    }

    // Função recursiva para liberar memória da árvore
    void liberarMemoria(No* no) {
        if (no != nullptr) {
            liberarMemoria(no->esquerdo);
            liberarMemoria(no->direito);
            delete no;
        }
    }

public:
    // Construtor que inicializa a raiz como nullptr
    ArvoreBinaria() {
        raiz = nullptr;
    }

    // Função pública para inserir um valor
    void inserir(int valor) {
        raiz = inserirRecursivo(raiz, valor);
    }

    // Função pública para buscar um valor
    bool buscar(int valor) {
        return buscarRecursivo(raiz, valor) != nullptr;
    }

    // Função pública para exibir os valores em ordem
    void emOrdem() {
        emOrdemRecursivo(raiz);
        cout << endl;
    }

    // Destrutor que libera a memória da árvore
    ~ArvoreBinaria() {
        liberarMemoria(raiz);
    }
};

int main() {
    ArvoreBinaria arvore;

    arvore.inserir(50);
    arvore.inserir(30);
    arvore.inserir(70);
    arvore.inserir(20);
    arvore.inserir(40);
    arvore.inserir(60);
    arvore.inserir(80);

  
    cout << "Elementos da arvore em ordem: ";
    arvore.emOrdem();  

    // Busca de valores
    cout << "Buscar 40: " << (arvore.buscar(40) ? "Encontrado" : "Não encontrado") << endl;  
    cout << "Buscar 25: " << (arvore.buscar(25) ? "Encontrado" : "Não encontrado") << endl;  
    return 0;
}
