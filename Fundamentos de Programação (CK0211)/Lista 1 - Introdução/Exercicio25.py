'''Faça um programa que receba uma hora (uma variável para hora e outra para minutos), calcule e mostre:
a) a hora digitada convertida em minutos;
b) o total dos minutos, ou seja, os minutos digitados mais a conversão anterior;
c) o total dos minutos convertidos em segundos'''

#minha assinatura 
print("=+"*28,"\n"," "*20, "ALB System","\n","=+"*28,"\n")

hour, minute = input(" Insert hours and minutes: ").split(":")

hour = float(hour)
minute = float(minute)

newMinute = hour*60
minute = minute + newMinute
segunds = minute * 60

print(f" The hour convert to minuite is {newMinute}")
print(f" the total in minutes is {minute}")
print(f" The total in segunds is {segunds}")