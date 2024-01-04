'''Write a program that receives a sentence and shows how many times each word appears in the entered sentence'''

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



