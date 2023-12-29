'''Faça um programa que receba uma frase e mostre quantas vezes cada palavra aparece na frase digitada'''

# My signature 
print("=+" * 28, "\n", " " * 20, "ALB System", "\n", "=+" * 28, "\n")

def formatPhrase(text):
    subTexts = text.split(" ")
    contArrays = {}

    for word in subTexts:
        contArrays[word] = contArrays.get(word, 0) + 1

    subTextsAux = list(contArrays.keys())
    return subTextsAux, list(contArrays.values())

def printValues(subTextsAux, contArrays):
    for word, count in zip(subTextsAux, contArrays):
        print(f"The word '{word}' appears {count} time(s)")

text = input("Enter a phrase: ")
subTextsAux, contArrays = formatPhrase(text)
printValues(subTextsAux, contArrays)



