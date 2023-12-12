'''A bank agency has two types of investments, as shown in the table below. Create a program that receives the type of investment and its value, calculates and shows the corrected value after one month of investment, according to the type of investment.
TYPE |DESCRIPTION            |MONTHLY INCOME
1    |Savings               |3%
2    |Fixed income funds    |4%'''

# My signature 
print("=+"*28,"\n"," "*20, "ALB System","\n","=+"*28,"\n")

print("What type of investment? ")
print("1 - Savings")
print("2 - Fixed Income")
investment_type = int(input())
value = float(input("Value: R$"))

if investment_type == 1:
    value *= 1.03
else:
    value *= 1.04

print(f"Your return will be R${value:.2f}")
