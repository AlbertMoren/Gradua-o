# Receive the names and prices of five products. Calculate and display:
# - the quantity of products with a price lower than R$ 50.00;
# - the names of products with a price between R$ 50.00 and R$ 100.00;
# - the average price of products with a price higher than R$ 100.00.

# My signature
print("=+"*28, "\n", " "*20, "ALB System", "\n", "=+"*28, "\n")

product_names = []
product_prices = []

# Receive names and prices of products
for i in range(5):
    name = input(f"Enter the name of product {i+1}: ")
    price = float(input(f"Enter the price of {name}: "))
    product_names.append(name)
    product_prices.append(price)

# Calculate and display the requested information
lower_than_50 = sum(1 for price in product_prices if price < 50)
between_50_and_100 = [product_names[i] for i, price in enumerate(product_prices) if 50 <= price <= 100]
above_100_prices = [price for price in product_prices if price > 100]

# Display the results
print(f"\nQuantity of products with a price lower than R$ 50.00: {lower_than_50}")
print(f"Products with a price between R$ 50.00 and R$ 100.00: {', '.join(between_50_and_100)}")
if above_100_prices:
    average_price_above_100 = sum(above_100_prices) / len(above_100_prices)
    print(f"Average price of products with a price above R$ 100.00: R$ {average_price_above_100:.2f}")
else:
    print("No products with a price above R$ 100.00.")
