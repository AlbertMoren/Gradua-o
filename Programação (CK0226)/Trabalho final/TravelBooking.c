#include "TravelBooking.h"
#include "tabela_hash.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct agenda {
  Reserva *reserva;
  Agenda *esq;
  Agenda *dir;
};

struct viagem {
  struct trecho *trechos;
};

struct tabela_viagem {
  int tamanho;
  Viagem *tabela_hash;
};

struct passageiro {
  int id;
  char *nome[50];
  char *endereco[50];
};

struct no_passageiro {
  Passageiro *passageiro;
  struct no_passageiro *proximo;
};

struct lista_passageiro {
  struct no_passageiro *primeiro;
};

typedef struct no_passageiro No_Passagueiro;

/* Aloca espaço em memória e retorna uma Lista */
ListaPassageiro *lista_cria(){
  ListaPassageiro *lista = (ListaPassageiro *)malloc(sizeof(ListaPassageiro));
  lista->primeiro = NULL;
  return lista;
}

/* Libera a memória da lista previamente criada e atribui NULL ao ponteiro lista.
 * Retorna 1 caso seja possível fazer a liberação e 0 caso a lista informada seja NULL. */
int lista_liberar(ListaPassageiro **lista){
  if(lista != NULL){
    if((*lista)->primeiro != NULL){
      No_Passagueiro *aux = (*lista)->primeiro;
      do{
        passageiro_liberar(&aux->passageiro);
        aux = aux->proximo;
      }while(aux != NULL);
    }
    free(*lista);
    *lista = NULL;
    return 1;
  }
  return 0;
}

/* Insere um passageiro na lista.
 *  Retorna 1 se foi possível adicionar, 0 caso já exista um passageiro com o mesmo id (nesse caso, o passageiro não pode ser adicionado) e -1 caso a lista ou passageiro sejam NULL */
int lista_inserir(ListaPassageiro *lista, Passageiro *passageiro){
  if(lista == NULL || passageiro==NULL){
    return -1;
  }

  if(lista->primeiro != NULL){
    int id_passagueiro;
    char nome[50];
    char endereco[50];
    passageiro_acessa(passageiro, &id_passagueiro,nome,endereco);
    Passageiro *passageiro_aux = lista_busca(lista,id_passagueiro);
    if(passageiro_aux != NULL){
      return 0;
    }
  }

  if(lista->primeiro == NULL){
    No_Passagueiro *novo = (No_Passagueiro *)malloc(sizeof(No_Passagueiro));
    novo->passageiro = passageiro;
    novo->proximo = NULL;
    lista->primeiro = novo;
  }else{
    No_Passagueiro *ultimo = lista->primeiro;
    while (ultimo->proximo != NULL){
      ultimo = ultimo->proximo;
    }

    No_Passagueiro *novo = (No_Passagueiro *)malloc(sizeof(No_Passagueiro));
    novo->passageiro = passageiro;
    novo->proximo = NULL;
    ultimo->proximo = novo;
  }
  return 1;
}

/* Busca passageiro pelo número de id. Retorna o passageiro se este estiver na
 * lista e NULL caso contrário, isto é, (i) lista vazia; (ii) não exista passageiro com a id fornecida;
 * ou (iii) a lista seja NULL */
ListaPassageiro *lista_busca(ListaPassageiro *lista, int ID){
  if(lista != NULL && lista->primeiro != NULL){

    int passageiro_id;
    char nome[50];
    char endereco[50];

    No_Passagueiro *aux = lista->primeiro;
    do{
      passageiro_acessa(aux->passageiro, &passageiro_id, nome, endereco);
      if(ID == passageiro_id){
        return aux->passageiro;
      }
      aux = aux->proximo;
    }while(aux != NULL);
  }

  return NULL;
}

/* Remove um passagueiro na lista. Retorna o passagueiro ou NULL caso a lista esteja vazia*/
ListaPassageiro *lista_retirar(ListaPassageiro *lista){
  if(lista == NULL || lista->primeiro == NULL){
    return NULL;
  }
  Passageiro *passageiro = lista->primeiro->passageiro;
  lista->primeiro = lista->primeiro->proximo;
  return passageiro;
}

/* Verifica se a lista está vazia. Retorna 1 se a lista estiver vazia, 0 caso não
 * esteja vazia e -1 se a lista for NULL*/
int lista_vazia(ListaPassageiro* lista){
  if (lista==NULL){
    return -1;
  }
  if (lista->primeiro==NULL){
    return 1;
  }
  return 0;
}

/* Recupera o primeiro passageiro da fila. Retorna o passageiro ou NULL caso a lista esteja vazia ou seja NULL */
Passageiro *lista_primeiro(ListaPassageiro* lista){
  if(lista == NULL || lista->primeiro ==NULL){
    return NULL;
  }
  return lista->primeiro->passageiro;
}


/* Computa a quantidade de passageiros na fila. Retorna a quantidade de passageiros
 * ou -1, caso a fila for NULL.*/
int lista_quantidade(ListaPassageiro *lista) {
  if (lista == NULL) {
    return -1;
  }

  int quantidade = 0;
  No_Passagueiro *percorre = lista->primeiro;
  while (percorre != NULL) {
    quantidade++;
    percorre = percorre->proximo;
  }

  return quantidade;
}


/*=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
//=-=-=-=-=-=-=-=-=-=-=-=Lista funções de passageiros=-=-==-=-=
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-*/

int verificar_parametros(int passageiro_id, char *nome, char *endereco){
    if(passageiro_id < 0 || nome == NULL || endereco == NULL){
        return -1;
    }

    if(strlen(nome) > 50 || strlen(endereco) > 50){
        return -1;
    }

    return 1;
}

/* Aloca e retorna um passageiro com os dados passados por parâmetro. Porém, para os
 * casos em que (i) pelo menos um dos parâmetros sejam nulos <-1, NULL, NULL>; e
 * (ii) o tamanho das strings nome e endereço sejam maiores que os da especificação
 * (50 e 50, respectivamente), a função deve retornar NULL. */
Passageiro *passageiro_novo(int id, char *nome,char *endereco){
  if(verificar_parametros(id,nome,endereco)== -1){
    return NULL;
  }
  if(strcmp(nome,endereco) == 0){
    return NULL;
  }
  Passageiro *novo_passageiro = (Passageiro *)malloc(sizeof(Passageiro));
  novo_passageiro->id = id;
  strcpy(novo_passageiro->nome, nome);
  strcpy(novo_passageiro->endereco, endereco);

  return novo_passageiro;
}

/* Libera a memória de um passageiro previamente criado e atribui NULL ao passageiro. */
void passageiro_liberar(Passageiro **passageiro){
  if(passageiro != NULL){
    free(*passageiro);
    *passageiro = NULL;
  }
}

/* Copia os valores de um passageiro para  as referências informadas. Em caso de passageiro,
 * atribuir valor padrão <-1, "NULL", "NULL"> aos parâmetros. */
void passageiro_acessa(Passageiro *passageiro,int *id, char *nome, char *endereco){
  if(passageiro == NULL){
    *id = -1;
    strcpy(nome, "NULL");
    strcpy(endereco, "NULL");
  }else{
    *id = passageiro->id;
    strcpy(nome, passageiro->nome);
    strcpy(endereco, passageiro->endereco);
  }
}


/* Atribui novos valores aos campos de um passageiro. Porém, para os casos em que (i)
 * algum dos parâmetros sejam nulos <NULL, -1, NULL, NULL>; ou (ii) o tamanho
 * das strings nome e curso sejam maiores que os da especificação (50 e 50,
 * respectivamente), a função não deve fazer a atribuição. */
void passageiro_atribuir(Passageiro *passageiro, int id, char *nome, char *endereco){
  if(passageiro != NULL && verificar_parametros(id,nome,endereco) == 1){
    passageiro->id = id;
    strcpy(passageiro->nome, nome);
    strcpy(passageiro->endereco, endereco);
  }
}

/* Avalia se dois passageiros são iguas. A função deve retornar 1 se os passageiros
 * possuem os mesmos dados, 0 caso os dados dos passageiro possuam alguma diferença
 * e -1 caso pelo menos um dos passageiro seja NULL.
 */
int passageiro_igual(Passageiro *passageiro1, Passageiro *passageiro2){
  if(passageiro1 == NULL || passageiro2 == NULL){
    return -1;
  }

  if(passageiro1->id != passageiro2->id){
    return 0;
  }

  if(strcmp(passageiro1->nome,passageiro2->nome) != 0){
    return 0;
  }

  if(strcmp(passageiro1->endereco,passageiro2->endereco) != 0){
    return 0;
  }

  return 1;
}



/*=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
//=-=-=-=-=-=-=-=-=Lista encadeada de passageiros-=-=-=-=-==-=-=
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-*/



/*=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
//=-=-=-=-=-=-=-=-=-=-=-=Lista encadeada de Voos=-=-=-=-=-==-=-=
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-*/
struct voo {
  int codigo;
  char *origem[50];
  char *destino[50];
};

struct no_voo {
  Voo *voo;
  struct no_voo *proximo;
};

struct lista_voo {
  struct no_voo *primeiro;
};

typedef struct no_voo No_voo;

/* Aloca espaço em memória e retorna uma Lista de voos*/
ListaVoo *lista_Voo_cria(){
  ListaVoo *lista = (ListaVoo *)malloc(sizeof(ListaVoo));
  lista->primeiro = NULL;
  return lista;
}

/* Libera a memória da lista previamente criada e atribui NULL ao ponteiro lista.
 * Retorna 1 caso seja possível fazer a liberação e 0 caso a lista informada seja NULL. */
int lista_Voo_liberar(ListaVoo **lista){
  if(lista != NULL){
    if((*lista)->primeiro != NULL){
      No_voo *aux = (*lista)->primeiro;
      do{
        passageiro_liberar(&aux->voo);
        aux = aux->proximo;
      }while(aux != NULL);
    }
    free(*lista);
    *lista = NULL;
    return 1;
  }
  return 0;
}

/* Insere um voo na lista.
 *  Retorna 1 se foi possível adicionar, 0 caso já exista um voo com o mesmo codigo (nesse caso, o voo não pode ser adicionado) e -1 caso a lista ou voo sejam NULL */
int lista_Voo_inserir(ListaVoo *lista, Voo *voo){
  if(lista == NULL || voo==NULL){
    return -1;
  }

  if(lista->primeiro != NULL){
    int codigo;
    char origem[50];
    char destino[50];
    voo_acessa(voo, &codigo,origem,destino);
    Voo *voo_aux = lista_Voo_busca(lista,codigo);
    if(voo_aux != NULL){
      return 0;
    }
  }

  if(lista->primeiro == NULL){
    No_voo *novo = (No_voo *)malloc(sizeof(No_voo));
    novo->voo = voo;
    novo->proximo = NULL;
    lista->primeiro = novo;
  }else{
    No_voo *ultimo = lista->primeiro;
    while (ultimo->proximo != NULL){
      ultimo = ultimo->proximo;
    }

    No_voo *novo = (No_voo *)malloc(sizeof(No_voo));
    novo->voo = voo;
    novo->proximo = NULL;
    ultimo->proximo = novo;
  }
  return 1;
}


/* Busca voo pelo número de codigo. Retorna o voo se este estiver na
 * lista e NULL caso contrário, isto é, (i) lista vazia; (ii) não exista voo com o codigo fornecida;
 * ou (iii) a lista seja NULL */
ListaVoo *lista_Voo_busca(ListaVoo *lista, int id){
  if(lista != NULL && lista->primeiro != NULL){

    int codigo;
    char origem[50];
    char destino[50];

    No_voo *aux = lista->primeiro;
    do{
      voo_acessa(aux->voo, &codigo, origem, destino);
      if(id == codigo){
        return aux->voo;
      }
      aux = aux->proximo;
    }while(aux != NULL);
  }

  return NULL;
}

/* Remove um voo na lista. Retorna o voo ou NULL caso a lista esteja vazia*/
ListaVoo *lista_voo_retirar(ListaVoo *lista){
  if(lista == NULL || lista->primeiro == NULL){
    return NULL;
  }
  Voo *voo = lista->primeiro->voo;
  lista->primeiro = lista->primeiro->proximo;
  return voo;
}

/* Verifica se a lista está vazia. Retorna 1 se a lista estiver vazia, 0 caso não
 * esteja vazia e -1 se a lista for NULL*/
int lista_Voo_vazia(ListaVoo* lista){
  if (lista==NULL){
    return -1;
  }
  if (lista->primeiro==NULL){
    return 1;
  }
  return 0;
}

/* Recupera o primeiro voo da fila. Retorna o voo ou NULL caso a lista esteja vazia ou seja NULL */
Voo *lista_Voo_primeiro(ListaVoo* lista){
  if(lista == NULL || lista->primeiro ==NULL){
    return NULL;
  }
  return lista->primeiro->voo;
}

/* Computa a quantidade de voo na fila. Retorna a quantidade de voos ou -1, caso a fila for NULL */
int lista_Voo_quantidade(ListaVoo *lista) {
  if (lista == NULL) {
    return -1;
  }

  int quantidade = 0;
  No_voo *percorre = lista->primeiro;
  while (percorre != NULL) {
    quantidade++;
    percorre = percorre->proximo;
  }

  return quantidade;
}

/*=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==
//=-=-=-=-=-=-=-=-=-=-=-=Lista funções de voos=-=-==-=-=-=-=-=-=
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-*/


int verificar_parametros_voos(int codigo, char *origem, char *destino){
    if(codigo < 0 || origem == NULL || destino == NULL){
        return -1;
    }

    if(strlen(origem) > 50 || strlen(destino) > 50){
        return -1;
    }

    return 1;
}

/* Aloca e retorna um voo com os dados passados por parâmetro. Porém, para os
 * casos em que (i) pelo menos um dos parâmetros sejam nulos <-1, NULL, NULL>; e
 * (ii) o tamanho das strings nome e curso sejam maiores que os da especificação
 * (50 e 50, respectivamente), a função deve retornar NULL. */
Voo *voo_novo(int codigo, char *origem,char *destino){
  if(verificar_parametros(codigo,origem,destino)== -1){
    return NULL;
  }
  if(strcmp(origem,destino) == 0){
    return NULL;
  }
  Voo *novo_voo = (Voo *)malloc(sizeof(Voo));
  novo_voo->codigo = codigo;
  strcpy(novo_voo->origem, origem);
  strcpy(novo_voo->destino, destino);

  return novo_voo;
}

/*Verifica se os dados do voos são validos, 
*retorna 1 se tiver ok, -1 se tiver invalido*/
int voo_verifica(Voo *voo) {
  int codigo_aux;
  char origem_aux[50];
  char destino_aux[50];
  
  voo_acessa(voo, &(codigo_aux), origem_aux, destino_aux);
  if (codigo_aux < 0 || origem_aux == NULL || destino_aux == NULL) {
    return -1;
  }
  else {
    return 1;
  }
}

/* Libera a memória de um voo previamente criado e atribui NULL ao passageiro. */
void voo_liberar(Voo **voo){
  if(voo != NULL){
    free(*voo);
    *voo = NULL;
  }
}

/* Copia os valores de um voo para as referências informadas. Em caso de voo NULL,
 * atribuir valor padrão <-1, "NULL", "NULL"> aos parâmetros. */
void voo_acessa(Voo *voo,int *codigo, char *origem, char *destino){
  if(voo == NULL){
    *codigo = -1;
    strcpy(origem, "NULL");
    strcpy(destino, "NULL");
  }else{
    *codigo = voo->codigo;
    strcpy(origem, voo->origem);
    strcpy(destino, voo->destino);
  }
}

/* Atribui novos valores aos campos de um voo. Porém, para os casos em que (i)
 * algum dos parâmetros sejam nulos <NULL, -1, NULL, NULL>; ou (ii) o tamanho
 * das strings origem e destino sejam maiores que os da especificação (50 e 50,
 * respectivamente), a função não deve fazer a atribuição. */
void voo_atribuir(Voo *voo, int codigo, char *origem, char *destino){
  if(voo != NULL && verificar_parametros(codigo,origem,destino) == 1){
    voo->codigo = codigo;
    strcpy(voo->origem, origem);
    strcpy(voo->destino, destino);
  }
}

/* Avalia se duas viagens são iguas. A função deve retornar 1 se os voos
 * possuem os mesmos dados, 0 caso os dados dos voos possuam alguma diferença
 * e -1 caso pelo menos um dos voo seja NULL.
 */
int voo_igual(Voo *voo1, Voo *voo2){
  if(voo1 == NULL || voo2 == NULL){
    return -1;
  }

  if(voo1->codigo != voo2->codigo){
    return 0;
  }

  if(strcmp(voo1->origem,voo2->origem) != 0){
    return 0;
  }

  if(strcmp(voo1->destino,voo2->destino) != 0){
    return 0;
  }

  return 1;
}

/* Retorna o tamanho em bytes do TAD voo. */
int voo_tramanho() {
  return sizeof(Voo); 
}

/*=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==
//=-=-=-=-=-=-=-=-=-=-=-=Árvore Binária =-=-==-=-=-=-=-=-=
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-*/
typedef struct Reserva {
    int codigo;
    Data *data_viagem;
    Passageiro *passageiro;
    Voo *voo;
    Assento assento;
} Reserva;

typedef struct Agenda {
    Reserva *reserva;
    struct Agenda *esq;
    struct Agenda *dir;
    struct Agenda *pai;
} Agenda;

typedef struct Trecho {
    Reserva *reserva;
    struct Trecho *proximo;
} Trecho;

typedef struct Viagem {
    Trecho *trechos;
} Viagem;

typedef struct Tabela_viagem {
    int tamanho;
    Viagem *tabela_hash;
} Tabela_viagem;

int checaData(Data anterior, Data nova){

    if (anterior.ano < nova.ano){
        return 1;
    }
    if (anterior.ano == nova.ano){
        if (anterior.mes < nova.mes){
            return 1;
        }
        if (anterior.mes == nova.mes && anterior.dia <= nova.dia){
            return 1;
        }
    }
    return 0;
}


Data hoje;

/* Cria ABB */
Agenda *IniciaABB(){

Reserva *primeira;
Reserva *prim;
primeira = PreencheReserva();
prim = primeira;



Data *aux = prim->data_viagem;


    //Dados Invalidos: (Data da viagem < Data de hoje)
    if (checaData(hoje, *aux) == 0){
        return NULL;
    }

//Happy path:
    Agenda *raiz = (Agenda *)malloc(sizeof(Agenda));
    raiz->reserva = prim;
    raiz->esq = NULL;
    raiz->dir = NULL;
    return raiz;
}



/* Procura a agenda pela data. Retorna a agenda caso a busca obtenha sucesso ou NULL
 * em caso contrário. */


Agenda *BuscaAgenda(Agenda *raiz, Data busca) { 
    Data *aux;
    *aux = busca;

    if (raiz != NULL) {
        if (raiz->reserva->data_viagem == aux){
            return raiz;
        }

        int checagemData;
        Data inicial;
        inicial = *raiz->reserva->data_viagem;

        checagemData = checaData(busca,inicial);


        if (checagemData == 0) {
            return BuscaAgenda(raiz->esq, busca);
        } else {
            return BuscaAgenda(raiz->dir, busca);
        }
    }

    return NULL;
}

//Funções da Árvore binária
Agenda *InsereAgenda(Agenda *raiz, Agenda *nova) {
    
    // impede de criar uma reserva com codigo de voo ou de reserva repetida
    Data *auxiliar;
    auxiliar = nova->reserva->data_viagem;


    int restricao, restricao2, restricao3, restricao4;
    restricao = BuscaInd(raiz,nova->reserva->passageiro->id);
    restricao2 = BuscaVoo(raiz,nova->reserva->voo->codigo);
    restricao3 = BuscaRes(raiz,nova->reserva->codigo);
    restricao4 = BuscaDeR(raiz,nova->reserva->passageiro->id,*auxiliar);

    if (restricao == 1){
        return NULL;
    }

    if (restricao2 == 1){
        return NULL;
    }

    if (restricao3 == 1){
       return NULL;
    }

    if (restricao4 == 1){
       return NULL;
    }

    if (raiz == NULL) {
        return nova;
    }
    // Insere a agenda
    Data *aux1, *aux2;
    aux1 = raiz->reserva->data_viagem;
    aux2 = nova->reserva->data_viagem;

    Data aux3, aux4;
    aux3 = *aux1;
    aux4 = *aux2;

    if (checaData(aux3, aux4) == 1){
        raiz->dir = InsereAgenda(raiz->dir, nova);
    } else {
        raiz->esq = InsereAgenda(raiz->esq, nova);
    }
    return raiz;

}


/*Realiza uma busca linear pelo código de reserva*/
Agenda *BuscaCodigo(Agenda *raiz, int reserva){
    if (raiz == NULL){
        return NULL;
    }
    if (raiz->reserva->codigo == reserva){
        return raiz;
    }
    Agenda *esq = BuscaCodigo(raiz->esq,reserva);
    Agenda *dir = BuscaCodigo(raiz->dir,reserva);
    if(esq != NULL){
        return esq;
    }
    return dir;
}
Agenda *BuscaAnterior(Agenda *raiz, int reserva){
    if (raiz == NULL){
        return NULL;
    }
    if (raiz->esq->reserva->codigo-> == reserva){
        return raiz;
    }
    if (raiz->dir->reserva->codigo-> == reserva){
        return raiz;
    }
    Agenda *esq = BuscaCodigo(raiz->esq,reserva);
    Agenda *dir = BuscaCodigo(raiz->dir,reserva);
    if(esq != NULL){
        return esq;
    }
    return dir;
}

/*Remove Agenda com um dado código de reserva*/
/*Agenda *removeCodigo(Agenda *raiz, int codigo){
    Agenda noRemove = BuscaCodigo(*raiz, codigo);
    Agenda antRemove = BuscaAnterior(*raiz, codigo);
    if(noRemove->esq == NULL && noRemove.dir == NULL){
        *Faz o nó anterior apontar para NULL seja onde antes apontava pra ele
    }
    if(noRemove->esq == NULL){
    }
    if(noRemove->dir == NULL){
    }

        Agenda noMinimo = BuscaMinimo(*noRemove);

}
Agenda *BuscaMinimo(Agenda *raiz){
    *Vai ao máximo a esq do Nó enquanto for diferente de NULL.

    Agenda aux = raiz->dir;

    while(aux->esq != Null){
        aux = aux->esq;
    }

}
void Transplante(Agenda *raiz){
     *I-Identifica nó a se remover
     *II- Percorre com BuscaMinimo(noRemover->dir)
     *III- Armazena em uma variável e substitui por NULL na abb
     *IV- Substitui o noRemove pela variável
     *V- Retorna abb alterada
}*/


/*Busca por (i) identificador do passageiro e código do voo*/
Agenda *BuscaI(Agenda *raiz, Passageiro passageiro, int codigo){

Passageiro *passageiroaux;
*passageiroaux = passageiro;


    if (raiz == NULL){
        return NULL;
    }
    if (raiz->reserva->codigo == codigo && raiz->reserva->passageiro == passageiroaux){
        return raiz;
    }
    Agenda *esq = BuscaI(raiz->esq,passageiro, codigo);
    Agenda *dir = BuscaI(raiz->dir,passageiro, codigo);
    if(esq != NULL){
        return esq;
    }
    return dir;
}

/*Busca por (ii) identificador do passageiro e data da viagem.*/

Agenda *BuscaII(Agenda *raiz, Passageiro passageiro, Data data){

Passageiro *passageiroaux;
*passageiroaux = passageiro;

Data *dataaux;
*dataaux = data;


    if (raiz == NULL){
        return NULL;
    }
    if (raiz->reserva->data_viagem == dataaux && raiz->reserva->passageiro == passageiroaux){
        return raiz;
    }
    Agenda *esq = BuscaII(raiz->esq,passageiro,data);
    Agenda *dir = BuscaII(raiz->dir,passageiro,data);
    if(esq != NULL){
        return esq;
    }
    return dir;
}

/*Busca por identificador do passageiro*/
int *BuscaInd(Agenda *raiz, int codigo){

    if (raiz->reserva->passageiro->id == codigo){
        return 1;
    }

    if(raiz != NULL){
        BuscaInd(raiz->esq,codigo);
        BuscaInd(raiz->dir,codigo);
    }
}

/*Busca por identificador de reserva*/
int *BuscaRes(Agenda *raiz, int codigo){

    if (raiz->reserva->codigo == codigo){
        return 1;
    }

    if(raiz != NULL){
        BuscaRes(raiz->esq,codigo);
        BuscaRes(raiz->dir,codigo);
    }
}

/*Busca por identificador do voo*/
int *BuscaVoo(Agenda *raiz, int voo){

    if (raiz->reserva->voo->codigo == voo){
        return 1;
    }

    if(raiz != NULL){
        BuscaVoo(raiz->esq,voo);
        BuscaVoo(raiz->dir,voo);
    }
}

int *BuscaDeR(Agenda *raiz, int id,Data nova){

//Busca agenda editada
    Data *aux;
    *aux = nova;

    if (raiz != NULL) {
        if (raiz->reserva->data_viagem == aux){
            if (raiz->reserva->passageiro->id == id){
                return 1;
            }
        }

        int checagemData;
        Data inicial;
        inicial = *raiz->reserva->data_viagem;

        checagemData  = checaData(nova,inicial);


        if (checagemData == 0) {
            return BuscaDer(raiz->esq,id, nova);
        } else {
            return BuscaDer(raiz->dir,id, nova);
        }
    }
    return NULL;
}
/*=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==
//=-=-=-=-=-=-=-=-=-=-=-=Funções para usar Árvore Binária =-=-==-=-=-=-=-=-=
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-*/
Agenda *Edita(Agenda *raiz, int codEditar){
    Agenda *edita;
    edita = BuscaCodigo(raiz,codEditar);

    printf("Qual campo deseja editar? \n");
    printf("1- Data \n");
    printf("2- Passageiro \n");
    printf("3- Assento \n");
    printf("4- Voo \n");
    int opc;
    scanf("%d",&opc);

    if (opc = 1){
        edita->reserva->data_viagem = cadastrar_data(edita->reserva);
    }
    if (opc = 2){
        edita->reserva->passageiro = cadastrar_passageiro(edita->reserva);
    }
    if (opc = 3){
        edita->reserva->assento = cadastrar_assento(edita->reserva);
    }
    if (opc = 4){
        edita->reserva->voo = cadastrar_voo(edita->reserva);
    }
    removeCodigo(raiz,codEditar);
    InsereAgenda(raiz, edita);
}

/*Preenche os dados de uma nova Reserva*/

Reserva *PreencheReserva(){
    Reserva *fill;

    cadastrar_data(fill);
    cadastrar_passageiro(fill);
    cadastrar_assento(fill);
    cadastrar_voo(fill);

    return fill;
}


/*Funções|métodos auxiliares para manipular as tads da Reserva*/
Reserva *cadastrar_data(Reserva* reserva){
    Data* data = (Data*)malloc(sizeof(Data));

    printf("Informe o dia da viagem:");
    scanf("%i", &data->dia);
    fflush(stdin);

    printf("Informe o mes da viagem:");
    scanf("%i", &data->mes);
    fflush(stdin);
    
    printf("Informe o ano da viagem:");
    scanf("%i", &data->ano);
    fflush(stdin);

    reserva->data_viagem = data;
    return reserva;
}

char *alocar_char(int tam){
    char *str = (char*)(malloc(sizeof(char)*tam));
    return str;
}

Reserva *cadastrar_passageiro(Reserva *reserva){
    Passageiro *passageiro = (Passageiro*)malloc(sizeof(Passageiro));
    passageiro->nome = alocar_char(50);
    passageiro->endereco = alocar_char(50);

    printf("Informe o id do passageiro: \n");
    scanf("%d", &passageiro->id);
    fflush(stdin);

    printf("Informe o nome do passageiro: \n");
    gets(passageiro->nome);
    fflush(stdin);

    printf("Informe o endereco do passageiro: \n");
    gets(passageiro->endereco);
    fflush(stdin);

    reserva->passageiro = passageiro;
    return reserva;
}

Reserva *cadastrar_voo(Reserva *reserva){
    Voo *voo = (Voo*)malloc(sizeof(Voo));
    voo->origem = alocar_char(50);
    voo->destino = alocar_char(50);

    printf("Informe o codigo do voo: \n");
    scanf("%d", &voo->codigo);
    fflush(stdin);

    printf("Informe a origem do voo: \n");
    gets(voo->origem);
    fflush(stdin);

    printf("Informe a destino do voo: \n");
    gets(voo->destino);
    fflush(stdin);

    reserva->voo = voo;
    return reserva;
}

Reserva *cadastrar_assento(Reserva *reserva){
    Assento novo_assento;
    Assento *assento_aux = (Assento*)malloc(sizeof(Assento));
    printf("Informe o num do assento 0 a 30: \n");
    scanf("%d", assento_aux);
    
    for(novo_assento = A0; novo_assento<=C9; novo_assento++){
        if(novo_assento == *assento_aux){
            printf("Assento: %d\n", novo_assento);
            reserva->assento = *assento_aux;
        }
    } 
    return reserva;
}

/*=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==
//=-=-=-=-=-=-=-=-=-=-=-=Implementação de tabela hash =-=-==-=-=-=-=-=-=
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-*/
struct reserva{
    int codigo;
    Data *data_viagem;
    Passageiro *passageiro;
    Voo *voo;
    Assento assento;
};

struct no{
    Reserva reserva;
    No *proximo;
};

struct trecho{ //Lista encadeada de Reservas.
    No *inicio;
    int tam;
};

//Tabela_hash definida globalmente.
Trecho *tabela_hash[TAM];

/*Funções|métodos auxiliares para manipular as tads da Reserva*/
void cadastrar_data(Reserva* reserva){
    Data* data = (Data*)malloc(sizeof(Data));

    printf("Informe o dia da viagem:");
    scanf("%i", &data->dia);
    fflush(stdin);

    printf("Informe o mes da viagem:");
    scanf("%i", &data->mes);
    fflush(stdin);
    
    printf("Informe o ano da viagem:");
    scanf("%i", &data->ano);
    fflush(stdin);

    reserva->data_viagem = data;
}

char *alocar_char(int tam){
    char *str = (char*)(malloc(sizeof(char)*tam));
    return str;
}

void cadastrar_passageiro(Reserva *reserva){
    Passageiro *passageiro = (Passageiro*)malloc(sizeof(Passageiro));
    passageiro->nome = alocar_char(50);
    passageiro->endereco = alocar_char(50);

    printf("Informe o id do passageiro: \n");
    scanf("%d", &passageiro->id);
    fflush(stdin);

    printf("Informe o nome do passageiro: \n");
    gets(passageiro->nome);
    fflush(stdin);

    printf("Informe o endereco do passageiro: \n");
    gets(passageiro->endereco);
    fflush(stdin);

    reserva->passageiro = passageiro;
}

void cadastrar_voo(Reserva *reserva){
    Voo *voo = (Voo*)malloc(sizeof(Voo));
    voo->origem = alocar_char(50);
    voo->destino = alocar_char(50);

    printf("Informe o codigo do voo: \n");
    scanf("%d", &voo->codigo);
    fflush(stdin);

    printf("Informe a origem do voo: \n");
    gets(voo->origem);
    fflush(stdin);

    printf("Informe a destino do voo: \n");
    gets(voo->destino);
    fflush(stdin);

    reserva->voo = voo;
}

void cadastrar_assento(Reserva *reserva){
    Assento novo_assento;
    Assento *assento_aux = (Assento*)malloc(sizeof(Assento));
    printf("Informe o num do assento 0 a 30: \n");
    scanf("%d", assento_aux);
    
    for(novo_assento = A0; novo_assento<=C9; novo_assento++){
        if(novo_assento == *assento_aux){
            printf("Assento: %d\n", novo_assento);
            reserva->assento = *assento_aux;
        }
    } 
}

void imprimir_data(Data *data){
    printf("\t  * Data: \n");
    printf("\t\t %i / %i / %i\n", data->dia, data->mes, data->ano);
}

void imprimir_passageiro(Passageiro *passageiro){
    printf("\t  * Pasageiro: \n");
    printf("\t\t nome: %s\n", passageiro->nome);
    printf("\t\t endereco: %s\n", passageiro->endereco);
    printf("\t\t id: %d\n", passageiro->id);
}

void imprimir_voo(Voo *voo){
    printf("\t  * Voo: \n");
    printf("\t\t codigo: %d\n", voo->codigo);
    printf("\t\t origem: %s\n", voo->origem);
    printf("\t\t destino: %s\n", voo->destino);
}

/*Funções|métodos para manipular a tad Reserva*/
Reserva criar_reserva(){ 
    Reserva nova_reserva;
    printf("Informe o codigo da reserva: \n");
    scanf("%d", &nova_reserva.codigo);
    
    cadastrar_data(&nova_reserva);
    cadastrar_passageiro(&nova_reserva);
    cadastrar_voo(&nova_reserva); 
    cadastrar_assento(&nova_reserva);
    
    return nova_reserva;
}

Reserva editar_reserva(int id_passageiro, int codigo_reserva){
    deletar_reserva_no_trecho(id_passageiro, codigo_reserva);
    Reserva nova_reserva;
    nova_reserva.codigo = codigo_reserva;

    cadastrar_data(&nova_reserva);
    cadastrar_passageiro(&nova_reserva);
    cadastrar_voo(&nova_reserva); 
    cadastrar_assento(&nova_reserva);
    
    return nova_reserva;
}

void imprimir_reserva(Reserva r){
    printf("\t<----------Reserva---------->\n");
    printf("\t * Codigo da reserva: %d\t\n", r.codigo);
    imprimir_data(r.data_viagem);
    imprimir_passageiro(r.passageiro);
    imprimir_voo(r.voo);
    printf("\t * Assento: %d\t\n", r.assento);
    printf("\t<--------------------------->\n");
}

//Cria uma lista de encadeada de Reservas (Trecho)
Trecho *criar_trecho(){
    Trecho *novo_trecho = (Trecho*)malloc(sizeof(Trecho));
    novo_trecho->inicio = NULL;
    novo_trecho->tam = 0;
    return novo_trecho;
}

//Insere uma reserva na lista encadeada de reservas (Trechos)
void inserir_reserva_no_trecho(Reserva reserva, Trecho *trecho){
    No *no = (No*) malloc(sizeof(No));
    no->reserva = reserva;
    no->proximo = trecho->inicio;
    trecho->inicio = no;
    trecho->tam++;
}

void deletar_reserva_no_trecho(int id, int codigo_reserva){
    int hash(int id_passageiro, int codigo_reserva);
    int indice = hash(id,codigo_reserva);
    No** atual = &tabela_hash[indice]->inicio;
    while((*atual) != NULL)
    {
        if ((*atual)->reserva.codigo == codigo_reserva)
        {
            No *no = *atual;
            *atual = (*atual)->proximo;
            free(no);
            tabela_hash[indice]->tam--;
            break;
        }
        atual = &(*atual)->proximo;
    }
}

No* buscar_reserva(int codigo, No *inicio){
    while(inicio != NULL){
        if(inicio->reserva.codigo == codigo)
            return inicio;
        else    
            inicio = inicio->proximo;
    }
    return NULL;
}

void imprimir_trecho(No *inicio){
    while(inicio != NULL) {
        imprimir_reserva(inicio->reserva);
        inicio = inicio->proximo;
    }
}

/*Funções|métodos para manipular a tabela hash*/
void inicializar_tabela_hash(){
    int i;
    for(i = 0; i < TAM; i++)
        tabela_hash[i] = criar_trecho();
}

//Função de hash
int hash(int id_passageiro, int codigo_reserva){
    return (id_passageiro+codigo_reserva) % TAM;
}

//Cria uma reserva e insere no trecho
void inserir_trecho_na_tabela(){
    Reserva nova_reserva = criar_reserva();
    int indice = hash(nova_reserva.passageiro->id, nova_reserva.codigo);
    inserir_reserva_no_trecho(nova_reserva, tabela_hash[indice]);
}

void editar_reserva_no_trecho(int id_passageiro, int codigo_reserva){
    Reserva nova_reserva = editar_reserva(id_passageiro, codigo_reserva);
    int indice = hash(nova_reserva.passageiro->id, nova_reserva.codigo);
    inserir_reserva_no_trecho(nova_reserva, tabela_hash[indice]);
}

//Busca por uma pessoa na tabela_hash.
Reserva *buscar_reserva_na_tabela_hash(int id_passageiro, int codigo_reserva){
    int indice = hash(id_passageiro, codigo_reserva);
    No *no = buscar_reserva(codigo_reserva, tabela_hash[indice]->inicio);
    if(no)
        return &no->reserva;
    else
        return NULL;
}

// imprimir tabela
void imprimir_tabela_hash(){
    int i;
    printf("\n---------------------VIAGENS-------------------------\n");
    for(i = 0; i < TAM; i++){
        printf("Trecho [%d] Reservas: %d\n", i, tabela_hash[i]->tam);
        imprimir_trecho(tabela_hash[i]->inicio);
    }
    printf("---------------------FIM TABELA-----------------------\n\n");
}
