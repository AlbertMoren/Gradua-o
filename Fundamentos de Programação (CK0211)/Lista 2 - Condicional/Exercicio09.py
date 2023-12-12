'''A bank will grant special credit to its clients based on the average balance in the last year. Create a program that receives the average balance of a client and calculates the credit value according to the following table. Display the average balance and the credit value.
AVERAGE BALANCE      PERCENTAGE
Above R$400.00       30% of the average balance
R$400.00 to R$300.00 25% of the average balance
R$300.00 to R$200.00 20% of the average balance
Up to R$200.00       10% of the average balance
'''

# My signature 
print("=+"*28,"\n"," "*20, "ALB System","\n","=+"*28,"\n")

# Receive the average balance
average_balance = float(input("Enter the client's average balance: R$"))

# Check the average balance range and calculate the credit value accordingly
if average_balance > 400:
    credit_value = average_balance + (average_balance * 0.3)
elif 300 < average_balance <= 400:
    credit_value = average_balance + (average_balance * 0.25)
elif 200 < average_balance <= 300:
    credit_value = average_balance + (average_balance * 0.2)
elif average_balance <= 200:
    credit_value = average_balance + (average_balance * 0.1)

# Display the result
print(f"Your average balance is R${average_balance:.2f} and your credit value is R${credit_value:.2f}")
