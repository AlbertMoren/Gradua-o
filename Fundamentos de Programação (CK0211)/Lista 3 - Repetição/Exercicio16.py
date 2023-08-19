'''Faça um programa que receba várias idades, calcule e mostre a média das idades digitadas. Finalize digitando idade igual a zero.'''

#minha assinatura 
print("=+"*28,"\n"," "*20, "ALB System","\n","=+"*28,"\n")

print("enter 0 to exit")
counterAge = 0
ages = 0
while True:
    age = int(input("Enter your age: "))
    counterAge+=1
    ages += age
    if age == 0:
        break
print(f"the everage age entered is {ages/counterAge:.2f}")
