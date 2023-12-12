'''Create a program that receives:
■ the code of the purchased product; and
■ the quantity purchased of the product.
Calculate and show:
■ the unit price of the purchased product, following Table I;
■ the total price of the invoice;
■ the discount amount, following Table II, applied to the total price of the invoice; and
■ the final price of the invoice after the discount.
'''

#minha assinatura 
print("=+"*28,"\n"," "*20, "ALB System","\n","=+"*28,"\n")

code_product = int(input("Enter the product code: "))
amount = int(input("How many: "))

if code_product > 0 and code_product <= 10:
    price = 10.00
elif code_product > 10 and code_product <= 20:
    price = 15.00
elif code_product > 20 and code_product <= 30:
    price = 15.00
elif code_product > 30 and code_product <= 40:
    price = 15.00

total = price * amount

if total <= 250:
    total = total * 0.95
elif total > 250 and total <= 500:
    total = total * 0.90
else:
    total = total * 0.85

print(f"total note price is {total:.2f}")