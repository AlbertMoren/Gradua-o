'''Each moviegoer answered a questionnaire that included their age and their opinion about the movie: excellent — 3; good — 2; regular — 1. Create a program that receives the age and opinion of fifteen moviegoers, calculates and shows:
■ the average age of people who answered excellent;
■ the number of people who answered regular; and
■ the percentage of people who answered good, among all the analyzed moviegoers.'''

# My signature
print("=+"*28, "\n", " "*20, "ALB System", "\n", "=+"*28, "\n")

counterOpinion = 0
ages = 0
counterRegular = 0
counterGood = 0

for i in range(15):
    age = int(input("Enter age: "))
    opinion = float(input("Enter your opinion [1/2/3]: "))
    if opinion == 3:
        counterOpinion += 1
        ages += age
    if opinion == 1:
        counterRegular += 1
    if opinion == 2:
        counterGood += 1

print(f"The average age of people who answered excellent is {ages/counterOpinion:.2f}")
print(f"The number of people who answered regular is {counterRegular}")
print(f"The percentage of people who answered good is {counterGood/15*100:.2f}%")
