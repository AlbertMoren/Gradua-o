
typedef struct data Data;
typedef struct voo Voo;
typedef struct lista_voo ListaVoo;
typedef struct passageiro Passageiro;
typedef struct lista_passageiro ListaPassageiro;
typedef struct reserva Reserva;
typedef struct agenda Agenda;
typedef struct viagem Viagem;
typedef struct tabela_viagem TabelaViagem;


/*Implementação da lista de passageiro*/

ListaPassageiro *lista_cria();
int lista_liberar(ListaPassageiro **lista);
int lista_inserir(ListaPassageiro *lista, Passageiro *passageiro);
ListaPassageiro *lista_busca(ListaPassageiro *lista, int ID);
ListaPassageiro *lista_retirar(ListaPassageiro *lista);
int lista_vazia(ListaPassageiro* lista);
Passageiro *lista_primeiro(ListaPassageiro* lista);
int lista_quantidade(ListaPassageiro *lista);

/*Funções para passageiros*/

Passageiro *passageiro_novo(int id, char *nome,char *endereco);
int passageiro_verifica(Passageiro *Passageiro);
int passageiro_igual(Passageiro *passageiro1, Passageiro *passageiro2);
int passageiro_tramanho();
void passageiro_liberar(Passageiro **passageiro);
void passageiro_atribuir(Passageiro *passageiro, int id, char *nome, char *endereco);
void passageiro_acessa(Passageiro *passageiro,int *id, char *nome, char *endereco);


/*Implementação da lista de voos*/

ListaVoo *lista_Voo_cria();
int lista_Voo_liberar(ListaVoo **lista);
int lista_Voo_inserir(ListaVoo *lista, Voo *voo);
ListaVoo *lista_Voo_busca(ListaVoo *lista, int id);
ListaVoo *lista_voo_retirar(ListaVoo *lista);
int lista_Voo_vazia(ListaVoo* lista);
Voo *lista_Voo_primeiro(ListaVoo *lista);
int lista_Voo_quantidade(ListaVoo *lista);

/*Funções para Voos*/


Voo *voo_novo(int codigo, char *origem,char *destino);
void voo_liberar(Voo **voo);
void voo_acessa(Voo *voo,int *codigo, char *origem, char *destino);
void voo_atribuir(Voo *voo, int codigo, char *origem, char *destino);
int voo_igual(Voo *voo1, Voo *voo2);
int voo_tramanho();

//Implementação da árvore binária

Agenda *BuscaAgenda(Agenda *raiz, Data busca);
int checaData(Data anterior, Data nova);
int *BuscaRes(Agenda *raiz, int codigo);
int *BuscaDeR(Agenda *raiz, int id,Data nova);
int BuscaInd(Agenda *raiz, int codigo);
int BuscaVoo(Agenda *raiz, int voo);
int *BuscaRes(Agenda *raiz, int codigo);
int *BuscaDeR(Agenda *raiz, int id,Data nova);

//Funções para acessar a árvore binária
Agenda *Edita(Agenda *raiz, int codEditar);
Reserva *PreencheReserva();
Reserva *cadastrar_data(Reserva* reserva);
char *alocar_char(int tam);
Reserva *cadastrar_passageiro(Reserva *reserva);
Reserva *cadastrar_voo(Reserva *reserva);
Reserva *cadastrar_assento(Reserva *reserva);

//Funções da tabela hash
void cadastrar_data(Reserva* reserva);
char *alocar_char(int tam);
void cadastrar_passageiro(Reserva *reserva);
void cadastrar_voo(Reserva *reserva);
void cadastrar_assento(Reserva *reserva);
void imprimir_data(Data *data);
void imprimir_passageiro(Passageiro *passageiro);
void imprimir_voo(Voo *voo);
Reserva criar_reserva();
Reserva editar_reserva(int id_passageiro, int codigo_reserva);
void imprimir_reserva(Reserva r);
Trecho *criar_trecho();
void inserir_reserva_no_trecho(Reserva reserva, Trecho *trecho);
void deletar_reserva_no_trecho(int id, int codigo_reserva);
No* buscar_reserva(int codigo, No *inicio);
void imprimir_trecho(No *inicio);
void inicializar_tabela_hash();
int hash(int id_passageiro, int codigo_reserva);
void inserir_trecho_na_tabela();
void editar_reserva_no_trecho(int id_passageiro, int codigo_reserva);
Reserva *buscar_reserva_na_tabela_hash(int id_passageiro, int codigo_reserva);
void imprimir_tabela_hash();