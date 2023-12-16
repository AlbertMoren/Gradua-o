'''A survey was carried out among 15 inhabitants of a region. The data collected from each inhabitant
were: age, sex, salary and number of children.
Make a subroutine that reads this data and stores it in vectors. Then, create subroutines that
receive these vectors as parameters and return the average salary among the inhabitants, the lowest and the highest
older age of the group and the number of women with three children who receive up to R$500.00 (use
a subroutine for each calculation)'''

# My signature 
print("=+" * 28, "\n", " " * 20, "ALB System", "\n", "=+" * 28, "\n")

def read_data():
    ages = []
    sexes = []
    salaries = []
    num_children = []

    for _ in range(15):
        age = int(input("Enter age: "))
        sex = input("Enter sex (M/F): ")
        salary = float(input("Enter salary: "))
        children = int(input("Enter number of children: "))

        ages.append(age)
        sexes.append(sex)
        salaries.append(salary)
        num_children.append(children)

    return ages, sexes, salaries, num_children

def average_salary(salaries):
    return sum(salaries) / len(salaries)

def age_extremes(ages):
    return min(ages), max(ages)

def women_with_three_children_and_low_salary(sexes, num_children, salaries):
    count = 0
    for i in range(len(sexes)):
        if sexes[i] == 'F' and num_children[i] == 3 and salaries[i] <= 500.0:
            count += 1
    return count

# Read data from inhabitants
ages, sexes, salaries, num_children = read_data()

# Calculate and display results
avg_salary = average_salary(salaries)
min_age, max_age = age_extremes(ages)
women_count = women_with_three_children_and_low_salary(sexes, num_children, salaries)

print(f"Average salary: {avg_salary:.2f}")
print(f"Lowest age: {min_age}, Highest age: {max_age}")
print(f"Number of women with three children and salary <= R$500.00: {women_count}")
