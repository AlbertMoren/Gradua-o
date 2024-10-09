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

class PilhaEncadeada {
private:
    Node* topoPilha;  
    int tam;          

public:
    // Construtor
    PilhaEncadeada() {
        topoPilha = nullptr;
        tam = 0;
    }

    // Verifica se a pilha está vazia
    bool estaVazia() {
        return topoPilha == nullptr;
    }

    // Retorna o tamanho da pilha
    int tamanho() {
        return tam;
    }

    // Adiciona um elemento ao topo da pilha
    void empilhar(int valor) {
        Node* novoNo = new Node(valor);
        novoNo->prox = topoPilha;  
        topoPilha = novoNo;        
        tam++;
    }

    // Remove o elemento do topo da pilha
    void desempilhar() {
        if (estaVazia()) {
            cout << "A pilha está vazia!" << endl;
        } else {
            Node* temp = topoPilha;
            topoPilha = topoPilha->prox;  
            delete temp;                 
            tam--;
        }
    }

    // Retorna o valor do topo da pilha
    int topo() {
        if (!estaVazia()) {
            return topoPilha->dado;
        } else {
            cout << "A pilha está vazia!" << endl;
            return -1; 
        }
    }

    // Exibe a pilha
    void exibirPilha() {
        if (estaVazia()) {
            cout << "A pilha está vazia!" << endl;
        } else {
            Node* temp = topoPilha;
            while (temp != nullptr) {
                cout << temp->dado << " -> ";
                temp = temp->prox;
            }
            cout << "NULL" << endl;
        }
    }
};

int main() {
    PilhaEncadeada pilha;

    pilha.empilhar(10);
    pilha.empilhar(20);
    pilha.empilhar(30);
    pilha.exibirPilha();  
    cout << "Topo da pilha: " << pilha.topo() << endl; 
    pilha.desempilhar();
    pilha.exibirPilha();  
    pilha.desempilhar();
    pilha.desempilhar();
    pilha.desempilhar();  
    cout << "Tamanho da pilha: " << pilha.tamanho() << endl;  

    return 0;
}
