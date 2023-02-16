'''Faça um programa que mostre as tabuadas dos números de 1 a 10.'''

#minha assinatura 
print("=+"*28,"\n"," "*20, "ALB System","\n","=+"*28,"\n") 

for i in range(11):
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    for j in range(11):
        print(f"{i} x {j} = {i*j}")