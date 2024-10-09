#include <iostream>
#include <vector>

using namespace std;

class Pilha {
private:
    vector<int> pilha;

public:
    // Adiciona um elemento ao topo da pilha
    void empilhar(int valor) {
        pilha.push_back(valor);
    }

    // Remove o elemento do topo da pilha
    void desempilhar() {
        if (!estaVazia()) {
            pilha.pop_back();
        } else {
            cout << "A pilha está vazia!" << endl;
        }
    }

    // Retorna o elemento do topo da pilha
    int topo() {
        if (!estaVazia()) {
            return pilha.back();
        } else {
            cout << "A pilha está vazia!" << endl;
            return -1; 
    }

    // Verifica se a pilha está vazia
    bool estaVazia() {
        return pilha.empty();
    }

    // Retorna o tamanho da pilha
    int tamanho() {
        return pilha.size();
    }
};

int main() {
    Pilha minhaPilha;

    minhaPilha.empilhar(10);
    minhaPilha.empilhar(20);
    minhaPilha.empilhar(30);

    cout << "Topo da pilha: " << minhaPilha.topo() << endl;  
    minhaPilha.desempilhar();
    cout << "Topo da pilha após desempilhar: " << minhaPilha.topo() << endl;  
    cout << "Tamanho da pilha: " << minhaPilha.tamanho() << endl;  
    minhaPilha.desempilhar();
    minhaPilha.desempilhar();
    minhaPilha.desempilhar();  

    return 0;
}
