#include <iostream>

using namespace std;

// Definição da estrutura de um nó da árvore AVL
struct No {
    int valor;
    No* esquerdo;
    No* direito;
    int altura;

    // Construtor para criar um nó com um valor
    No(int v) {
        valor = v;
        esquerdo = nullptr;
        direito = nullptr;
        altura = 1;  // Altura inicial de um nó folha
    }
};

// Função para obter a altura de um nó
int altura(No* no) {
    if (no == nullptr)
        return 0;
    return no->altura;
}

// Função para calcular o fator de balanceamento de um nó
int fatorBalanceamento(No* no) {
    if (no == nullptr)
        return 0;
    return altura(no->esquerdo) - altura(no->direito);
}

// Função para rotacionar à direita
No* rotacaoDireita(No* y) {
    No* x = y->esquerdo;
    No* T2 = x->direito;

    x->direito = y;
    y->esquerdo = T2;

    y->altura = max(altura(y->esquerdo), altura(y->direito)) + 1;
    x->altura = max(altura(x->esquerdo), altura(x->direito)) + 1;

    return x;
}

// Função para rotacionar à esquerda
No* rotacaoEsquerda(No* x) {
    No* y = x->direito;
    No* T2 = y->esquerdo;

    y->esquerdo = x;
    x->direito = T2;

    x->altura = max(altura(x->esquerdo), altura(x->direito)) + 1;
    y->altura = max(altura(y->esquerdo), altura(y->direito)) + 1;

 
    return y;
}

// Função para inserir um novo valor na árvore AVL
No* inserir(No* no, int valor) {
    if (no == nullptr)
        return new No(valor);

    if (valor < no->valor)
        no->esquerdo = inserir(no->esquerdo, valor);
    else if (valor > no->valor)
        no->direito = inserir(no->direito, valor);
    else
        return no;  

    no->altura = max(altura(no->esquerdo), altura(no->direito)) + 1;

   
    int balance = fatorBalanceamento(no);

    // Caso 1: Rotação à direita (LL)
    if (balance > 1 && valor < no->esquerdo->valor)
        return rotacaoDireita(no);

    // Caso 2: Rotação à esquerda (RR)
    if (balance < -1 && valor > no->direito->valor)
        return rotacaoEsquerda(no);

    // Caso 3: Rotação dupla à direita (LR)
    if (balance > 1 && valor > no->esquerdo->valor) {
        no->esquerdo = rotacaoEsquerda(no->esquerdo);
        return rotacaoDireita(no);
    }

    // Caso 4: Rotação dupla à esquerda (RL)
    if (balance < -1 && valor < no->direito->valor) {
        no->direito = rotacaoDireita(no->direito);
        return rotacaoEsquerda(no);
    }

    return no;
}

// Função para percorrer a árvore em ordem (in-order traversal)
void emOrdem(No* raiz) {
    if (raiz != nullptr) {
        emOrdem(raiz->esquerdo);
        cout << raiz->valor << " ";
        emOrdem(raiz->direito);
    }
}

// Função para liberar a memória da árvore
void liberarMemoria(No* no) {
    if (no != nullptr) {
        liberarMemoria(no->esquerdo);
        liberarMemoria(no->direito);
        delete no;
    }
}

int main() {
    No* raiz = nullptr;

    raiz = inserir(raiz, 10);
    raiz = inserir(raiz, 20);
    raiz = inserir(raiz, 30);
    raiz = inserir(raiz, 40);
    raiz = inserir(raiz, 50);
    raiz = inserir(raiz, 25);

    cout << "Elementos da arvore AVL em ordem: ";
    emOrdem(raiz);  
    cout << endl;

    liberarMemoria(raiz);

    return 0;
}
