'''Create a program that receives a person's height and gender, and calculates and displays their ideal weight using the following formulas (where h is the height):
■ For men: (72.7 * h) - 58.
■ For women: (62.1 * h) - 44.7.'''

#minha assinatura 
print("=+"*28,"\n"," "*20, "ALB System","\n","=+"*28,"\n")

height = float(input("Enter your height: "))
sex = input("Enter you gender: [M/F] ")

if (sex == "M" or sex == "m"):
    weight = (72.7 * height) - 58
elif(sex == "F" or sex == "f"):
    weight = (62.1 * height) - 44.7

print(f"Your ideal weight is {weight:.2f}")