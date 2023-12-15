'''Create a program that receives a temperature in Celsius, calculates, and shows that temperature in Fahrenheit. It is known that F = 180*(C + 32)/100'''

# My signature
print("=+"*28,"\n"," "*20, "ALB System","\n","=+"*28,"\n")

celsius = float(input("What is the temperature in Celsius: "))

fahrenheit = 180 * (celsius + 32) / 100

print(f"The temperature in Fahrenheit = {fahrenheit}")
