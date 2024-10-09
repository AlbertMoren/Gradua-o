#include <iostream>

using namespace std;

enum Cor { VERMELHO, PRETO };

// Definição da estrutura de um nó da árvore rubro-negra
struct No {
    int valor;
    Cor cor;
    No *esquerdo, *direito, *pai;

    // Construtor para criar um nó com um valor
    No(int v) {
        valor = v;
        esquerdo = direito = pai = nullptr;
        cor = VERMELHO;  
    }
};

class ArvoreRubroNegra {
private:
    No* raiz;

    // Função para realizar uma rotação à esquerda
    void rotacaoEsquerda(No* &raiz, No* &x) {
        No* y = x->direito;
        x->direito = y->esquerdo;

        if (y->esquerdo != nullptr)
            y->esquerdo->pai = x;

        y->pai = x->pai;

        if (x->pai == nullptr)
            raiz = y;
        else if (x == x->pai->esquerdo)
            x->pai->esquerdo = y;
        else
            x->pai->direito = y;

        y->esquerdo = x;
        x->pai = y;
    }

    // Função para realizar uma rotação à direita
    void rotacaoDireita(No* &raiz, No* &x) {
        No* y = x->esquerdo;
        x->esquerdo = y->direito;

        if (y->direito != nullptr)
            y->direito->pai = x;

        y->pai = x->pai;

        if (x->pai == nullptr)
            raiz = y;
        else if (x == x->pai->direito)
            x->pai->direito = y;
        else
            x->pai->esquerdo = y;

        y->direito = x;
        x->pai = y;
    }

    // Função para corrigir violações após a inserção
    void corrigirInsercao(No* &raiz, No* &z) {
        while (z != raiz && z->pai->cor == VERMELHO) {
            if (z->pai == z->pai->pai->esquerdo) {
                No* tio = z->pai->pai->direito;

                if (tio != nullptr && tio->cor == VERMELHO) {
                    z->pai->cor = PRETO;
                    tio->cor = PRETO;
                    z->pai->pai->cor = VERMELHO;
                    z = z->pai->pai;
                } else {
                    if (z == z->pai->direito) {
                        z = z->pai;
                        rotacaoEsquerda(raiz, z);
                    }

                    z->pai->cor = PRETO;
                    z->pai->pai->cor = VERMELHO;
                    rotacaoDireita(raiz, z->pai->pai);
                }
            } else {
                No* tio = z->pai->pai->esquerdo;


                if (tio != nullptr && tio->cor == VERMELHO) {
                    z->pai->cor = PRETO;
                    tio->cor = PRETO;
                    z->pai->pai->cor = VERMELHO;
                    z = z->pai->pai;
                } else {
                    if (z == z->pai->esquerdo) {
                        z = z->pai;
                        rotacaoDireita(raiz, z);
                    }

                    z->pai->cor = PRETO;
                    z->pai->pai->cor = VERMELHO;
                    rotacaoEsquerda(raiz, z->pai->pai);
                }
            }
        }

        raiz->cor = PRETO;
    }

public:
    // Construtor que inicializa a árvore com a raiz nula
    ArvoreRubroNegra() {
        raiz = nullptr;
    }

    // Função para inserir um novo valor na árvore rubro-negra
    void inserir(int valor) {
        No* novoNo = new No(valor);

        No* y = nullptr;
        No* x = raiz;

        // Realiza a inserção normal de árvore binária de busca
        while (x != nullptr) {
            y = x;
            if (novoNo->valor < x->valor)
                x = x->esquerdo;
            else
                x = x->direito;
        }

        novoNo->pai = y;

        if (y == nullptr)
            raiz = novoNo;
        else if (novoNo->valor < y->valor)
            y->esquerdo = novoNo;
        else
            y->direito = novoNo;

        corrigirInsercao(raiz, novoNo);
    }

    // Função para exibir os elementos da árvore em ordem
    void emOrdem(No* raiz) {
        if (raiz != nullptr) {
            emOrdem(raiz->esquerdo);
            cout << raiz->valor << " ";
            emOrdem(raiz->direito);
        }
    }

    // Função pública para chamar o percurso em ordem
    void exibir() {
        emOrdem(raiz);
        cout << endl;
    }
};

int main() {
    ArvoreRubroNegra arvore;

    arvore.inserir(7);
    arvore.inserir(3);
    arvore.inserir(18);
    arvore.inserir(10);
    arvore.inserir(22);
    arvore.inserir(8);
    arvore.inserir(11);
    arvore.inserir(26);

    cout << "Elementos da árvore rubro-negra em ordem: ";
    arvore.exibir();  

    return 0;
}
