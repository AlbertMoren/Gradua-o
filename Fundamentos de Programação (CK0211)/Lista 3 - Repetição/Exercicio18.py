'''A survey was conducted among the inhabitants of a region. Data on age, gender (M/F), and salary were collected. Create a program that calculates and shows:
■ the average salary of the group;
■ the oldest and youngest age in the group;
■ the number of women with a salary up to R$ 200.00;
■ the age and gender of the person with the lowest salary.
Finish the data entry when a negative age is entered.'''

# My signature
print("=+"*28, "\n", " "*20, "ALB System", "\n", "=+"*28, "\n")

counterSalary = 0
minorSex = ''
cont = 0
majorAge = 0
minorAge = 999999
counterWomans = 0

while True:
    age = int(input("Enter your age: "))
    if age < 0:
        break
    sex = input("Enter your gender [M/F]: ")
    salary = float(input("Enter your salary: "))
    
    counterSalary += salary
    cont += 1
    
    if age > majorAge:
        majorAge = age
    if age < minorAge:
        minorAge = age
        minorSex = sex
    
    if sex == 'F' and salary <= 200.00:
        counterWomans += 1

print(f"The average salary of the group is {counterSalary/cont:.2f}")
print(f"The oldest age is {majorAge} and the youngest age is {minorAge}")
print(f"The number of women earning up to R$ 200.00 is {counterWomans}")
print(f"The age and gender of the person with the lowest salary is {minorAge} and {minorSex}")
