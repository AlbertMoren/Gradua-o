# Program Description:
# Create a program to control the stock of goods in a company. Initially, the program should fill two arrays with ten positions each, where the first corresponds to the product code, and the second to the total of that product in stock. Soon after, the program should read an indeterminate set of data containing the customer's code and the product code they want to buy, along with the quantity. A customer code equal to zero indicates the end of the program. The program should check:
# ■ if the requested product code exists. If it does, try to fulfill the request; otherwise, display the message "Code does not exist";
# ■ each order made by a customer can only be fully met. If this is not possible, write the message "We do not have enough stock of this product." If you can attend to it, write the message "Order fulfilled. Thank you and come back often.";
# ■ update the stock only if the order is fully met;
# ■ at the end of the program, write the product codes with their respective updated stocks.

# My signature
print("=+" * 28, "\n", " " * 20, "ALB System", "\n", "=+" * 28, "\n")

# Initialize arrays
codes = []
quantities = []

# Fill the arrays with initial stock data
for i in range(3):
    code, qt = map(int, input("Product code and quantity: ").split())
    codes.append(code)
    quantities.append(qt)

# Process customer orders
customer = 1
while customer != 0:
    customer = int(input("Customer code: "))
    if customer == 0:
        break
    desired_code = int(input("Desired product code: "))
    if desired_code not in codes:
        while desired_code not in codes:
            print("Product does not exist, please enter a valid one.")
            desired_code = int(input("Desired product code: "))

    desired_quantity = int(input("Desired quantity: "))
    for i in range(len(codes)):
        if desired_code == codes[i]:
            if quantities[i] < desired_quantity:
                print("We do not have enough stock of this product.")
            else:
                quantities[i] -= desired_quantity
                print("Order fulfilled. Thank you and come back often.")

# Display updated stocks
for i in range(3):
    print(f"Code {codes[i]} | Quantity {quantities[i]}")
