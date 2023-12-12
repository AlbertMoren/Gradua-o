'''Create a program that receives the amount of money in Brazilian reais that a person who is going to travel has. She will visit several countries and needs to convert her money into dollars, German marks, and British pounds. It is known that the exchange rate is $1.80 for one dollar, $2.00 for one German mark, and $3.57 for one British pound. The program should perform the conversions and display them.'''

# My signature
print("=+"*28, "\n", " "*20, "ALB System", "\n", "=+"*28, "\n")

# Receive the amount in Brazilian reais
brazilian_reais = float(input("Enter the amount: R$"))

# Perform currency conversions
us_dollars = brazilian_reais / 1.80
german_marks = brazilian_reais / 2.00
british_pounds = brazilian_reais / 3.57

# Display the results
print(f"In dollars, it is ${us_dollars:.2f}")
print(f"In German marks, it is DM {german_marks:.2f}")
print(f"In British pounds, it is £{british_pounds:.2f}")
