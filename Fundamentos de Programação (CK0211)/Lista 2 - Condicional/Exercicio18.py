'''Create a program that receives a person's age and displays a message indicating whether they are of legal age or not.'''

#minha assinatura 
print("=+"*28,"\n"," "*20, "ALB System","\n","=+"*28,"\n")

age = int(input("Enter your age: "))

if(age >= 18):
    print("You are of legal age")
else:
    print("you are not of legal age")