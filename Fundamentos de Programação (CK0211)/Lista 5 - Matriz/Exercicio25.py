'''Create a program that:
■ receive the price of ten products and store them in a vector;
■ receive the stocked quantity of each of these products, in five different warehouses, using
a 5 x 10 matrix.
The program should calculate and display:
■ the quantity of products stored in each of the warehouses;
■ the quantity of each product stored in all warehouses together;
■ the price of the product that has the largest stock in a single warehouse;
■ the smallest stock stored;
■ the cost of each warehouse.'''

# My signature
print("=+" * 28, "\n", " " * 20, "ALB System", "\n", "=+" * 28, "\n")

# Function to create a matrix
def create_matrix(n_rows, n_columns, value):
    matrix = []  # empty list
    for i in range(n_rows):
        row = [] 
        for j in range(n_columns):
            row.append(value)		        
        matrix.append(row)	
    return matrix

# Initialize the product prices vector
product_prices = [0] * 10

# Initialize the matrix to store the quantity of products in each warehouse
warehouses_matrix = create_matrix(5, 10, 0)

# Receive the prices of ten products
print("Enter the price for each product:")
for i in range(10):
    product_prices[i] = float(input(f"Product {i + 1}: "))

# Receive the quantity stocked in each warehouse
for i in range(5):
    print(f"\nEnter the quantity stocked in Warehouse {i + 1}:")
    for j in range(10):
        warehouses_matrix[i][j] = int(input(f"Product {j + 1}: "))

# Calculate and display the quantity of products in each warehouse
print("\nQuantity of products in each warehouse:")
for i in range(5):
    total_quantity = sum(warehouses_matrix[i])
    print(f"Warehouse {i + 1}: {total_quantity} products")

# Calculate and display the total quantity of each product in all warehouses
print("\nTotal quantity of each product in all warehouses:")
for j in range(10):
    total_quantity = sum(row[j] for row in warehouses_matrix)
    print(f"Product {j + 1}: {total_quantity} units")

# Find and display the price of the product with the highest stock in a single warehouse
max_stock_product_index = max((max(row), j) for j, row in enumerate(warehouses_matrix))[1]
print(f"\nPrice of the product with the highest stock in a single warehouse (Product {max_stock_product_index + 1}): ${product_prices[max_stock_product_index]:.2f}")

# Find and display the smallest stock across all warehouses
min_stock = min(min(row) for row in warehouses_matrix)
print(f"\nSmallest stock across all warehouses: {min_stock} units")

# Calculate and display the cost of each warehouse
print("\nCost of each warehouse:")
for i in range(5):
    total_cost = sum(quantity * product_prices[j] for j, quantity in enumerate(warehouses_matrix[i]))
    print(f"Warehouse {i + 1}: ${total_cost:.2f}")
