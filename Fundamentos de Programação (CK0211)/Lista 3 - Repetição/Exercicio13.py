'''Create a program that receives the age and weight of fifteen people and calculates and shows the average weights of people in the same age group. The age groups are: from 1 to 10 years, from 11 to 20 years, from 21 to 30 years, and 31 years and older.'''

# My signature
print("=+"*28, "\n", " "*20, "ALB System", "\n", "=+"*28, "\n")

trackOne = 0
trackTwo = 0
trackThree = 0
trackFour = 0
counterOne = 0
counterTwo = 0
counterThree = 0
counterFour = 0

for i in range(15):
    age = int(input("Enter age: "))
    weight = float(input("Enter your weight: "))
    if age <= 10:
        trackOne += weight
        counterOne += 1
    elif 10 < age <= 20:
        trackTwo += weight
        counterTwo += 1
    elif 20 < age <= 30:
        trackThree += weight
        counterThree += 1
    else:
        trackFour += weight
        counterFour += 1

print(f"Track one has an average weight of {trackOne/counterOne}")
print(f"Track two has an average weight of {trackTwo/counterTwo}")
print(f"Track Three has an average weight of {trackThree/counterThree}")
print(f"Track Four has an average weight of {trackFour/counterFour}")
