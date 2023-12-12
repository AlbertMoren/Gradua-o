# A program that receives a person's year of birth and the current year, calculates and displays:
# a) the person's age in years;
# b) the person's age in months;
# c) the person's age in days;
# d) the person's age in weeks.

# My signature
print("=+" * 28, "\n", " " * 20, "ALB System", "\n", "=+" * 28, "\n")

# Input the year of birth and the current year
year_of_birth = int(input("What is your year of birth? "))
current_year = int(input("What is the current year? "))

# Calculate age in years, months, days, and weeks
years = current_year - year_of_birth
months = years * 12
days = years * 365
weeks = years * 52

# Display the results
print(f"You are {years} years old.")
print(f"You are {months} months old.")
print(f"You are {days} days old.")
print(f"You are {weeks} weeks old.")
