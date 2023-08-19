'''Uma empresa fez uma pesquisa de mercado para saber se as pessoas gostaram ou não de um novo produto lançado. Para isso, forneceu o sexo do entrevistado e sua resposta (S — sim; ou N — não). Sabe-se que foram entrevistadas dez pessoas. Faça um programa que calcule e mostre:
■ o número de pessoas que responderam sim;
■ o número de pessoas que responderam não;
■ o número de mulheres que responderam sim; e
■ a percentagem de homens que responderam não, entre todos os homens analisados.'''

#minha assinatura 
print("=+"*28,"\n"," "*20, "ALB System","\n","=+"*28,"\n")

opnionYes = 0
opnionNo = 0
opnionWomans = 0
opnionMen = 0
mens = 0
for i in range(10):
    sex = input("Enter your gender[M/F]: ")
    opnion = input("Your interest[S/N]: ")
    if opnion == 'S':
        opnionYes += 1
        if sex == 'F':
            opnionWomans += 1
    elif opnion == 'N':
        opnionNo += 1
        if sex == 'M':
            opnionMen += 1
    if sex == 'M':
        mens+=1

print(f"the number of people who answered yes is {opnionYes}")
print(f"the number of people who answered no is {opnionNo}")
print(f"the number of women who answered yes is {opnionWomans}")
print(f"the percentage of men who answered no is {mens/opnionMen:.2f}")
