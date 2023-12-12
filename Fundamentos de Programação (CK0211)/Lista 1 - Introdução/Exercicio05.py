# Program that receives the price of a product, calculates and displays the new price, knowing that it had a discount of 10%.

# My signature
print("=+" * 28, "\n", " " * 20, "ALB System", "\n", "=+" * 28, "\n")

# Input the price of the product
price = float(input("Enter the price of the product: $"))

# Calculate and print the new price after a 10% discount
new_price = price - (price * 0.1)
print(f"The new price is ${new_price}")
