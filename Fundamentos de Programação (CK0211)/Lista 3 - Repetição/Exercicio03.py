'''Create a program that receives the age of eight people, calculates and shows:
a) the quantity of people in each age group;
b) the percentage of people in the first age group relative to the total number of people.
c) the percentage of people in the last age group relative to the total number of people.
AGE GROUP       AGE
1st Up to 15 years
2nd From 16 to 30 years
3rd From 31 to 45 years
4th From 46 to 60 years
5th Above 60 years'''

# My signature
print("=+"*28, "\n", " "*20, "ALB System", "\n", "=+"*28, "\n")

group1 = 0
group2 = 0
group3 = 0
group4 = 0
group5 = 0

for i in range(8):
    age = int(input("Age: "))
    if age <= 15:
        group1 += 1
    elif 15 < age <= 30:
        group2 += 1
    elif 30 < age <= 45:
        group3 += 1
    elif 45 < age <= 60:
        group4 += 1
    else:
        group5 += 1

print(f"There are {(group1/8)*100:.0f}% in group 1\nThere are {(group5/8)*100:.0f}% in group 5")
