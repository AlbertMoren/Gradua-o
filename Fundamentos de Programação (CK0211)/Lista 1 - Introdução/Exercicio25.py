'''Create a program that receives an hour (one variable for hours and another for minutes), calculates, and displays:
a) the entered hour converted to minutes;
b) the total minutes, i.e., the minutes entered plus the previous conversion;
c) the total minutes converted to seconds'''

# My signature
print("=+"*28,"\n"," "*20, "ALB System","\n","=+"*28,"\n")

# Receive hours and minutes
hour, minute = input("Insert hours and minutes: ").split(":")
hour = float(hour)
minute = float(minute)

# Convert hours to minutes
new_minute = hour * 60
total_minutes = minute + new_minute

# Convert total minutes to seconds
total_seconds = total_minutes * 60

# Display the results
print(f"The hour converted to minutes is {new_minute}")
print(f"The total in minutes is {total_minutes}")
print(f"The total in seconds is {total_seconds}")
