'''Create a program that receives the age, weight, height, eye color (A — blue; P — black; V — green; and C — brown), and hair color (P — black; C — brown; L — blonde; and R — red) of six people. Calculate and show:
■ the number of people older than 50 years and weighing less than 60 kg;
■ the average age of people with a height less than 1.50 m;
■ the percentage of people with blue eyes among all the people analyzed; and
■ the number of red-haired people who do not have blue eyes.'''

# My signature
print("=+"*28, "\n", " "*20, "ALB System", "\n", "=+"*28, "\n")

count_age_weight = 0
count_age_height = 0
count_blue_eyes = 0
count_red_hair_no_blue_eyes = 0

for i in range(6):
    age, height, weight = map(float, input("Enter age, height, and weight separated by space: ").split())
    eye_color, hair_color = input("Enter eye color (A,P,V,C) and hair color (P,C,L,R) separated by space: ").split()

    if age > 50 and weight < 60:
        count_age_weight += 1
    if height < 1.50:
        count_age_height += age
    if eye_color == 'A':
        count_blue_eyes += 1
    if hair_color == 'R' and eye_color != 'A':
        count_red_hair_no_blue_eyes += 1

average_age_height = count_age_height / 6

print(f"{count_age_weight} people are older than 50 years and weigh less than 60 kg.")
print(f"The average age of people with a height less than 1.50 m: {average_age_height:.2f}")
print(f"{(count_blue_eyes/6)*100:.0f}% of people have blue eyes.")
print(f"{count_red_hair_no_blue_eyes} red-haired people who do not have blue eyes.")
