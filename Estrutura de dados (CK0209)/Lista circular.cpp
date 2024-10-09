#include <iostream>

using namespace std;

// Definição de um nó da lista circular simplesmente encadeada
struct Node {
    int dado;
    Node* prox;

    Node(int valor) {
        dado = valor;
        prox = nullptr;
    }
};

class ListaCircular {
private:
    Node* head;  
    Node* tail;  
    int tam;     

public:
    // Construtor
    ListaCircular() {
        head = nullptr;
        tail = nullptr;
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
        if (estaVazia()) {
            head = novoNo;
            tail = novoNo;
            tail->prox = head;  
        } else {
            novoNo->prox = head;
            head = novoNo;
            tail->prox = head;  
        }
        tam++;
    }

    // Insere um elemento no fim da lista
    void inserirFim(int valor) {
        Node* novoNo = new Node(valor);
        if (estaVazia()) {
            head = novoNo;
            tail = novoNo;
            tail->prox = head;  
        } else {
            tail->prox = novoNo;
            tail = novoNo;
            tail->prox = head;  
        }
        tam++;
    }

    // Remove o primeiro elemento da lista
    void removerInicio() {
        if (estaVazia()) {
            cout << "A lista está vazia!" << endl;
        } else if (head == tail) {  
            delete head;
            head = nullptr;
            tail = nullptr;
            tam--;
        } else {
            Node* temp = head;
            head = head->prox;
            tail->prox = head;  
            delete temp;
            tam--;
        }
    }

    // Remove o último elemento da lista
    void removerFim() {
        if (estaVazia()) {
            cout << "A lista está vazia!" << endl;
        } else if (head == tail) {  
            delete tail;
            head = nullptr;
            tail = nullptr;
            tam--;
        } else {
            Node* temp = head;
            while (temp->prox != tail) {  
                temp = temp->prox;
            }
            temp->prox = head;  // Mantém a circularidade
            delete tail;
            tail = temp;
            tam--;
        }
    }

    // Busca um valor na lista
    bool buscar(int valor) {
        if (estaVazia()) {
            return false;
        }
        Node* temp = head;
        do {
            if (temp->dado == valor) {
                return true;
            }
            temp = temp->prox;
        } while (temp != head);  
        return false;
    }

    // Exibe a lista
    void exibirLista() {
        if (estaVazia()) {
            cout << "A lista está vazia!" << endl;
        } else {
            Node* temp = head;
            do {
                cout << temp->dado << " -> ";
                temp = temp->prox;
            } while (temp != head);
            cout << "(circular: volta ao início)" << endl;
        }
    }
};

int main() {
    ListaCircular lista;

    lista.inserirInicio(10);
    lista.inserirFim(20);
    lista.inserirInicio(5);
    lista.inserirFim(30);

    cout << "Lista: ";
    lista.exibirLista();  

    lista.removerInicio();
    lista.exibirLista();  

    lista.removerFim();
    lista.exibirLista();  

    if (lista.buscar(20)) {
        cout << "Valor 20 encontrado na lista." << endl;
    } else {
        cout << "Valor 20 não encontrado na lista." << endl;
    }

    lista.removerFim();
    lista.removerFim();
    lista.exibirLista();  

    cout << "Tamanho da lista: " << lista.tamanho() << endl;  

    return 0;
}
