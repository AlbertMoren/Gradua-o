#Uma empresa decide dar um aumento de 30% aos funcionários com salários inferiores a R$ 500,00. Faça um
#programa que receba o salário do funcionário e mostre o valor do salário reajustado ou uma mensagem, caso
#ele não tenha direito ao aumento

salario = float(input("Qual o salario: R$"))
if(salario <= 500):
    print(f"Seu novo salário séra de {(salario + (salario*0.3)):.2f}")
else:
    print("Seu tem direito de reajuste")