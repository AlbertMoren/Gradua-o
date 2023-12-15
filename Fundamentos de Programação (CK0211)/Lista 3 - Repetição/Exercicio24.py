# Program Description:
# This program receives a set of positive integer values, calculates and displays the largest and smallest values in the set.
# Considerations:
# - To end the data entry, the value zero must be entered.
# - For negative values, a message should be displayed.
# - Negative values or values equal to zero will not be considered in the calculations.

# Initialize variables to store the largest and smallest values
largest_value = float('-inf')  # Initialize as negative infinity, so any positive value will be larger
smallest_value = float('inf')  # Initialize as positive infinity, so any positive value will be smaller

# Loop to process user input
while True:
    # Get user input
    value = int(input("Enter a positive integer value (enter 0 to finish): "))

    # Check if user wants to finish
    if value == 0:
        break

    # Check if the value is positive
    if value <= 0:
        print("Invalid input. Please enter a positive integer.")
        continue

    # Update largest and smallest values
    largest_value = max(largest_value, value)
    smallest_value = min(smallest_value, value)

# Display the results
if largest_value == float('-inf') and smallest_value == float('inf'):
    print("No valid values entered.")
else:
    print(f"The largest value is: {largest_value}")
    print(f"The smallest value is: {smallest_value}")
