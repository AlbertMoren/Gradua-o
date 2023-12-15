'''Create a program that receives the price of a product, calculates and shows, according to the following tables, the new price and classification'''

# My signature 
print("=+"*28,"\n"," "*20, "ALB System","\n","=+"*28,"\n")

# Receive the product value
value = float(input("Enter product value: R$"))

# Calculate the new price based on the provided conditions
if value <= 50.00:
    value *= 1.05
elif 50.00 < value <= 100.00:
    value *= 1.10
else:
    value *= 1.15

# Classify the product based on the new price
if value <= 80:
    classification = "cheap"
elif 80.00 < value <= 120.00:
    classification = "Normal"
elif 120.00 < value <= 200.00:
    classification = "Dear"
else:
    classification = "Very expensive"

# Display the result
print(f"The product will cost R${value:.2f}, and the rating is {classification}")
