#include <iostream>
#include <vector>

using namespace std;

class MinHeap {
private:
    vector<int> heap;  

    // Retorna o índice do pai
    int pai(int i) {
        return (i - 1) / 2;
    }

    // Retorna o índice do filho à esquerda
    int filhoEsquerda(int i) {
        return 2 * i + 1;
    }

    // Retorna o índice do filho à direita
    int filhoDireita(int i) {
        return 2 * i + 2;
    }

    // Função para reorganizar a heap após inserção (Heapify para cima)
    void heapifyCima(int i) {
        while (i != 0 && heap[pai(i)] > heap[i]) {
            swap(heap[i], heap[pai(i)]);
            i = pai(i);
        }
    }

    // Função para reorganizar a heap após remoção (Heapify para baixo)
    void heapifyBaixo(int i) {
        int menor = i;
        int esquerda = filhoEsquerda(i);
        int direita = filhoDireita(i);
       
        if (esquerda < tamanho() && heap[esquerda] < heap[menor]) {
            menor = esquerda;
        }

        if (direita < tamanho() && heap[direita] < heap[menor]) {
            menor = direita;
        }

        if (menor != i) {
            swap(heap[i], heap[menor]);
            heapifyBaixo(menor);
        }
    }

public:
    // Retorna o tamanho da heap
    int tamanho() {
        return heap.size();
    }

    // Verifica se a heap está vazia
    bool estaVazia() {
        return tamanho() == 0;
    }

    // Insere um novo elemento na heap
    void inserir(int valor) {
        heap.push_back(valor);
        int index = tamanho() - 1;
        heapifyCima(index);
    }

    // Retorna o valor mínimo (raiz) da heap
    int obterMinimo() {
        if (estaVazia()) {
            throw out_of_range("A heap está vazia.");
        }
        return heap[0];
    }

    // Remove e retorna o valor mínimo (raiz) da heap
    int extrairMinimo() {
        if (estaVazia()) {
            throw out_of_range("A heap está vazia.");
        }

        int minimo = heap[0];
        heap[0] = heap.back();  
        heap.pop_back();        
        heapifyBaixo(0);        

        return minimo;
    }

    // Exibe os elementos da heap
    void exibirHeap() {
        for (int i : heap) {
            cout << i << " ";
        }
        cout << endl;
    }
};

int main() {
    MinHeap heap;

    heap.inserir(40);
    heap.inserir(20);
    heap.inserir(30);
    heap.inserir(5);
    heap.inserir(10);
    cout << "Heap atual: ";
    heap.exibirHeap();  
    cout << "Mínimo: " << heap.obterMinimo() << endl;  
    cout << "Extrair mínimo: " << heap.extrairMinimo() << endl;  
    cout << "Heap após extração: ";
    heap.exibirHeap();  
    cout << "Extrair mínimo: " << heap.extrairMinimo() << endl;  
    cout << "Heap após extração: ";
    heap.exibirHeap();  

    return 0;
}
