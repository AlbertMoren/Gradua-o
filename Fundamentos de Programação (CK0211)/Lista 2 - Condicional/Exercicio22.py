'''Create a program that receives a person's age and weight. According to the following table, check and show which risk group this person fits into.

    AGE     | WEIGHT
| Up to 60  | Between 60 and 90 (inclusive) | Above 90
Less than 20 | 9 | 8 | 7
20 to 50 | 6 | 5 | 4
Over 50 | 3 | 2 | 1'''


#minha assinatura 
print("=+"*28,"\n"," "*20, "ALB System","\n","=+"*28,"\n")

age = int(input("Enter your age: "))
weight = float(input("Enter your weight: "))

if(age <20):
    if(weight <=60):
        risk = 9
    elif(weight >60 and weight<=90):
        risk = 8
    else:
        risk = 7
elif(age >= 20 and age <=50):
    if(weight <=60):
        risk = 6
    elif(weight >60 and weight<=90):
        risk = 5
    else:
        risk = 4
else:
    if(weight <=60):
        risk = 3
    elif(weight >60 and weight<=90):
        risk = 2
    else:
        risk = 1

print(f"Your risk group is {risk}")