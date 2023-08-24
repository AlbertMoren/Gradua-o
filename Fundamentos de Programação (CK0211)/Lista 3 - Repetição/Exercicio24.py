'''Faça um programa que receba um conjunto de valores inteiros e positivos, calcule e mostre o maior e o menor valor do conjunto. Considere que:
■ para encerrar a entrada de dados, deve ser digitado o valor zero;
■ para valores negativos, deve ser enviada uma mensagem;
■ os valores negativos ou iguais a zero não entrarão nos cálculos.'''

#my signature 
print("=+"*28,"\n"," "*20, "ALB System","\n","=+"*28,"\n")

highestValue = 0
lowerValue = 0
cont = 0
while True:
    number = int(input("Enter a number: "))
    if number == 0:
        break
    elif number < 0:
        print("This value will be desregarded")
    else:
        if cont == 0:
            highestValue = number
            lowerValue = number
        else:
            if number > highestValue:
                highestValue = number
            if number < lowerValue:
                lowerValue = number
    
print(f"the largest number entered was {highestValue}\nThe smallest number entered was {lowerValue} ")
