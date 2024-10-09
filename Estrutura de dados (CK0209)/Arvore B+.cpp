#include <iostream>
#include <vector>

using namespace std;

class NoBPlus {
public:
    vector<int> chaves; 
    vector<NoBPlus*> filhos; 
    bool folha; 
    NoBPlus* proximo; 

    NoBPlus(bool isFolha) : folha(isFolha), proximo(nullptr) {}
};

// Classe que implementa a Árvore B+
class ArvoreBPlus {
private:
    NoBPlus* raiz; 
    int grau; 

    // Função para dividir um filho de um nó
    void dividirFilho(NoBPlus* pai, int indice, NoBPlus* filho) {
        NoBPlus* novoNo = new NoBPlus(filho->folha);
        novoNo->chaves.resize(grau - 1);

        for (int i = 0; i < grau - 1; i++)
            novoNo->chaves[i] = filho->chaves[i + grau];

        if (!filho->folha) {
            novoNo->filhos.resize(grau);
            for (int i = 0; i < grau; i++)
                novoNo->filhos[i] = filho->filhos[i + grau];
        }

        filho->chaves.resize(grau - 1);

        pai->filhos.insert(pai->filhos.begin() + indice + 1, novoNo);
        pai->chaves.insert(pai->chaves.begin() + indice, filho->chaves[grau - 1]);
    }

    // Função para inserir uma chave na árvore B+
    void inserirChave(NoBPlus* no, int chave) {
        int i = no->chaves.size() - 1;

        if (no->folha) {
            while (i >= 0 && chave < no->chaves[i]) {
                no->chaves.push_back(no->chaves[i]); 
                i--;
            }
            no->chaves.push_back(0);
            no->chaves[i + 1] = chave;
        } else {
            while (i >= 0 && chave < no->chaves[i])
                i--;

            if (no->filhos[i + 1]->chaves.size() == grau - 1) {
                dividirFilho(no, i + 1, no->filhos[i + 1]);

                if (chave > no->chaves[i + 1])
                    i++;
            }
            inserirChave(no->filhos[i + 1], chave);
        }
    }

public:
    ArvoreBPlus(int t) : raiz(nullptr), grau(t) {}

    // Função para inserir uma nova chave na árvore B+
    void inserir(int chave) {
        if (raiz == nullptr) {
            raiz = new NoBPlus(true);
            raiz->chaves.push_back(chave);
        } else {
            if (raiz->chaves.size() == grau - 1) {
                NoBPlus* novoNo = new NoBPlus(false);
                novoNo->filhos.push_back(raiz);
                dividirFilho(novoNo, 0, raiz);
                int i = 0;

                if (novoNo->chaves[0] < chave)
                    i++;
                inserirChave(novoNo->filhos[i], chave);
                raiz = novoNo; 
            } else {
                inserirChave(raiz, chave);
            }
        }
    }

    // Função para exibir as chaves da árvore B+
    void emOrdem(NoBPlus* no) {
        if (no != nullptr) {
            for (int i = 0; i < no->chaves.size(); i++) {
                emOrdem(no->filhos[i]); 
                cout << no->chaves[i] << " "; 
            }
            emOrdem(no->filhos[no->chaves.size()]); 
        }
    }

    // Função pública para exibir a árvore
    void exibir() {
        emOrdem(raiz);
        cout << endl;
    }

    // Função para exibir as folhas da árvore
    void exibirFolhas() {
        NoBPlus* atual = raiz;
        while (atual && !atual->folha)
            atual = atual->filhos[0]; 

        // Percorre as folhas
        while (atual) {
            for (int chave : atual->chaves)
                cout << chave << " ";
            atual = atual->proximo; 
        }
        cout << endl;
    }
};

int main() {
    ArvoreBPlus arvore(3); 

    arvore.inserir(10);
    arvore.inserir(20);
    arvore.inserir(5);
    arvore.inserir(6);
    arvore.inserir(12);
    arvore.inserir(30);
    arvore.inserir(15);

    cout << "Elementos da árvore B+ em ordem: ";
    arvore.exibir(); 

    cout << "Elementos da árvore B+ nas folhas: ";
    arvore.exibirFolhas(); 

    return 0;
}
