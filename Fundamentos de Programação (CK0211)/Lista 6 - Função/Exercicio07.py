'''Write a subroutine that reads an undetermined number of positive values ​​and returns the arithmetic mean of these values. End data entry with the value zero'''

# My signature 
print("=+" * 28, "\n", " " * 20, "ALB System", "\n", "=+" * 28, "\n")

def sub_rotina(numbers):
    average = sum(numbers) / len(numbers)
    return average

numbers = []
while True:
    number = int(input("Enter a value (enter 0 to stop): "))
    if number == 0:
        break
    numbers.append(number)

if numbers:
    avg = sub_rotina(numbers)
    print(f"The average of the entered values is {avg:.1f}")
else:
    print("No values entered.")
