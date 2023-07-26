'''Uma loja utiliza o código V para transação à vista e P para transação a prazo. Faça um programa que receba o código e o valor de quinze transações, calcule e mostre:
■ o valor total das compras à vista;
■ o valor total das compras a prazo;
■ o valor total das compras efetuadas; e
■ o valor da primeira prestação das compras a prazo juntas, sabendo-se que serão pagas em três vezes.'''

#minha assinatura 
print("=+"*28,"\n"," "*20, "ALB System","\n","=+"*28,"\n") 

total_avista = 0
total_aprazo = 0
total_geral = 0
total_dos_prazos = 0
for i in range(3):
    tipo = input("Tipo de transação: V ou P: ")
    valor = float(input("Qual o valor da compra? "))
    if(tipo == 'V'):
        total_avista+=valor
    else:
        total_aprazo+=valor
        total_dos_prazos+=(valor/3)
    total_geral+= valor
print(f"Total de compra a vista é R${total_avista:.2f}\nTotal de compra a prazo é R${total_aprazo:.2f}\nTotal de geral é de R${total_geral:.2f}\nTotal das primeiras parcelas de cada compra a prazo é de R${total_dos_prazos:.2f}")