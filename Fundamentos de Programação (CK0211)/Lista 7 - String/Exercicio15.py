'''Write a program that receives a sentence and, every time a digit between 0 and 9 appears in it, replace it, writing it out.
Example:
Phrase: I'M IN ARMCHAIR 5.
Exit: I'M IN ARMCHAIR FIVE'''

# My signature 
print("=+" * 28, "\n", " " * 20, "ALB System", "\n", "=+" * 28, "\n")

def convertPhrase(phrase):
    numberInFull = ['zero','one','two','three','four','five','six', 'seven', 'eight', 'nine']
    number = ['0','1','2','3','4','5','6','7','8','9']
    phrase = phrase.split(" ")
    newPhrase = ''
    for i in range(len(phrase)):
        for j in range(len(number)):
            if phrase[i] == number[j]:
                phrase[i] = numberInFull[int(number[j])]
        newPhrase += ' ' + phrase[i]
    print(newPhrase.strip())

phrase = input("Insert a phrase: ")
convertPhrase(phrase)