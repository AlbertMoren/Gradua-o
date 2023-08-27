'''Faça um programa que receba o tipo da ação, ou seja, uma letra a ser comercializada na bolsa de valores, o preço de compra e o preço de venda de cada ação e que calcule e mostre:
■ o lucro de cada ação comercializada;
■ a quantidade de ações com lucro superior a R$ 1.000,00;
■ a quantidade de ações com lucro inferior a R$ 200,00;
■ o lucro total da empresa.
Finalize com o tipo de ação ‘F’.'''

#my signature 
print("=+"*28,"\n"," "*20, "ALB System","\n","=+"*28,"\n")

counterUp = 0
counterDown = 0
while True:
    share = input("Enter your share: ")
    if share == "F":
        break
    valueBuy = float(input("Enter the purshase amount: "))
    valueSell = float(input("Enter the sale value: "))
    profit = valueSell - valueBuy
    if profit > 1000:
        counterUp+=1
    if profit < 200:
        counterDown+=1
    print(f"The profit from this action was R${profit:.2f}")