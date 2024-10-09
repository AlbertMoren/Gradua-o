#include <iostream>

using namespace std;

// Definição de um nó da lista simplesmente encadeada
struct Node {
    int dado;
    Node* prox;
    
    Node(int valor) {
        dado = valor;
        prox = nullptr;
    }
};

class ListaSimplesmenteEncadeada {
private:
    Node* head;  
    int tam;     

public:
    // Construtor
    ListaSimplesmenteEncadeada() {
        head = nullptr;
        tam = 0;
    }

    // Verifica se a lista está vazia
    bool estaVazia() {
        return head == nullptr;
    }

    // Retorna o tamanho da lista
    int tamanho() {
        return tam;
    }

    // Insere um elemento no início da lista
    void inserirInicio(int valor) {
        Node* novoNo = new Node(valor);
        novoNo->prox = head;
        head = novoNo;
        tam++;
    }

    // Insere um elemento no fim da lista
    void inserirFim(int valor) {
        Node* novoNo = new Node(valor);
        if (estaVazia()) {
            head = novoNo;
        } else {
            Node* temp = head;
            while (temp->prox != nullptr) {
                temp = temp->prox;
            }
            temp->prox = novoNo;
        }
        tam++;
    }

    // Remove o primeiro elemento da lista
    void removerInicio() {
        if (!estaVazia()) {
            Node* temp = head;
            head = head->prox;
            delete temp;
            tam--;
        } else {
            cout << "A lista está vazia!" << endl;
        }
    }

    // Remove o último elemento da lista
    void removerFim() {
        if (estaVazia()) {
            cout << "A lista está vazia!" << endl;
        } else if (head->prox == nullptr) {
            delete head;
            head = nullptr;
            tam--;
        } else {
            Node* temp = head;
            while (temp->prox->prox != nullptr) {
                temp = temp->prox;
            }
            delete temp->prox;
            temp->prox = nullptr;
            tam--;
        }
    }

    // Busca um valor na lista
    bool buscar(int valor) {
        Node* temp = head;
        while (temp != nullptr) {
            if (temp->dado == valor) {
                return true;
            }
            temp = temp->prox;
        }
        return false;
    }

    // Exibe a lista
    void exibirLista() {
        if (estaVazia()) {
            cout << "A lista está vazia!" << endl;
        } else {
            Node* temp = head;
            while (temp != nullptr) {
                cout << temp->dado << " -> ";
                temp = temp->prox;
            }
            cout << "NULL" << endl;
        }
    }
};

int main() {
    ListaSimplesmenteEncadeada lista;

    lista.inserirInicio(10);
    lista.inserirFim(20);
    lista.inserirInicio(5);
    lista.inserirFim(30);
    lista.exibirLista();  

    lista.removerInicio();
    lista.exibirLista(); 

    lista.removerFim();
    lista.exibirLista();  

    cout << "Tamanho da lista: " << lista.tamanho() << endl;  

    if (lista.buscar(20)) {
        cout << "Valor 20 encontrado na lista." << endl;
    } else {
        cout << "Valor 20 não encontrado na lista." << endl;
    }

    lista.removerFim();
    lista.removerFim();
    lista.exibirLista();  
    
    return 0;
}
