'''Create a program that presents the following options menu:
Options Menu:
1. Arithmetic average
2. Weighted average
3. Exit
Enter the desired option.
For option 1: receive two grades, calculate and show the arithmetic average.
For option 2: receive three grades and their respective weights, calculate and show the weighted average.
For option 3: exit the program.
Check the possibility of an invalid option. In this case, the program should display a message.'''

# My signature 
print("=+"*28, "\n", " "*20, "ALB System", "\n", "=+"*28, "\n")

while True:
    print("1 - Arithmetic average")
    print("2 - Weighted average")
    print("3 - Exit")
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        noteOne = float(input("Enter the first note: "))
        noteTwo = float(input("Enter the second note: "))
        average = (noteOne + noteTwo) / 2
        print(f"The average of these scores is {average:.2f}")
    
    elif choice == 2:
        noteOne = float(input("Enter the first note: "))
        weightOne = int(input("Enter the weight: "))
        noteTwo = float(input("Enter the second note: "))
        weightTwo = int(input("Enter the weight: "))
        noteThree = float(input("Enter the third note: "))
        weightThree = int(input("Enter the weight: "))
        weighted_average = ((noteOne * weightOne) + (noteTwo * weightTwo) + (noteThree * weightThree)) / (weightOne + weightTwo + weightThree)
        print(f"The weighted average of these scores is {weighted_average:.2f}")
    
    elif choice == 3:
        break
    
    else:
        print("Invalid option, please try again.")
