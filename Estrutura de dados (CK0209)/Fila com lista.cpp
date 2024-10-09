#include <iostream>

using namespace std;

// Definição de um nó da lista encadeada
struct Node {
    int dado;
    Node* prox;
    
    Node(int valor) {
        dado = valor;
        prox = nullptr;
    }
};

class FilaEncadeada {
private:
    Node* frente; 
    Node* fim;     
    int tam;       

public:
    // Construtor
    FilaEncadeada() {
        frente = nullptr;
        fim = nullptr;
        tam = 0;
    }

    // Verifica se a fila está vazia
    bool estaVazia() {
        return frente == nullptr;
    }

    // Retorna o tamanho da fila
    int tamanho() {
        return tam;
    }

    // Adiciona um elemento ao final da fila
    void enfileirar(int valor) {
        Node* novoNo = new Node(valor);
        if (estaVazia()) {
            frente = novoNo;
            fim = novoNo;
        } else {
            fim->prox = novoNo;
            fim = novoNo;
        }
        tam++;
    }

    // Remove o elemento do início da fila
    void desenfileirar() {
        if (estaVazia()) {
            cout << "A fila está vazia!" << endl;
        } else {
            Node* temp = frente;
            frente = frente->prox;
            delete temp;
            tam--;
            
            // Se a fila ficar vazia após a remoção
            if (frente == nullptr) {
                fim = nullptr;
            }
        }
    }

    // Retorna o valor do primeiro elemento da fila
    int frenteFila() {
        if (!estaVazia()) {
            return frente->dado;
        } else {
            cout << "A fila está vazia!" << endl;
            return -1; 
        }
    }

    // Exibe a fila
    void exibirFila() {
        if (estaVazia()) {
            cout << "A fila está vazia!" << endl;
        } else {
            Node* temp = frente;
            while (temp != nullptr) {
                cout << temp->dado << " -> ";
                temp = temp->prox;
            }
            cout << "NULL" << endl;
        }
    }
};

int main() {
    FilaEncadeada fila;

    fila.enfileirar(10);
    fila.enfileirar(20);
    fila.enfileirar(30);
    fila.exibirFila();  /

    cout << "Frente da fila: " << fila.frenteFila() << endl;  

    fila.desenfileirar();
    fila.exibirFila();  

    fila.desenfileirar();
    fila.desenfileirar();
    fila.desenfileirar();  

    cout << "Tamanho da fila: " << fila.tamanho() << endl;  

    return 0;
}
