'''Faça um programa que receba o valor de um carro e mostre uma tabela com os seguintes dados: preço final, quantidade de parcelas e valor da parcela. Considere o seguinte:
■ o preço final para compra à vista tem desconto de 20%;
■ a quantidade de parcelas pode ser: 6, 12, 18, 24, 30, 36, 42, 48, 54 e 60; e
■ os percentuais de acréscimo encontram-se na tabela a seguir.'''

#minha assinatura 
print("=+"*28,"\n"," "*20, "ALB System","\n","=+"*28,"\n")

value = float(input("Enter car value: "))

j = 0
fees = 1.03
print("final value | Number of istallmentes | value of installments")
for i in range(11):
    if i == 0:
        final_value = value * 0.8
        installments = 0
    else:
        j+= 6
        final_value = value * fees
        installments =  final_value / j
        fees += 0.03
    print(f"   R${final_value:.2f}  |          {j}           |       {installments:.2f}   ")