'''Write a program that receives the average temperature for each month of the year and stores them in a vector. O
The program should calculate and display the highest and lowest temperatures of the year, along with the month in which they
occurred (the month must be shown in full: 1 = January; 2 = February; ...).
Observation
Don't worry about draws. Each calculation must be performed and displayed in a subroutine.'''

# My signature
print("=+" * 28, "\n", " " * 20, "ALB System", "\n", "=+" * 28, "\n")

def month_name(month):
    month_names = [
        "January", "February", "March", "April",
        "May", "June", "July", "August",
        "September", "October", "November", "December"
    ]
    return month_names[month - 1]

def highest_temperature(temperatures):
    max_temp = max(temperatures)
    max_month = temperatures.index(max_temp) + 1
    return max_temp, max_month

def lowest_temperature(temperatures):
    min_temp = min(temperatures)
    min_month = temperatures.index(min_temp) + 1
    return min_temp, min_month

# Receive input from the user
temperatures = []
for month in range(1, 13):
    temp = float(input(f"Enter the average temperature for {month_name(month)}: "))
    temperatures.append(temp)

# Calculate and display highest temperature
max_temp, max_month = highest_temperature(temperatures)
print(f"\nThe highest temperature of {max_temp}°C occurred in {month_name(max_month)}.")

# Calculate and display lowest temperature
min_temp, min_month = lowest_temperature(temperatures)
print(f"The lowest temperature of {min_temp}°C occurred in {month_name(min_month)}.")
