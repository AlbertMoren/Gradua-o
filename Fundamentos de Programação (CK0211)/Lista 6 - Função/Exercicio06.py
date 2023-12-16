'''Create a subroutine that receives a person's height (alt) and gender as parameters and returns their ideal weight. For men, you should calculate the ideal weight using the formula: ideal weight = 72.7 *alt − 58; for women: ideal weight = 62.1 *alt − 44.7'''

# My signature 
print("=+" * 28, "\n", " " * 20, "ALB System", "\n", "=+" * 28, "\n")

def calculate_ideal_weight(height, gender):
    if gender.upper() == 'F':
        weight = 72.7 * height - 58
    elif gender.upper() == 'M':
        weight = 62.1 * height - 44.7
    else:
        weight = None  # Invalid gender

    return weight

# Get user input
try:
    height, gender = input("Enter height and gender (M/F): ").split()
    height = float(height)

    ideal_weight = calculate_ideal_weight(height, gender)
    
    if ideal_weight is not None:
        print(f"Your ideal weight is {ideal_weight:.2f} kg.")
    else:
        print("Invalid gender. Please enter 'M' or 'F'.")
except ValueError:
    print("Invalid input. Please enter valid height and gender.")
