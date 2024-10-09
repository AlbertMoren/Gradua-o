#include <iostream>

using namespace std;

// Definição de um nó da lista duplamente encadeada
struct Node {
    int dado;
    Node* prox;
    Node* ant;

    Node(int valor) {
        dado = valor;
        prox = nullptr;
        ant = nullptr;
    }
};

class ListaDuplamenteEncadeada {
private:
    Node* head;  
    Node* tail;  
    int tam;     

public:
    // Construtor
    ListaDuplamenteEncadeada() {
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
        } else {
            novoNo->prox = head;
            head->ant = novoNo;
            head = novoNo;
        }
        tam++;
    }

    // Insere um elemento no fim da lista
    void inserirFim(int valor) {
        Node* novoNo = new Node(valor);
        if (estaVazia()) {
            head = novoNo;
            tail = novoNo;
        } else {
            tail->prox = novoNo;
            novoNo->ant = tail;
            tail = novoNo;
        }
        tam++;
    }

    // Remove o primeiro elemento da lista
    void removerInicio() {
        if (estaVazia()) {
            cout << "A lista está vazia!" << endl;
        } else {
            Node* temp = head;
            if (head == tail) {
                head = nullptr;
                tail = nullptr;
            } else {
                head = head->prox;
                head->ant = nullptr;
            }
            delete temp;
            tam--;
        }
    }

    // Remove o último elemento da lista
    void removerFim() {
        if (estaVazia()) {
            cout << "A lista está vazia!" << endl;
        } else {
            Node* temp = tail;
            if (head == tail) {
                head = nullptr;
                tail = nullptr;
            } else {
                tail = tail->ant;
                tail->prox = nullptr;
            }
            delete temp;
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

    // Exibe a lista da frente para trás
    void exibirLista() {
        if (estaVazia()) {
            cout << "A lista está vazia!" << endl;
        } else {
            Node* temp = head;
            while (temp != nullptr) {
                cout << temp->dado << " <-> ";
                temp = temp->prox;
            }
            cout << "NULL" << endl;
        }
    }

    // Exibe a lista de trás para frente
    void exibirListaReversa() {
        if (estaVazia()) {
            cout << "A lista está vazia!" << endl;
        } else {
            Node* temp = tail;
            while (temp != nullptr) {
                cout << temp->dado << " <-> ";
                temp = temp->ant;
            }
            cout << "NULL" << endl;
        }
    }
};

int main() {
    ListaDuplamenteEncadeada lista;

    lista.inserirInicio(10);
    lista.inserirFim(20);
    lista.inserirInicio(5);
    lista.inserirFim(30);

    cout << "Lista (da frente para trás): ";
    lista.exibirLista(); 

    cout << "Lista (de trás para frente): ";
    lista.exibirListaReversa();  

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
