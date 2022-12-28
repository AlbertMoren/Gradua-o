#include "ABB.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct node {
  int chave;
  char conteudo;
  No *esq;
  No *dir;
  No *pai;
};

/* Aloca e retorna um No com os dados passados por parâmetro. Retorna no nó
 * criado ou NULL caso não seja posivel criar o nó. */
No *abb_cria_no(int chave, char conteudo) {
  if(chave < 0){
    return NULL;
  }
  No *p = (No*)malloc(sizeof(No));
  p->chave = chave;
  p->conteudo = conteudo;
  p->dir = NULL;
  p->esq = NULL;
  p->pai = NULL;
  return p;
}

/* Libera a memória de um nó e toda as suas sub-árvores. Retorna 1 se for
 * possivel fazer a liberação ou 0 caso o nó seja NULL. */
int abb_libera_no(No *no) {
  if (no == NULL) {
    return 0;
  }

  No *proxEsq = no->esq;
  No *proxDir = no->dir;
  free(no);  
  if (proxEsq != NULL) {
    abb_libera_no(proxEsq);
  }
  if (proxDir != NULL){
    abb_libera_no(proxDir);
  }

  return 1;
}

/* Retorna a chave do nó ou -1 caso o nó seja NULL.  */
int abb_chave_no(No *no) {
  if(no == NULL){
    return -1;
  }
  return no->chave;
}

/* Retorna o conteúdo do no ou '#' caso o nó seja NULL. */
char abb_conteudo_no(No *no) {
  if(no == NULL){
    return '#';
  }
  return no->conteudo;
}

/* Adiciona um nó à esquerda ou à direita do no raiz. Retorna a raiz da árvore
 * resultante ou NULL caso (i) a raiz e o nó sejam NULL e (ii) caso o nó possua
 * mesma chave que outro nó previamente inserido na árvore. */
No *abb_insere_no(No *raiz, No *no) {
  if (raiz == NULL && no == NULL) {
    return NULL;
  }
  No *aux1 = NULL;
  No *aux2 = raiz;

  while (aux2 != NULL) {
    aux1 = aux2;
    if (no->chave < aux2->chave) {
      aux2 = aux2->esq;
    }
    else if (no->chave > aux2->chave) {
      aux2 = aux2->dir;
    }
    else if (no->chave == aux1->chave){
      return NULL;
    }
  }
  if (raiz != NULL) {
    if (no->chave < aux1->chave) {
      aux1->esq = no;
    }
    else {
      aux1->dir = no;
    }

    no->pai = aux1;
  }
  else {
    raiz = no;
  }
  return raiz;
}

/* Procura o nó pela chave. Retorna o nó caso a busca obtenha sucesso ou NULL
 * em caso contrário. */
No *abb_busca_no(No *raiz, int chave) {
  No *aux = raiz;
  while (aux != NULL && aux->chave != chave) {
    if (aux->chave > chave) {
      aux = aux->esq;
    }
    else if (aux->chave < chave) {
      aux = aux->dir;
    }
  }
  return aux;
}


/* Remove o nó com a chave fornecida. Retorna a raiz da arvore atualizada ou
 * NULL em caso a raiz fornecida seja NULL. */
No *abb_remove_no(No *raiz, int chave) {
  if (raiz == NULL) {
    return NULL;
  }
  No *aux = raiz;
  while (aux != NULL && aux->chave != chave) {
    if (aux->chave > chave) {
      aux = aux->esq;
    }
    else if (aux->chave < chave) {
      aux = aux->dir;
    }
  }
  No *aux2;
  if (aux->esq->chave == chave) {
    aux2 = aux->esq;
    aux->esq = NULL;
  }
  else if (aux->dir->chave == chave) {
    aux2 = aux->dir;
    aux->dir = NULL;
  }
  return aux2;
}

/* Retorna a altura da árvore ou -1 caso araiz seja NULL. */
int abb_altura(No *raiz) {
  if (raiz == NULL) {
    return -1;
  }

  int alturaEsq = abb_altura(raiz->esq);
  int alturaDir = abb_altura(raiz->dir);

  if (alturaEsq < alturaDir) {
    return alturaDir + 1;
  }
  else {
    return alturaEsq + 1;
  }
}

/* Retorna o número de nós da árvore ou -1 caso araiz seja NULL. */
int abb_numero(No *raiz) {
  if (raiz == NULL) {
    return -1;
  }
  int quantidade = 0;

  No *aux = raiz;

  if (aux->esq != NULL) {
    aux = minimo(aux->esq);
    quantidade += 1;
  }
  while (sucessor(aux) != NULL) {
    aux = sucessor(aux);
    quantidade += 1;
  }
  return quantidade;
}

/*Retorna a concatenação do conteúdo da árvore fazendo percurso em pré-ordem à
 * partir do nó ou '#' caso o nó seja NULL. */
char *abb_pre_ordem(No *no) {
  if (no == NULL) {
      return "#";
  }
  char *concatenacao;

  return preOrdem(no, concatenacao);
}

/*Retorna a concatenação do conteúdo da árvore fazendo percurso em ordem à
 * partir do nó ou '#' caso o nó seja NULL. */
char *abb_ordem(No *no) {
  if (no == NULL) {
      return "#";
  }
  char *concatenacao;
  
  if (no->esq != NULL) {
    no = minimo(no->esq);
    strcat(concatenacao, &no->conteudo);
  }
  while (sucessor(no) != NULL) {
    no = sucessor(no);
    strcat(concatenacao, &no->conteudo);
  }
  return concatenacao;
}

/*Retorna a concatenação do conteúdo da árvore fazendo percurso em pós-ordem à
 * partir do nó ou '#' caso o nó seja NULL. */
char *abb_pos_ordem(No *no) {
  if (no == NULL) {
      return "#";
  }
  char concatenacao[100];

  return posOrdem(no, concatenacao);
}

No *sucessor(No *no) {
  No *aux;
  No *y;
  if (no->dir != NULL) {
    return minimo(no->dir);
  }
  y = no->pai;
  while (y != NULL && no == y->dir) {
    no = y;
    y = no->pai;
  }
  return y;
}

No *minimo (No *no) {
  while (no->esq != NULL) {
    no = no->esq;
  }
  return no;
}

char *preOrdem(No *no, char *concat) {
  strcat(concat, &no->conteudo);
  preOrdem(no->esq, concat);
  preOrdem(no->dir, concat);

  return concat;
}

char *posOrdem(No *no, char *concat) {
  preOrdem(no->esq, concat);
  preOrdem(no->dir, concat);
  strcat(concat, &no->conteudo);

  return concat;
}