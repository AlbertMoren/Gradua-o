#include <iostream>
#include <vector>
using namespace std;

class Fila {
private:
    vector<int> fila;

public:
    // Adiciona um elemento ao final da fila
    void enfileirar(int valor) {
        fila.push_back(valor);
    }

    // Remove o primeiro elemento da fila
    void desenfileirar() {
        if (!estaVazia()) {
            fila.erase(fila.begin()); 
        } else {
            cout << "A fila está vazia!" << endl;
        }
    }

    // Retorna o primeiro elemento da fila
    int frente() {
        if (!estaVazia()) {
            return fila.front();
        } else {
            cout << "A fila está vazia!" << endl;
            return -1; 
        }
    }

    // Verifica se a fila está vazia
    bool estaVazia() {
        return fila.empty();
    }

    // Retorna o tamanho da fila
    int tamanho() {
        return fila.size();
    }
};

int main() {
    Fila minhaFila;
    cout<<"Adcionando 10,20 e 30 para fila"<<endl;
    minhaFila.enfileirar(10);
    minhaFila.enfileirar(20);
    minhaFila.enfileirar(30);
    cout << "Frente da fila: " << minhaFila.frente() << endl;  
    minhaFila.desenfileirar();
    cout << "Frente da fila após desenfileirar: " << minhaFila.frente() << endl;
    cout << "Tamanho da fila: " << minhaFila.tamanho() << endl;  
    minhaFila.desenfileirar();
    minhaFila.desenfileirar();
    minhaFila.desenfileirar();  

    return 0;
}
