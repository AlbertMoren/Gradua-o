'''A store uses code V for cash transactions and P for credit transactions. Create a program that receives the code and the value of fifteen transactions, calculates and shows:
■ the total value of cash purchases;
■ the total value of credit purchases;
■ the overall total value of purchases; and
■ the value of the first installment of all credit purchases, knowing that they will be paid in three installments.'''

# My signature
print("=+"*28, "\n", " "*20, "ALB System", "\n", "=+"*28, "\n") 

total_cash = 0
total_credit = 0
total_general = 0
total_credit_installments = 0

for i in range(15):
    transaction_type = input("Transaction type (V for cash, P for credit): ")
    value = float(input("Enter the transaction value: "))

    if transaction_type == 'V':
        total_cash += value
    elif transaction_type == 'P':
        total_credit += value
        total_credit_installments += value / 3

    total_general += value

print(f"Total value of cash transactions: ${total_cash:.2f}")
print(f"Total value of credit transactions: ${total_credit:.2f}")
print(f"Overall total value of transactions: ${total_general:.2f}")
print(f"Total value of the first installment of all credit transactions: ${total_credit_installments:.2f}")
