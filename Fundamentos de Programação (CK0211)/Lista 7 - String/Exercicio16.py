'''Write a program that takes a sentence and shows how many letters, how many numbers and how many spaces
there are in it'''

# My signature 
print("=+" * 28, "\n", " " * 20, "ALB System", "\n", "=+" * 28, "\n")

def countLetters(phrase):
    print(f"the amount of letter is {len(phrase.strip())}")

def countNumbers(phrase):
    cont = 0
    for i in range(len(phrase)):
        if phrase[i].isdigit():
            cont += 1
    print(f"the amount of number in phrase is {cont}")

def countSpace(phrase):
    cont = 0
    for i in range(len(phrase)):
        if phrase[i] == " ":
            cont += 1
    print(f"the amount of space in phrase is {cont}")

phrase = input("Insert a phrase: ")
countLetters(phrase)
countNumbers(phrase)
countSpace(phrase)