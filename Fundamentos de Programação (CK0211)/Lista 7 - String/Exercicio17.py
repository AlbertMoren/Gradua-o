'''Faça um programa que receba uma frase e, a cada duas palavras dela, realize uma criptografia, ou seja:
a primeira letra da primeira palavra da frase concatenada com a última letra da segunda palavra, concatenada com a segunda letra da primeira palavra e com a penúltima letra da segunda palavra e assim por
diante. No caso de quantidade de palavras ímpares, a última palavra deve simplesmente ser invertida.
Exemplos:
Frase: Aula com bola
Saída: Amuolca alob
Frase: Casa com janelas coloridas
Saída: Cmaosca jsaandeilraosloc'''

# My signature 
print("=+" * 28, "\n", " " * 20, "ALB System", "\n", "=+" * 28, "\n")

def encryptPhrase(phrase):
    phrase = phrase.split(" ")
    if len(phrase) % 2 == 0:
        for i in range(len(phrase)):
            

phrase = input("insert a phrase: ")