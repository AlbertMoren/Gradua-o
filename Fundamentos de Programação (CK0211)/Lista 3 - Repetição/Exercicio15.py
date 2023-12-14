'''A company conducted a market survey to find out whether people liked a new product or not. For this, it provided the gender of the interviewee and their response (S — yes; or N — no). It is known that ten people were interviewed. Create a program that calculates and shows:
■ the number of people who answered yes;
■ the number of people who answered no;
■ the number of women who answered yes; and
■ the percentage of men who answered no, among all the men analyzed.'''

# My signature
print("=+"*28, "\n", " "*20, "ALB System", "\n", "=+"*28, "\n")

opinionYes = 0
opinionNo = 0
opinionWomen = 0
opinionMen = 0
menCount = 0

for i in range(10):
    gender = input("Enter your gender [M/F]: ")
    opinion = input("Your interest [S/N]: ")
    if opinion == 'S':
        opinionYes += 1
        if gender == 'F':
            opinionWomen += 1
    elif opinion == 'N':
        opinionNo += 1
        if gender == 'M':
            opinionMen += 1
    if gender == 'M':
        menCount += 1

print(f"The number of people who answered yes is {opinionYes}")
print(f"The number of people who answered no is {opinionNo}")
print(f"The number of women who answered yes is {opinionWomen}")
print(f"The percentage of men who answered no is {opinionMen/menCount*100:.2f}%")
