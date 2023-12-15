# My signature
print("=+" * 28, "\n", " " * 20, "ALB System", "\n", "=+" * 28, "\n")

# Initialize variables
names = []
total_sales = [0] * 3
commission_percentages = [0] * 3
highest_sale_index = 0
lowest_sale_index = 0

# Input for each salesperson
for i in range(3):
    name = input("Name of the salesperson: ")
    if name in names:
        while name in names:
            name = input("Salesperson already exists in our database, please enter another name: ")
    names.append(name)
    total_sales[i] = float(input("Enter the total sales for the salesperson: "))
    commission_percentages[i] = float(input("Enter the commission percentage for the salesperson: ")) / 100

    # Update indices for highest and lowest sales
    if total_sales[i] > total_sales[highest_sale_index]:
        highest_sale_index = i
    if total_sales[i] < total_sales[lowest_sale_index]:
        lowest_sale_index = i

# Report
print("=" * 5, "REPORT", "=" * 5)
for i in range(len(names)):
    commission = total_sales[i] * commission_percentages[i]
    print(f"Salesperson {names[i]} made ${total_sales[i]:.2f} in sales and earns a commission of ${commission:.2f}")
print(f"Total sales: ${sum(total_sales):.2f}")
print(f"The salesperson {names[highest_sale_index]} made the highest sale of ${total_sales[highest_sale_index]:.2f}")
print(f"The salesperson {names[lowest_sale_index]} made the lowest sale of ${total_sales[lowest_sale_index]:.2f}")
print("=" * 20)
