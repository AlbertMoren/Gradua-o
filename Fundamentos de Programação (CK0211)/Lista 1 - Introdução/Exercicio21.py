'''Faça um programa que receba o número de horas trabalhadas, o valor do salário mínimo e o número
de horas extras trabalhadas, calcule e mostre o salário a receber, de acordo com as regras a seguir:
a) a hora trabalhada vale 1/8 do salário mínimo;
b) a hora extra vale 1/4 do salário mínimo;
c) o salário bruto equivale ao número de horas trabalhadas multiplicado pelo valor da hora trabalhada;
d) a quantia a receber pelas horas extras equivale ao número de horas extras trabalhadas multiplicado pelo valor
da hora extra;
e) o salário a receber equivale ao salário bruto mais a quantia a receber pelas horas extras.'''

#minha assinatura 
print("=+"*28,"\n"," "*20, "ALB System","\n","=+"*28,"\n")

salario = float(input("Informe o salario minimo: "))
horas = float(input("Informe o número de horas trabalhada: "))
extras = float(input("Informe o total de hora extra trabalhada: "))

valor = ((1/8) * salario) * horas
valor = valor + (((1/4)* salario) * extras)

print(f" O salario a ser recebido sera de {valor:.2f}")