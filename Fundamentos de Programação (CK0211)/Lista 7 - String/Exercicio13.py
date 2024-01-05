'''Write a program that receives a string of characters and the number of repetitions (limited to 5) and generates a
new chain.
Example:
Chain = Ouch!
Number = 3
New string = Ouch! Ouch! Ouch!'''

def fuctions(phrase,number ):
    number = min(number, 5)
    newPhrase = [phrase] * number
    for word in newPhrase:
        print(word, end=" ")

phrase = input("Insert a phrase: ")
number = int(input("Insert the number of repetitions: "))
fuctions(phrase,number)
