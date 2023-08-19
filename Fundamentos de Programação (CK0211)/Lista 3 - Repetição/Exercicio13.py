'''Faça um programa que receba a idade e o peso de quinze pessoas, e que calcule e mostre as médias dos pesos das pessoas da mesma faixa etária. As faixas etárias são: de 1 a 10 anos, de 11 a 20 anos, de 21 a 30 anos e de 31 anos para cima.'''

#minha assinatura 
print("=+"*28,"\n"," "*20, "ALB System","\n","=+"*28,"\n")

trackOne = 0
trackTwo = 0
trackThree = 0
trackFour = 0
counterOne = 0
counterTwo = 0
counterThree = 0
counterFour = 0

for i in range(15):
    age = int(input("Enter age: "))
    weight = float(input("Enter your weight: "))
    if(age <= 10):
        trackOne+=weight
        counterOne+=1
    elif(age > 10 and age<=20):
        trackTwo+=weight
        counterTwo+=1
    elif(age > 20 and age<=30):
        trackThree+=weight
        counterThree+=1
    else:
        trackFour+=weight
        counterFour+=1

print(f"track one has an everage of {trackOne/counterOne}")
print(f"track two has an everage of {trackTwo/counterTwo}")
print(f"track Three has an everage of {trackThree/counterThree}")
print(f"track Four has an everage of {trackFour/counterFour}")