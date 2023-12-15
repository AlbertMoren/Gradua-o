'''Create a program that receives the price, the category (1 — cleaning; 2 — food; or 3 — clothing) and the status (R — products that require refrigeration; and N — products that do not require refrigeration). Calculate and show:'''

#minha assinatura 
print("=+"*28,"\n"," "*20, "ALB System","\n","=+"*28,"\n")

price = float(input("Enter product value: "))
category = input("Choice product category\n1 - cleaning\n2 - food\n3 - clothing\n")
situation = input("Choice product situation\nN - unrefrigerated\nR - chilled\n")

if price <= 25:
    if category == 1:
        discount = price * 0.05
    elif category == 2:
        discount = price * 0.08
    else:
        discount = price * 0.10
else:
    if category == 1:
        discount = price * 0.12
    elif category == 2:
        discount = price * 0.15
    else:
        discount = price * 0.18

if category == 2 and (situation == "R" or situation == "r"):
    price = price - discount + (price * 0.05)
else:
     price = price - discount + (price * 0.08)

if price <= 50:
    new_category = "cheap"
elif price > 50 and price < 120:
    new_category = "normal"
else:
    new_category = "Expensive"

print(f"This product will be {price:.2f} and category '{new_category}'")