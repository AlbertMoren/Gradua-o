'''Cada espectador de um cinema respondeu a um questionário no qual constava sua idade e sua opinião em relação ao filme: ótimo — 3; bom — 2; regular — 1. Faça um programa que receba a idade e a opinião de quinze espectadores, calcule e mostre:
■ a média das idades das pessoas que responderam ótimo;
■ a quantidade de pessoas que responderam regular; e
■ a percentagem de pessoas que responderam bom, entre todos os espectadores analisados.'''

#minha assinatura 
print("=+"*28,"\n"," "*20, "ALB System","\n","=+"*28,"\n")

counterOpnion = 0
ages = 0
counterNormal = 0
counterGood = 0
for i in range(15):
    age = int(input("Enter age: "))
    opnion = float(input("Enter your opnion[1/2/3]: "))
    if opnion == 3:
        counterOpnion+=1
        ages+= age
    if opnion == 1:
        counterNormal+=1
    if opnion == 2:
        counterGood+=1
        
print(f"the average age of people who answered great is {ages/counterOpnion:.2f}")
print(f"the number of people who answered regular is {counterNormal}")
print(f"the percentage of people who answered good is {counterGood/15:.2f}")