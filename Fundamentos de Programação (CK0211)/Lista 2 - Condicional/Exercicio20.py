'''Create a program that receives a swimmer's age and shows their category using the following rules. For ages below 5, it should display a message.
CATEGORY | AGE
Infantil | 5 to 7
Juvenil | 8 to 10
Adolescente | 11 to 15
Adulto | 16 to 30
Sênior | Over 30'''

#minha assinatura 
print("=+"*28,"\n"," "*20, "ALB System","\n","=+"*28,"\n")

age = int(input("Enter your age: "))

if(age >= 5 and age <= 7):
    print("Your category is children")
elif(age >= 8 and age <= 10):
    print("Your category is young")
elif(age >= 11 and age <= 15):
    print("Your category is adolescent")
elif(age >= 16 and age <= 30):
    print("Your category is adult")
elif(age > 30):
    print("Your category is senior")
else:
    print("you don't fit into any category")