''' Uma agência bancária possui vários clientes que podem fazer investimentos com rendimentos mensais, conforme a tabela a seguir:
1 Poupança 1,5%
2 Poupança plus 2%
3 Fundos de renda fixa 4%
Faça um programa que leia o código do cliente, o tipo do investimento e o valor investido, e que calcule e mostre o rendimento mensal de acordo com o tipo do investimento. No final, o programa deverá mostrar o total investido e o total de juros pagos.
A leitura terminará quando o código do cliente digitado for menor ou igual a 0.'''

total_invested = 0
total_interest = 0

while True:
    code = int(input("Enter your code: "))
    
    if code <= 0:
        break
    
    typeInvestment = int(input("Enter your investment type (1 for Savings, 2 for Savings Plus, 3 for Fixed Income Funds): "))
    value = float(input("Enter the amount invested: "))
    
    interest_rate = 0
    
    if typeInvestment == 1:
        interest_rate = 0.015  # 1.5%
    elif typeInvestment == 2:
        interest_rate = 0.02   # 2%
    elif typeInvestment == 3:
        interest_rate = 0.04   # 4%
    
    monthly_interest = value * interest_rate
    total_invested += value
    total_interest += monthly_interest
    
    print(f"Monthly interest: {monthly_interest:.2f}")
    
print(f"Total invested: {total_invested:.2f}")
print(f"Total interest paid: {total_interest:.2f}")

