'''A company decides to apply discounts on its prices using the following table. Create a program that receives the current price of a product and its code, calculates and shows the discount amount and the new price.
CURRENT PRICE              |DISCOUNT %
Up to R$ 30.00            |No discount
Between R$ 30.00 and R$ 100.00 |10%
Above R$ 100.00           |15%'''

# My signature 
print("=+"*28,"\n"," "*20, "ALB System","\n","=+"*28,"\n")

value, code = input("Enter the value of the product and its code: ").split(" ")

value = float(value)

discount = 0
if 30 < value < 100:
    new_value = value * 0.9
    discount = value - new_value
elif value >= 100:
    new_value = value * 0.85
    discount = value - new_value

print(f"The product {code} will have a discount of R${discount:.2f} and a new price of R${new_value:.2f}")
