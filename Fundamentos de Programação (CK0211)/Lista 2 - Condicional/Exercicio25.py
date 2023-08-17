'''Uma empresa decidiu dar uma gratificação de Natal a seus funcionários, baseada no número de horas extras e no número de horas que o funcionário faltou ao trabalho. O valor do prêmio é obtido pela consulta à tabela que se segue, na qual:
H = número de horas extras – (2/3 * (número de horas falta))
H (MINUTOS)     |PRÊMIO (R$)
> = 2.400       |500,00
1.800 e 2.400   |400,00
1.200 e 1.800   |300,00
600  e 1.200    |200,00
< 600           |100,00'''

overtime = int(input("Enter your overtime: "))
hours_left = int(input("Enter your hours left: "))

H = overtime - ((2/3) * (hours_left))

if H >= 2400:
    prize = 500
elif H > 1800 and H < 2400:
    prize = 400
elif H >= 1800 and H < 1800:
    prize = 300
elif H >= 600 and H < 1200:
    prize = 200
else:
    prize = 100

print(f"Your prize will be {prize:.2f}")