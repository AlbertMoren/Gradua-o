# Program Description:
# A bank agency has several clients who can make investments with monthly returns,
# according to the following table:
# TYPE | DESCRIPTION           | MONTHLY RETURN
#   1  | Savings               | 1.5%
#   2  | Savings Plus          | 2%
#   3  | Fixed Income Funds    | 4%
#
# This program reads the client code, the type of investment, and the invested amount.
# It calculates and displays the monthly return based on the type of investment.
# Finally, the program shows the total invested and the total interest paid.
# The reading ends when the entered client code is less than or equal to 0.

# Initialize total invested and total interest paid
total_invested = 0
total_interest_paid = 0

# Loop to process user input
while True:
    # Get user input
    client_code = int(input("Enter client code (<= 0 to exit): "))
    
    # Check if the reading should end
    if client_code <= 0:
        break

    investment_type = int(input("Enter investment type (1-3): "))
    invested_amount = float(input("Enter invested amount: "))

    # Calculate monthly return based on the investment type
    if investment_type == 1:
        monthly_return = invested_amount * 0.015
    elif investment_type == 2:
        monthly_return = invested_amount * 0.02
    elif investment_type == 3:
        monthly_return = invested_amount * 0.04
    else:
        print("Invalid investment type. Skipping this investment.")
        continue

    # Update total invested and total interest paid
    total_invested += invested_amount
    total_interest_paid += monthly_return

    # Display the monthly return
    print(f"Monthly return for client {client_code}: {monthly_return:.2f}")

# Display totals at the end
print(f"\nTotal invested: {total_invested:.2f}")
print(f"Total interest paid: {total_interest_paid:.2f}")
