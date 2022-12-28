#include "Aluno.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct aluno{
    int matricula;
    char nome[50];
    char curso[30];
};

int verifica_params(int matricula, char *nome, char *curso) {
  if (matricula < 0 || nome == NULL || curso == NULL) {
    return -1;
  }

  if (strlen(nome) > 50 || strlen(curso) > 30) {
    return -1;
  }

  return 1;
}

Aluno *alu_novo(int matricula, char *nome, char *curso) {
  if (verifica_params(matricula, nome, curso) == -1) {
    return NULL;
  }

  Aluno *novo_aluno = (Aluno *)malloc(sizeof(Aluno));
  novo_aluno->matricula = matricula;
  strcpy(novo_aluno->nome, nome);
  strcpy(novo_aluno->curso, curso);

  return novo_aluno;
}

void alu_acessa(Aluno *aluno, int *matricula, char *nome, char *curso) {
  if (aluno == NULL) {
    *matricula = -1;
    strcpy(nome, "NULL");
    strcpy(curso, "NULL");
  } else {
    *matricula = aluno->matricula;
    strcpy(nome, aluno->nome);
    strcpy(curso, aluno->curso);
  }
}

void alu_atribui(Aluno *aluno, int matricula, char *nome, char *curso) {
  if (aluno != NULL && verifica_params(matricula, nome, curso) == 1) {
    aluno->matricula = matricula;
    strcpy(aluno->nome, nome);
    strcpy(aluno->curso, curso);
  }
}

int alu_igual(Aluno *aluno1, Aluno *aluno2) {

  if (aluno1 == NULL || aluno2 == NULL) {
    return -1;
  }

  if (aluno1->matricula != aluno2->matricula) {
    return 0;
  }

  if (strcmp(aluno1->nome, aluno2->nome) != 0) {
    return 0;
  }

  if (strcmp(aluno1->curso, aluno2->curso) != 0) {
    return 0;
  }

  return 1;
}

int alu_tamanho(){ 
    return sizeof(Aluno); 
}

void alu_libera(Aluno **aluno) {
  if (aluno != NULL) {
    free(*aluno);
    *aluno = NULL;
  }
}