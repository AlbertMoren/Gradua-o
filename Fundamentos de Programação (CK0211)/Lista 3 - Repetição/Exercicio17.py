'''Foi feita uma pesquisa sobre a audiência de canal de TV em várias casas de uma cidade, em determinado dia. Para cada casa consultada foi fornecido o número do canal (4, 5, 7, 12) e o número de pessoas que estavam assistindo àquele canal. Se a televisão estivesse desligada, nada era anotado, ou seja, essa casa não entrava na pesquisa. Faça um programa que:
■ leia um número indeterminado de dados (número do canal e número de pessoas que estavam assistindo); e
■ calcule e mostre a porcentagem de audiência de cada canal. Para encerrar a entrada de dados, digite o número do canal ZERO'''

#minha assinatura 
print("=+"*28,"\n"," "*20, "ALB System","\n","=+"*28,"\n")

counter = 0
counterFour = 0
counterFive = 0
counterSeven = 0
counterTwelve = 0

while True:
    channel = int(input("which channel do you watch[4/5/7/12]? "))
    if channel == 0:
        break
    amount = int(input("how many peoplo watch? "))
    counter+=1
    if channel == 4:
        counterFour+=amount
    elif channel == 5:
        counterFive+=amount
    elif channel == 7:
        counterSeven+=amount
    elif channel == 12:
        counterTwelve+=amount

print(f"the percentage of people who watch channel 4 is {counterFour/counter}\nthe percentage of people who watch channel 5 is {counterFive/counter}\nthe percentage of people who watch channel 7 is {counterSeven/counter}\nthe percentage of people who watch channel 12 is {counterTwelve/counter}")