'''*A company decided to give a Christmas bonus to its employees based on the number of overtime hours and the number of hours the employee missed work. The prize value is obtained by consulting the following table, where: H = number of overtime hours – (2/3 * (number of hours absent))
H (MINUTES)     |PRIZE  (R$)
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