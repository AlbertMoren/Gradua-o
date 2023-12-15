'''Create a program that receives the value of a car and shows a table with the following data: final price, number of installments, and installment value. Consider the following:
■ The final price for a cash purchase has a 20% discount;
■ The number of installments can be: 6, 12, 18, 24, 30, 36, 42, 48, 54, and 60; and
■ The percentage increases are in the following table.'''

# My signature
print("=+"*28, "\n", " "*20, "ALB System", "\n", "=+"*28, "\n")

value = float(input("Enter car value: "))

j = 0
fees = 1.03
print("final value | Number of installments | Value of installments")
for i in range(11):
    if i == 0:
        final_value = value * 0.8
        installments = 0
    else:
        j += 6
        final_value = value * fees
        installments = final_value / j
        fees += 0.03
    print(f"   R${final_value:.2f}  |          {j}           |       {installments:.2f}   ")
