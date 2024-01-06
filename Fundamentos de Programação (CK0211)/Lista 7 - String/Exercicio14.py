'''Write a program that takes a sentence and converts the vowels in its words to uppercase and the consonants to lowercase'''

# My signature 
print("=+" * 28, "\n", " " * 20, "ALB System", "\n", "=+" * 28, "\n")

def convertPhrase(phrase):
    vowels = ['a','e','i','o','u']
    newPhrase = ''
    for  letter in phrase:
        if letter in vowels:
            newPhrase += letter.upper()
        else:
            newPhrase += letter.lower()
    print(newPhrase)

phrase = input("Insert a phrase: ")
convertPhrase(phrase)

