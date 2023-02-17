## **Universidade Federal do Ceará** |  **Departamento de Computação**
### **Disciplina Fundamentos de Programação (CK0211)** | **Professor: Miguel franklin**

**Trabalho Prático – Jogo da Velha 3D**

Desenvolver um programa em linguagem Python, em modo texto (terminal), representando o jogo da velha
em 3 dimensões (3D), onde um usuário deverá ser capaz de jogar contra o computador. O jogo em 3D difere
do jogo da velha tradicional no fato de ser possível ganhar o jogo se houver uma sequência de 3 símbolos
iguais não só na sequência de linhas, colunas ou diagonais de cada camada do jogo, mas também em
diagonais, linhas e colunas entre as camadas.
Requisitos:
- 1. Cada jogador deverá (usuário/humano e computador), a cada rodada, visualizar a tabela de jogo
atualizada na forma seguinte:

![exemplo](C:\Users\livia\Box\file.png)

- 2. O usuário (jogador 1) deve poder escolher entre jogar com X ou O. Ao computador (jogador 2), será
atribuído o outro símbolo.
- 3. O usuário entrará sua jogada com as coordenadas da casa desejada, sendo na ordem camada, linha e
coluna. (Ex. “1,3,2”, o que equivale à casa da coluna 2, da linha 3 da primeira camada do tabuleiro 3D).
Esta entrada pode ser flexível (Ex. “1, 2, 2” = “1,2,2” = “1, 2, 2), mas a sequência camada, linha
e coluna deve ser respeitada. Toda entrada deverá ser validada (Ex. O computador não deve receber
uma jogada como “1,5,2”. Caso uma entrada do usuário seja inválida, o computador deverá solicitar
nova jogada válida até que o usuário o faça.
- 4. Após a jogada do usuário, o computador deverá fazer a sua jogada, usando a seguinte estratégia (nessa
ordem):
a. Caso haja uma sequência de dois símbolos do computador, em qualquer linha, coluna ou
diagonal, seguida de uma casa vazia, o computador deverá jogar nessa casa, para ganhar a
rodada, fazendo a sequência de três símbolos;
b. Caso não haja situação de vitória iminente do computador, caso haja uma sequência de dois
símbolos do adversário, em qualquer linha, coluna ou diagonal, seguida de uma casa vazia, o
computador deverá jogar nessa casa, para evitar que o usuário ganhe o jogo;
c. Caso não haja situação de vitória iminente do usuário, o computador deve jogar em uma casa
tal que se forme uma sequência de dois símbolos do computador, seguidos de uma casa
vazia, considerando linha, coluna ou diagonal;
d. Caso não haja situação descrita no item (c), o computador deve jogar em qualquer casa de
qualquer linha, coluna ou diagonal onde não haja nenhuma outra casa ocupada (seja por
símbolo do usuário ou do computador);
e. Caso nenhuma das hipóteses anteriores seja plausível, o computador deve jogar em qualquer
casa livre.
- 5. Após a jogada do computador, o usuário deverá realizar a sua nova jogada, seguido pelo computador,
até que algum dos jogadores ganhe o jogo, ou que haja empate.
- 6. O computador deverá, desde quando o programa for executado até o usuário escolher terminar o
programa, guardar o placar entre usuário e computador, contabilizando também os empates. No final
de cada rodada, o computador deverá exibir o placar e perguntar se o usuário deseja jogar novamente.
Se sim, o jogo é recomeçado.