# Fill three arrays with ten positions each: the first array, with the names of ten products; the second array, with the codes of ten products; and the third array, with the prices of the products. 
# Show a report with only the name, code, price, and the new price of the products that will undergo an increase. 
# It is known that the products that will undergo an increase are those that have an even code or a price higher than R$ 1,000.00. 
# It is also known that, for products that satisfy both previous conditions, code and price, the increase will be 20%; for those that satisfy only the code condition, the increase will be 15%; and for those that satisfy only the price condition, the increase will be 10.

# My signature
print("=+"*28,"\n"," "*20, "ALB System","\n","=+"*28,"\n")

product_names = []
product_ids = [0]*3
product_prices = [0]*3
updated_product_names = []
updated_product_ids = []
updated_product_prices = []

for i in range(len(product_ids)):               
    product_ids[i] = int(input("Enter the product ID: "))
    if product_ids[i] in product_ids:   
        flag = 1
        while(flag == 1):
            product_ids[i] = int(input("Enter a valid ID for the product: "))
            if product_ids[i] not in product_ids:
                flag = 0
    product_names.append(input("Enter the product name: "))
    product_prices[i] = float(input("Enter the product price: "))
    if (product_ids[i] % 2 == 0) or (product_prices[i] >= 1000):
        if (product_ids[i] % 2 == 0) and (product_prices[i] >= 1000):
            updated_product_names.append(product_names[i])
            updated_product_ids.append(product_ids[i])
            updated_product_prices.append(product_prices[i] * 1.2)
        if (product_ids[i] % 2 == 0) and (product_prices[i] < 1000):
            updated_product_names.append(product_names[i])
            updated_product_ids.append(product_ids[i])
            updated_product_prices.append(product_prices[i] * 1.15)
        if (product_ids[i] % 2 != 0) and (product_prices[i] >= 1000):
            updated_product_names.append(product_names[i])
            updated_product_ids.append(product_ids[i])
            updated_product_prices.append(product_prices[i] * 1.1)

# Print the products with updated prices
print("\nProducts with updated prices")
for i in range(len(updated_product_ids)):
    print(f"The product {updated_product_names[i]} with ID {updated_product_ids[i]} now has a new price of {updated_product_prices[i]:.2f}")
