'''Create a program that receives the age, height, and weight of five people, calculates and shows:
■ the number of people older than 50 years;
■ the average height of people aged between 10 and 20 years;
■ the percentage of people weighing less than 40 kg among all the people analyzed.'''

# My signature
print("=+"*28, "\n", " "*20, "ALB System", "\n", "=+"*28, "\n")

age_over_50 = 0
average_height_10_to_20 = 0.0
weight_less_than_40 = 0

for i in range(5):
    age, height, weight = map(float, input("Enter age, height, and weight separated by space: ").split())

    if age > 50:
        age_over_50 += 1
    if 10 < age < 20:
        average_height_10_to_20 += height
    if weight < 40:
        weight_less_than_40 += 1

average_height_10_to_20 /= 5

print(f"Number of people older than 50: {age_over_50}")
print(f"Average height of people aged between 10 and 20 years: {average_height_10_to_20:.2f}")
print(f"Percentage of people weighing less than 40 kg: {(weight_less_than_40/5)*100:.0f}%")
