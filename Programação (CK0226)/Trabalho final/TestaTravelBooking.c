#include "TravelBooking.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

float teste_passageiro_novo_com_dados_validos() {
  char nome[50];
  char endereco[50];
  Passageiro *passageiro = passageiro_novo(1, "Livia", "messejana");

  if (passageiro != NULL) {
    printf("Teste da função passageiro_novo() com dados válidos!\n");
  } else {
    printf("Teste da função passageiro_novo() com dados válidos!\n");
  }
}

float teste_passageiro_novo_com_dados_invalidos() {
  char nome[55] = "N";
  char endereco[50] = "C";

  for (int i = 0; i < 53; i++) {
    strcat(nome, "N");
  }

  for (int i = 0; i < 33; i++) {
    strcat(endereco, "C");
  }

  Passageiro *passageiro = passageiro_novo(-1, nome, endereco);
  if (passageiro == NULL) {
    printf("Teste da função passageiro_novo() com dados inválidos!\n");
  } else {
    printf("Teste da função passageiro_novo() com dados inválidos!\n");
  }
}

float teste_passageiro_novo_com_dados_nulos() {
  Passageiro *passageiro = passageiro_novo(-1, NULL, NULL);
  if (passageiro == NULL) {
    printf("Teste da função passageiro_novo() com dados nulos!\n");
  } else {
    printf("Teste da função passageiro_novo() com dados nulos!\n");
  }
}

float teste_passageiro_acessa_com_dados_validos() {
  int id;
  char nome[50];
  char endereco[50];

  Passageiro *passageiro = passageiro_novo(1, "Carlos", "Barroso");
  if (passageiro != NULL) {
    passageiro_acessa(passageiro, &id, nome, endereco);
    if (id == 1 && strcmp(nome, "Carlos") == 0 &&
        strcmp(endereco, "Barroso") == 0) {
      printf(
          "Teste da função passageiro_acessa() com dados válidos!\n");
    } else {
      printf(
          "Teste da função passageiro_acessa()com dados válidos!\n");
    }
  } else {
    printf("Teste da função passageiro_acessa() com dados válidos!\n");
  }
}

float teste_passageiro_atribui_com_dados_validos() {
  int id;
  char nome[50];
  char endereco[50];

  Passageiro *passageiro = passageiro_novo(1, "Carlos", "Barroso");
  if (passageiro != NULL) {
    passageiro_atribuir(passageiro, 2, "Livia", "Messejana");
    passageiro_acessa(passageiro, &id, nome, endereco);
    if (id == 2 && strcmp(nome, "Livia") == 0 &&
        strcmp(endereco, "Messejana") == 0) {
      printf(
          "Teste da função passageiro_atribuir() com dados válidos!\n");
    } else {
      printf(
          "Teste da função passageiro_atribuir() com dados válidos!\n");
    }
  } else {
    printf(
        "Teste da função passageiro_atribuir() com dados válidos!\n");
  }
}

float teste_passageiro_atribui_com_dados_invalidos() {
  int id;
  char nome[55] = "N";
  char endereco[50] = "C";

  for (int i = 0; i < 53; i++) {
    strcat(nome, "N");
  }

  for (int i = 0; i < 33; i++) {
    strcat(endereco, "C");
  }

  Passageiro *passageiro = passageiro_novo(1, "Carlos", "Barroso");
  if (passageiro != NULL) {
    passageiro_atribuir(passageiro, 2, nome, endereco);
    passageiro_acessa(passageiro, &id, nome, endereco);
    if (id == 1 || strcmp(nome, "Carlos") == 0 ||
        strcmp(endereco, "Barroso") == 0) {
      printf("Teste da função passageiro_atribuir() com dados "
             "inválidos!\n");
    } else {
      printf("Teste da função passageiro_atribuir() com dados "
             "inválidos!\n");
    }
  } else {
    printf(
        "Teste da função passageiro_atribuir() com dados inválidos!\n");
  }
}

float teste_passageiro_atribui_com_dados_nulos() {
  int id;
  char nome[50];
  char endereco[50];

  Passageiro *passageiro = passageiro_novo(1, "Carlos", "Barroso");
  if (passageiro != NULL) {
    passageiro_atribuir(NULL, -1, NULL, NULL);
    passageiro_acessa(passageiro, &id, nome, endereco);
    if (id == 1 && strcmp(nome, "Carlos") == 0 &&
        strcmp(endereco, "Barroso") == 0) {
      printf(
          "Teste da função passageiro_atribuir() com dados nulos!\n");
      
    } else {
      printf(
          "Teste da função passageiro_atribuir() com dados nulos!\n");
    }
  } else {
    printf("Teste da função passageiro_atribuir() com dados nulos!\n");
  }
}

float teste_passageiro_libera_com_dados_validos() {
  int id;
  char nome[50];
  char endereco[50];

  Passageiro *passageiro = passageiro_novo(1, "Carlos", "Barroso");
  passageiro_liberar(&passageiro);
  if (passageiro != NULL) {
    printf("Teste da função passageiro_liberar() com dados válidos!\n");
  } else {
    printf("Teste da função passageiro_liberar() com dados válidos!\n");
  }
}

float teste_passageiro_libera_com_dados_nulos() {
  int id;
  char nome[50];
  char endereco[50];

  Passageiro *passageiro = NULL;
  passageiro_liberar(&passageiro);
  if (passageiro == NULL) {
    printf("Teste da função passageiro_liberar() com dados nulos!\n");
    
  } else {
    printf("Teste da função passageiro_liberar() com dados nulos!\n");
  }
}

float teste_lista_cria_com_dados_validos() {
  ListaPassageiro *lista = lista_cria();
  if (lista != NULL) {
    printf("Teste da função criar_lista() com dados válidos!\n");
  } else {
    printf("Teste da função criar_lista() com dados válidos!\n");
  }
}

float teste_lista_libera_com_dados_validos() {
  ListaPassageiro *lista = lista_cria();
  lista_liberar(&lista);
  if (lista != NULL) {
    printf(
        "Teste da função lista_liberar() com dados válidos!\n");
  } else {
    printf(
        "Teste da função lista_liberar() com dados válidos!\n");
  }
}

float teste_lista_libera_com_dados_nulos() {
  if (lista_liberar(NULL) == 0) {
    printf("Teste da função lista_liberar() com dados nulos!\n");
  } else {
    printf("Teste da função lista_liberar() com dados nulos!\n");
  }
}

float teste_lista_inserir_com_dados_validos() {
  ListaPassageiro *lista = lista_cria();
  if (lista != NULL) {
    Passageiro *Carlos = passageiro_novo(1, "Carlos", "Barroso");
    if (lista_inserir(lista, Carlos) == 1) {
      Passageiro *Albert = passageiro_novo(2, "Albert", "Aldeota");
      if (lista_inserir(lista, Albert) == 1) {
        Passageiro *Ricardo = passageiro_novo(3, "Ricardo", "Eusebio");
        if (lista_inserir(lista, Ricardo) == 1) {
          printf("Teste da função lista_inserir() com dados "
                 "válidos!\n");
        } else {
          printf("Teste da função lista_inserir() com dados "
                 "válidos!\n");
        }
      } else {
        printf("Teste da função lista_inserir() com dados "
               "válidos!\n");
      }
    } else {
      printf("Teste da função lista_inserir() com dados "
             "válidos!\n");
    }
  } else {
    printf(
        "Teste da função lista_inserir() com dados válidos!\n");
  }
}

float teste_lista_inserir_com_dados_invalidos() {
  ListaPassageiro *lista = lista_cria();

  if (lista != NULL) {
    Passageiro *abraao = passageiro_novo(1, "Abraão", "Messejana");
    lista_inserir(lista, abraao);
    Passageiro *jaco = passageiro_novo(1, "Jaco", "ALdeota");
    if (lista_inserir(lista, jaco) == 0) {
      printf("Teste da função lista_inserir() com dados "
             "inválidos!\n");
      
    } else {
      printf("Teste da função lista_inserir() com dados "
             "inválidos!\n");
    }
  } else {
    printf("Teste da função lista_inserir() com dados "
           "inválidos!\n");
  }

}

float teste_lista_inserir_com_dados_nulos() {
  ListaPassageiro *lista = lista_cria();
  if (lista_inserir(lista, NULL) == -1) {
    Passageiro *abraao = passageiro_novo(1, "Abraão", "Messejana");
    if (lista_inserir(NULL, abraao) == -1) {
      if (lista_inserir(NULL, NULL) == -1) {
        printf("Teste da função lista_inserir() com dados "
               "nulos!\n");
  
      } else {
        printf("Teste da função lista_inserir() com dados "
               "nulos!\n");
      }
    } else {
      printf(
          "Teste da função lista_inserir() com dados nulos!\n");
    }
  } else {
    printf("Teste da função lista_inserir() com dados nulos!\n");
  }
}

float teste_lista_retira_com_dados_validos() {
  ListaPassageiro *lista = lista_cria();
  if (lista != NULL) {
    Passageiro *abraao = passageiro_novo(1, "Abraão", "Messejana");
    lista_inserir(lista, abraao);
    Passageiro *jaco = passageiro_novo(2, "Jaco", "Aracati");
    lista_inserir(lista, jaco);
    Passageiro *jose = passageiro_novo(3, "Jose", "Papicu");
    lista_inserir(lista, jose);
    Passageiro *passageiro = lista_retirar(lista);

    if (passageiro_igual(passageiro, abraao) == 1) {
      passageiro = lista_retirar(lista);
      if (passageiro_igual(passageiro, jaco) == 1) {
        passageiro = lista_retirar(lista);
        if (passageiro_igual(passageiro, jose) == 1) {
          printf("Teste da função lista_retirar() com dados "
                 "válidos!\n");
        } else {
          printf("Teste da função lista_retirar() com dados "
                 "válidos!\n");
        }
      } else {
        printf("Teste da função lista_retirar() com dados "
               "válidos!\n");
      }
    } else {
      printf(
          "Teste da função lista_retirar() com dados válidos!\n");
    }
  } else {
    printf(
        "Teste da função lista_retirar() com dados válidos!\n");
  }
}

float teste_lista_retira_com_dados_nulos() {
  if (lista_retirar(NULL) == NULL) {
    printf("Teste da função lista_retirar() com dados nulos!\n");
  } else {
    printf("Teste da função lista_retirar() com dados nulos!\n");
  }
}

float teste_lista_busca_com_dados_validos() {
  int id;
  char nome[50];
  char endereco[50];

  ListaPassageiro *lista = lista_cria();
  if (lista != NULL) {
    Passageiro *abraao = passageiro_novo(1, "Abraão", "Messejana");
    lista_inserir(lista, abraao);
    Passageiro *jaco = passageiro_novo(2, "Jaco", "Aracati");
    lista_inserir(lista, jaco);
    Passageiro *jose = passageiro_novo(3, "Jose", "Papicu");
    lista_inserir(lista, jose);
    Passageiro *aux = lista_busca(lista, 2);
    if (aux != NULL) {
      passageiro_acessa(aux, &id, nome, endereco);
      if (id == 2 && strcmp(nome, "Jaco") == 0 &&
          strcmp(endereco, "Computação") == 0) {
        printf("Teste da função lista_busca() com dados "
               "válidos!\n");
      } else {
        printf("Teste da função lista_busca() com dados "
               "válidos!\n");
      }
    } else {
      printf("Teste da função lista_busca() com dados "
             "válidos!\n");
    }
  } else {
    printf("Teste da função lista_busca() com dados válidos!\n");
  }
}

float teste_lista_busca_com_dados_invalidos() {
  int id;
  char nome[50];
  char endereco[50];

  ListaPassageiro *lista = lista_cria();
  if (lista != NULL) {
    Passageiro *abraao = passageiro_novo(1, "Abraão", "Messejana");
    lista_inserir(lista, abraao);
    Passageiro *jaco = passageiro_novo(2, "Jaco", "Aracati");
    lista_inserir(lista, jaco);
    Passageiro *jose = passageiro_novo(3, "Jose", "papicu");
    lista_inserir(lista, jose);
    Passageiro *aux = lista_busca(lista, 5);
    if (aux == NULL) {
      printf("Teste da função lista_busca() com dados "
             "inválidos!\n");
    } else {
      printf("Teste da função lista_busca() com dados "
             "inválidos!\n");
    }
  } else {
    printf("Teste da função lista_busca() com dados "
           "inválidos!\n");
  }
}

float teste_lista_busca_com_dados_nulos() {
  int id;
  char nome[50];
  char endereco[50];

  Passageiro *aux = lista_busca(NULL, 1);
  if (aux == NULL) {
    printf("Teste da função lista_busca() com dados nulos!\n");
  } else {
    printf("Teste da função lista_busca() com dados nulos!\n");
  }
}

float bateria_testes_01() {
  printf("====================================================================="
         "====================\n");
  printf(".:: Bateria de Testes para a TAD passageiro ::.\n");
  printf("====================================================================="
         "====================\n");
  teste_passageiro_novo_com_dados_validos();
  teste_passageiro_novo_com_dados_invalidos();
  teste_passageiro_novo_com_dados_nulos();
  teste_passageiro_acessa_com_dados_validos();
  teste_passageiro_atribui_com_dados_validos();
  teste_passageiro_atribui_com_dados_invalidos();
  teste_passageiro_atribui_com_dados_nulos();
  teste_passageiro_libera_com_dados_validos();
  teste_passageiro_libera_com_dados_nulos();
  teste_lista_cria_com_dados_validos();
  teste_lista_libera_com_dados_validos();
  teste_lista_busca_com_dados_validos();
  teste_lista_busca_com_dados_nulos();
  teste_lista_busca_com_dados_invalidos();
  teste_lista_inserir_com_dados_validos();
  teste_lista_inserir_com_dados_nulos();
  teste_lista_inserir_com_dados_invalidos();
  teste_lista_libera_com_dados_nulos();
  teste_lista_retira_com_dados_nulos();
  teste_lista_retira_com_dados_validos();
  printf("====================================================================="
         "====================\n\n");
}

/*===================================================================
========================== Teste de voo =============================
====================================================================*/

float teste_voo_novo_com_dados_validos() {
  char origem[50];
  char destino[50];

  Voo *voo = voo_novo(1, "Fortaleza", "São paulo");

  if (voo != NULL) {
    printf("Teste da função voo_novo() com dados válidos!\n");
  } else {
    printf("Teste da função voo_novo() com dados válidos!\n");
  }
}

float teste_voo_novo_com_dados_invalidos() {
  char origem[55] = "N";
  char destino[50] = "C";

  for (int i = 0; i < 53; i++) {
    strcat(origem, "N");
  }

  for (int i = 0; i < 33; i++) {
    strcat(destino, "C");
  }

  Voo *voo = voo_novo(-1, origem, destino);
  if (voo == NULL) {
    printf("Teste da função voo_novo() com dados inválidos!\n");
  } else {
    printf("Teste da função voo_novo() com dados inválidos!\n");
  }
}

float teste_voo_novo_com_dados_nulos() {
  Voo *voo = voo_novo(-1, NULL, NULL);
  if (voo == NULL) {
    printf("Teste da função voo_novo() com dados nulos!\n");
    
  } else {
    printf("Teste da função voo_novo() com dados nulos!\n");
  }
}

float teste_voo_acessa_com_dados_validos() {
  int codigo;
  char origem[50];
  char destino[50];

  Voo *voo = voo_novo(1, "Fortaleza", "São Paulo");
  if (voo != NULL) {
    passageiro_acessa(voo, &codigo, origem, destino);
    if (codigo == 1 && strcmp(origem, "Fortaleza") == 0 &&
        strcmp(destino, "São Paulo") == 0) {
      printf(
          "Teste da função voo_acessa() com dados válidos!\n");

    } else {
      printf(
          "Teste da função voo_acessa()com dados válidos!\n");
    }
  } else {
    printf("Teste da função voo_acessa() com dados válidos!\n");
  }
}

float teste_voo_atribui_com_dados_validos() {
  int codigo;
  char origem[50];
  char destino[50];

  Voo *voo = voo_novo(1, "Fortaleza", "São Paulo");
  if (voo != NULL) {
    voo_atribuir(voo, 2, "Belo Horizonte", "Parana");
    voo_acessa(voo, &codigo, origem, destino);
    if (codigo == 2 && strcmp(origem, "Fortaleza") == 0 &&
        strcmp(destino, "Parana") == 0) {
      printf(
          "Teste da função voo_atribuir() com dados válidos!\n");

    } else {
      printf(
          "Teste da função voo_atribuir() com dados válidos!\n");
    }
  } else {
    printf(
        "Teste da função voo_atribuir() com dados válidos!\n");
  }
}

float teste_voo_atribui_com_dados_invalidos() {
  int codigo;
  char origem[55] = "N";
  char destino[50] = "C";

  for (int i = 0; i < 53; i++) {
    strcat(origem, "N");
  }

  for (int i = 0; i < 33; i++) {
    strcat(destino, "C");
  }

  Voo *voo = voo_novo(1, "Fortaleza", "Sao Paulo");
  if (voo != NULL) {
    voo_atribuir(voo, 2, origem, destino);
    voo_acessa(voo, &codigo, origem, destino);
    if (codigo == 1 || strcmp(origem, "Fortaleza") == 0 ||
        strcmp(destino, "Sao Paulo") == 0) {
      printf("Teste da função voo_atribuir() com dados "
             "inválidos!\n");

    } else {
      printf("Teste da função voo_atribuir() com dados "
             "inválidos!\n");
    }
  } else {
    printf(
        "Teste da função voo_atribuir() com dados inválidos!\n");
  }
}

float teste_voo_atribui_com_dados_nulos() {
  int codigo;
  char origem[50];
  char destino[50];

  Voo *voo = voo_novo(1, "Fortaleza", "Sao Paulo");
  if (voo != NULL) {
    voo_atribuir(NULL, -1, NULL, NULL);
    voo_acessa(voo, &codigo, origem, destino);
    if (codigo == 1 && strcmp(origem, "Fortaleza") == 0 &&
        strcmp(destino, "Sao Paulo") == 0) {
      printf(
          "Teste da função voo_atribuir() com dados nulos!\n");
      
    } else {
      printf(
          "Teste da função voo_atribuir() com dados nulos!\n");
    }
  } else {
    printf("Teste da função voo_atribuir() com dados nulos!\n");
  }
}

float teste_voo_libera_com_dados_validos() {
  int codigo;
  char origem[50];
  char destino[50];

  Voo *voo = voo_novo(1, "Fortaleza", "Sao Paulo");
  voo_liberar(&voo);
  if (voo != NULL) {
    printf("Teste da função voo_liberar() com dados válidos!\n");
  } else {
    printf("Teste da função voo_liberar() com dados válidos!\n");
  }
}

float teste_voo_libera_com_dados_nulos() {
  int codigo;
  char origem[50];
  char destino[50];

  Voo *voo = NULL;
  voo_liberar(&voo);
  if (voo == NULL) {
    printf("Teste da função voo_liberar() com dados nulos!\n");
    
  } else {
    printf("Teste da função voo_liberar() com dados nulos!\n");
  }
}

float teste_lista_voo_cria_com_dados_validos() {
  ListaVoo *lista = lista_Voo_cria();
  if (lista != NULL) {
    printf("Teste da função lista_Voo_cria() com dados válidos!\n");
  } else {
    printf("Teste da função lista_Voo_cria() com dados válidos!\n");
  }
}

float teste_lista_voo_libera_com_dados_validos() {
  ListaVoo *lista = lista_Voo_cria();
  lista_Voo_liberar(&lista);
  if (lista != NULL) {
    printf(
        "Teste da função lista_Voo_liberar() com dados válidos!\n");
  } else {
    printf(
        "Teste da função lista_Voo_liberar() com dados válidos!\n");
  }
}

float teste_lista_voo_libera_com_dados_nulos() {
  if (lista_Voo_liberar(NULL) == 0) {
    printf("Teste da função lista_Voo_liberar() com dados nulos!\n");
  } else {
    printf("Teste da função lista_Voo_liberar() com dados nulos!\n");
  }
}



float teste_lista_voo_inserir_com_dados_validos() {
  ListaVoo *lista = lista_Voo_cria();
  if (lista != NULL) {
    Voo *fortaleza_sp = voo_novo(1, "Fortaleza", "Sao Paulo");
    if (lista_Voo_inserir(lista, fortaleza_sp) == 1) {
      Voo *juazeiro_parana = voo_novo(2, "Juazeiro", "Parana");
      if (lista_Voo_inserir(lista, juazeiro_parana) == 1) {
        Voo *rio_rs = voo_novo(3, "RIo de janeiro", "Rio grande do Sul");
        if (lista_Voo_inserir(lista, rio_rs) == 1) {
          printf("Teste da função lista_Voo_inserir() com dados "
                 "válidos!\n");
    
        } else {
          printf("Teste da função lista_Voo_inserir() com dados "
                 "válidos!\n");
        }
      } else {
        printf("Teste da função lista_Voo_inserir() com dados "
               "válidos!\n");
      }
    } else {
      printf("Teste da função lista_Voo_inserir() com dados "
             "válidos!\n");
    }
  } else {
    printf(
        "Teste da função lista_Voo_inserir() com dados válidos!\n");
  }
}

float teste_lista_voo_inserir_com_dados_invalidos() {
  ListaVoo *lista = lista_Voo_cria();

  if (lista != NULL) {
    Voo *fortaleza_sp = voo_novo(1, "Fortaleza", "Sao Paulo");
    lista_Voo_inserir(lista, fortaleza_sp);
    Voo *rio_rs = voo_novo(1, "RIo de Janeiro", "Rio grande do Sul");
    if (lista_Voo_inserir(lista, rio_rs) == 0) {
      printf("Teste da função lista_Voo_inserir() com dados "
             "inválidos!\n");
      
    } else {
      printf("Teste da função lista_Voo_inserir() com dados "
             "inválidos!\n");
    }
  } else {
    printf("Teste da função lista_Voo_inserir() com dados "
           "inválidos!\n");
  }

}

float teste_lista_voo_inserir_com_dados_nulos() {
  ListaVoo *lista = lista_Voo_cria();
  if (lista_Voo_inserir(lista, NULL) == -1) {
    Voo *Fortaleza_sp = voo_novo(1, "Fortaleza", "Sao Paulo");
    if (lista_Voo_inserir(NULL, Fortaleza_sp) == -1) {
      if (lista_Voo_inserir(NULL, NULL) == -1) {
        printf("Teste da função lista_Voo_inserir() com dados "
               "nulos!\n");
  
      } else {
        printf("Teste da função lista_Voo_inserir() com dados "
               "nulos!\n");
      }
    } else {
      printf(
          "Teste da função lista_Voo_inserir() com dados nulos!\n");
    }
  } else {
    printf("Teste da função lista_Voo_inserir() com dados nulos!\n");
  }
}

float teste_lista_voo_retira_com_dados_validos() {
  ListaVoo *lista = lista_Voo_cria();
  if (lista != NULL) {
    Voo *fortaleza_sp = voo_novo(1, "Fortaleza", "Sao Paulo");
    lista_Voo_inserir(lista, fortaleza_sp);
    Voo *juazeiro_parana = voo_novo(2, "Juazeiro", "Parana");
    lista_Voo_inserir(lista, juazeiro_parana);
    Voo *rio_rs = voo_novo(3, "Rio de Janeiro", "Rio grande do Sul");
    lista_Voo_inserir(lista, rio_rs);
    Voo *voo = lista_voo_retirar(lista);

    if (voo_igual(voo, fortaleza_sp) == 1) {
      voo = lista_voo_retirar(lista);
      if (voo_igual(voo, juazeiro_parana) == 1) {
        voo = lista_voo_retirar(lista);
        if (voo_igual(voo, rio_rs) == 1) {
          printf("Teste da função lista_voo_retirar() com dados "
                 "válidos!\n");
    
        } else {
          printf("Teste da função lista_voo_retirar() com dados "
                 "válidos!\n");
        }
      } else {
        printf("Teste da função lista_voo_retirar() com dados "
               "válidos!\n");
      }
    } else {
      printf(
          "Teste da função lista_voo_retirar() com dados válidos!\n");
    }
  } else {
    printf(
        "Teste da função lista_voo_retirar() com dados válidos!\n");
  }
}

float teste_lista_voo_retira_com_dados_nulos() {
  if (lista_voo_retirar(NULL) == NULL) {
    printf("Teste da função lista_voo_retirar() com dados nulos!\n");
  } else {
    printf("Teste da função lista_voo_retirar() com dados nulos!\n");
  }
}

float teste_lista_voo_busca_com_dados_validos() {
  int codigo;
  char origem[50];
  char destino[50];

  ListaVoo *lista = lista_Voo_cria();
  if (lista != NULL) {
    Voo *fortaleza_sp = voo_novo(1, "Fortaleza", "Sao paulo");
    lista_Voo_inserir(lista, fortaleza_sp);
    Voo *juazeiro_parana = voo_novo(2, "Juazeiro", "Parana");
    lista_Voo_inserir(lista, juazeiro_parana);
    Voo *rio_rs = voo_novo(3, "Rio de Janeiro", "Rio grande do Sul");
    lista_Voo_inserir(lista, rio_rs);
    Voo *aux = lista_Voo_busca(lista, 2);
    if (aux != NULL) {
      voo_acessa(aux, &codigo, origem, destino);
      if (codigo == 2 && strcmp(origem, "Jaco") == 0 &&
          strcmp(destino, "Computação") == 0) {
        printf("Teste da função lista_Voo_busca() com dados "
               "válidos!\n");
  
      } else {
        printf("Teste da função lista_Voo_busca() com dados "
               "válidos!\n");
      }
    } else {
      printf("Teste da função lista_Voo_busca() com dados "
             "válidos!\n");
    }
  } else {
    printf("Teste da função lista_Voo_busca() com dados válidos!\n");
  }
}

float teste_lista_voo_busca_com_dados_invalidos() {
  int codigo;
  char origem[50];
  char destino[50];

  ListaVoo *lista = lista_Voo_cria();
  if (lista != NULL) {
    Voo *fortaleza_sp = voo_novo(1, "Fortaleza", "Sao Paulo");
    lista_inserir(lista, fortaleza_sp);
    Voo *juazeiro_parana = voo_novo(2, "Juazeiro", "Parana");
    lista_inserir(lista, juazeiro_parana);
    Voo *rio_rs = voo_novo(3, "Rio de Janeiro", "Rio grande do Sul");
    lista_inserir(lista, rio_rs);
    Voo *aux = lista_Voo_busca(lista, 5);
    if (aux == NULL) {
      printf("Teste da função lista_Voo_busca() com dados "
             "inválidos!\n");
      
    } else {
      printf("Teste da função lista_Voo_busca() com dados "
             "inválidos!\n");
    }
  } else {
    printf("Teste da função lista_Voo_busca() com dados "
           "inválidos!\n");
  }
}

float teste_lista_voo_busca_com_dados_nulos() {
  int codigo;
  char origem[50];
  char destino[50];

  Voo *aux = lista_Voo_busca(NULL, 1);
  if (aux == NULL) {
    printf("Teste da função lista_Voo_busca() com dados nulos!\n");
  } else {
    printf("Teste da função lista_Voo_busca() com dados nulos!\n");
  }
}

float bateria_testes_voo_01() {
  printf("====================================================================="
         "====================\n");
  printf(".:: Bateria de Testes para a tad voo ::.\n");
  printf("====================================================================="
         "====================\n");
  
  teste_voo_novo_com_dados_validos();
  teste_voo_novo_com_dados_invalidos();
  teste_voo_novo_com_dados_nulos();
  teste_voo_acessa_com_dados_validos();
  teste_voo_libera_com_dados_validos();
  teste_voo_atribui_com_dados_validos();
  teste_voo_atribui_com_dados_invalidos();
  teste_voo_atribui_com_dados_nulos();
  teste_voo_libera_com_dados_nulos();
  teste_lista_voo_cria_com_dados_validos();
  teste_lista_voo_busca_com_dados_validos();
  teste_lista_voo_busca_com_dados_nulos();
  teste_lista_voo_busca_com_dados_invalidos();
  teste_lista_voo_inserir_com_dados_nulos();
  teste_lista_voo_inserir_com_dados_invalidos();
  teste_lista_voo_inserir_com_dados_validos();
  teste_lista_voo_libera_com_dados_nulos();
  teste_lista_voo_libera_com_dados_validos();
  teste_lista_voo_retira_com_dados_nulos();
  teste_lista_voo_retira_com_dados_validos();
  
  printf("====================================================================="
         "====================\n");
}

int main(void) {
  bateria_testes_01();
  printf("\n");
  bateria_testes_voo_01();
  return 0;
  int op, cod, id;
    Reserva *r;

    inicializar_tabela_hash();

    do {
        printf("----------------------- MENU -------------------------\n");
        printf("\n\t\t0 - Sair do Menu\n");
        printf("\t\t1 - Inserir Reserva\n"); 
        printf("\t\t2 - Editar Reserva\n"); 
        printf("\t\t3 - Deletar Reserva\n"); 
        printf("\t\t4 - Buscar Reserva\n");
        printf("\t\t5 - Imprimir tabela\n\t\tOp: ");
        scanf("%d", &op);
        
        switch(op){
        case 0:
            printf("\t\tSaindo...\n");
            break;
        
        case 1:
            inserir_trecho_na_tabela();
            break;
        
        case 2:
            printf("Informe o codigo da reserva: \n");
            scanf("%d", &cod);
            printf("Informe o id do passageiro: \n");
            scanf("%d", &id);
            editar_reserva_no_trecho(id, cod);
            break;

        case 3:
            printf("Informe o codigo da reserva: \n");
            scanf("%d", &cod);
            printf("Informe o id do passageiro: \n");
            scanf("%d", &id);
            deletar_reserva_no_trecho(id, cod);
            break;
        
        case 4:
            printf("Informe o codigo da reserva: \n");
            scanf("%d", &cod);
            printf("Informe o id do passageiro: \n");
            scanf("%d", &id);

            r = buscar_reserva_na_tabela_hash(id, cod);
            if(r) {
                printf("\t Reserva encontrada!\n");
                printf("\t  * Codigo: %d\n", r->codigo);
                imprimir_data(r->data_viagem);
                imprimir_passageiro(r->passageiro);
                imprimir_voo(r->voo);
                printf("Assento: %d\n", r->assento);
            } else
                printf("\tReserva nao encontrada!\n");
            break;
        
        case 5:
            imprimir_tabela_hash();
            break;
        
        default:
            printf("Opcao invalida!\n");
        }
        printf("----------------------FIM MENU------------------------\n\n");
    } while(op != 0);

    return 0;
}