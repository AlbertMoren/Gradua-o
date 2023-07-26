'''O preço ao consumidor de um carro novo é a soma do custo de fábrica com a porcentagem do distribuidor e dos impostos, ambos aplicados ao custo de fábrica. As porcentagens encontram-se na tabela a seguir. Faça um programa que receba o custo de fábrica de um carro e mostre o preço ao consumidor. CUSTO DE FÁBRICA % DO DISTRIBUIDOR % dos IMPOSTOS
Até R$ 12.000,00 5 isento
Entre R$ 12.000,00 e R$ 25.000,00 10 15
Acima de R$ 25.000,00 15 20'''

#minha assinatura 
print("=+"*28,"\n"," "*20, "ALB System","\n","=+"*28,"\n")

valor = float(input("Valor do carro: R$"))
if(valor < 12.000):
    print(f"valor do carro séra de {(valor + (valor*0.05))}")
elif(valor := 12.000 and valor <25.000):
    print(f"valor do carro séra de {(valor + (valor*0.1)+ (valor*0.15))}")
else:
    print(f"valor do carro séra de {(valor + (valor*0.15)+ (valor*0.2))}")