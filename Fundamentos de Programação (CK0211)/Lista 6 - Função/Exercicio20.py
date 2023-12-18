'''The city hall of a city carried out a survey among its inhabitants, collecting data on salary and salary. number of children. Write a subroutine that reads this data to an unspecified number of people and return the average salary of the population, the average number of children, the highest salary and the percentage of people with a salary of less than R$380.00'''

# My signature
print("=+" * 28, "\n", " " * 20, "ALB System", "\n", "=+" * 28, "\n")

def inhabitant_survey():
    total_salary = 0
    total_children = 0
    max_salary = float('-inf')
    below_380_count = 0

    while True:
        salary = float(input("Enter the salary of the inhabitant (enter -1 to stop): "))
        if salary == -1:
            break

        children = int(input("Enter the number of children: "))

        total_salary += salary
        total_children += children

        if salary > max_salary:
            max_salary = salary

        if salary < 380:
            below_380_count += 1

    average_salary = total_salary / (below_380_count + 1)  # Adding 1 to avoid division by zero
    average_children = total_children / (below_380_count + 1)

    percentage_below_380 = (below_380_count / (below_380_count + 1)) * 100  # Adding 1 to avoid division by zero

    return average_salary, average_children, max_salary, percentage_below_380

# Call the subroutine
result = inhabitant_survey()

# Display the result
average_salary, average_children, max_salary, percentage_below_380 = result
print("\nSurvey Results:")
print(f"Average Salary: {average_salary:.2f}")
print(f"Average Number of Children: {average_children:.2f}")
print(f"Highest Salary: {max_salary:.2f}")
print(f"Percentage of People with Salary < R$ 380.00: {percentage_below_380:.2f}%")
