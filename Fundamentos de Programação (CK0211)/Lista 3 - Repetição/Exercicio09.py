'''Create a program that receives ten ages, weights, and heights, calculates and shows:
■ the average age of the ten people;
■ the number of people weighing over 90 kg and measuring less than 1.50 meters; and
■ the percentage of people aged between 10 and 30 among those who are over 1.90 meters tall.'''

# My signature
print("=+"*28,"\n"," "*20, "ALB System","\n","=+"*28,"\n")

count_age = 0
count_height = 0
count_general = 0

for i in range(10):
    age, height, weight = map(float, input("Enter age, height, and weight separated by space: ").split())
    count_age += age

    if weight > 90 and height < 1.5:
        count_height += 1

    if 10 < age < 30 and height > 1.90:
        count_general += 1

average_age = count_age / 10

print(f"The average age is: {average_age:.2f}")
print(f"Number of people weighing over 90 kg and measuring less than 1.50 meters: {count_height}")
print(f"{(count_general/10)*100:.0f}% of people in the third case.")
