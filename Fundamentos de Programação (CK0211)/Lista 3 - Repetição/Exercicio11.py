'''Faça um programa que receba o valor de um carro e mostre uma tabela com os seguintes dados: preço final, quantidade de parcelas e valor da parcela. Considere o seguinte:
■ o preço final para compra à vista tem desconto de 20%;
■ a quantidade de parcelas pode ser: 6, 12, 18, 24, 30, 36, 42, 48, 54 e 60; e
■ os percentuais de acréscimo encontram-se na tabela a seguir.'''

#minha assinatura 
print("=+"*28,"\n"," "*20, "ALB System","\n","=+"*28,"\n")

value = float(input("Enter car value: "))

j = 0
print("final value | Number of istallmentes | value of installments ")
for i in range(10):
    if i == 0:
        installments = value * 0.8
    else:
        j+= 6
        installments = (value * 1.03) / j
    print("||")