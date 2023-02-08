#Faça um programa que calcule e mostre a área de um trapézio.
#Sabe-se que: A = ((base maior + base menor) * altura)/2
base_M, Base_m, altura = input("Valor da base maio, base menor e a altura:").split(" ")
base_M = float(base_M)
Base_m = float(Base_m)
altura = float(altura)
print(f"A área do trapezio é de {((base_M+Base_m)*altura)/2}")