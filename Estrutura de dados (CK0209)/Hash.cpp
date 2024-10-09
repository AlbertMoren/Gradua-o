#include <iostream>
#include <list>
#include <vector>
using namespace std;

// Classe que implementa a tabela hash
class TabelaHash {
private:
    vector<list<int>> tabela; 
    int capacidade;           

    // Função de hash para calcular o índice
    int funcaoHash(int chave) {
        return chave % capacidade; 
    }

public:
    // Construtor que inicializa a tabela hash com uma capacidade
    TabelaHash(int tamanho) {
        capacidade = tamanho;
        tabela.resize(tamanho); 
    }

    // Função para inserir uma chave na tabela hash
    void inserir(int chave) {
        int indice = funcaoHash(chave); 
        tabela[indice].push_back(chave); 
    }

    // Função para remover uma chave da tabela hash
    void remover(int chave) {
        int indice = funcaoHash(chave); 
        tabela[indice].remove(chave);   
    }

    // Função para buscar uma chave na tabela hash
    bool buscar(int chave) {
        int indice = funcaoHash(chave); 
        for (int elemento : tabela[indice]) {
            if (elemento == chave)
                return true;
        }
        return false; 
    }

    // Função para exibir o conteúdo da tabela hash
    void exibir() {
        for (int i = 0; i < capacidade; i++) {
            cout << "Bucket " << i << ": ";
            for (int chave : tabela[i]) {
                cout << chave << " ";
            }
            cout << endl;
        }
    }
};

int main() {
    TabelaHash hash(7); 

    hash.inserir(10);
    hash.inserir(20);
    hash.inserir(15);
    hash.inserir(7);
    hash.inserir(30);

    cout << "Tabela Hash:" << endl;
    hash.exibir();

    cout << "Busca por 15: " << (hash.buscar(15) ? "Encontrado" : "Não encontrado") << endl;
    cout << "Busca por 50: " << (hash.buscar(50) ? "Encontrado" : "Não encontrado") << endl;

    hash.remover(15);
    cout << "Tabela Hash após remover 15:" << endl;
    hash.exibir();

    return 0;
}
