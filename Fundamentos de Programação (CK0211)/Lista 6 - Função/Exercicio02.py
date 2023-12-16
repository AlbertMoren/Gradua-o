'''Create a subroutine that takes three integers as parameters, representing hours, minutes, and seconds, and converts them to seconds. Example: 2h, 40min and 10s correspond to 9,610 seconds.'''

# My signature
print("=+" * 28, "\n", " " * 20, "ALB System", "\n", "=+" * 28, "\n")

def convert_to_seconds(hours, minutes, seconds):
    total_seconds = (hours * 3600) + (minutes * 60) + seconds
    return total_seconds

user_input = input("Enter hours, minutes, and seconds separated by space: ")
hours, minutes, seconds = map(int, user_input.split())

result_seconds = convert_to_seconds(hours, minutes, seconds)
print(f"The total seconds is: {result_seconds}")
