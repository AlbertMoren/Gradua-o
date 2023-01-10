'''Faça um programa que receba um número, calcule e mostre a tabuada desse número'''
number = int(input("Qual tabuada? "))
for i in range(11):
    print(f"{number} x {i} = {number*i}")
