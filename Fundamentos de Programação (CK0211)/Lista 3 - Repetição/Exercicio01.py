'''Make a program that reads five groups of four values (A, B, C, D) and displays them in the order they were read. Then, organize them in ascending and descending order.'''

#minha assinatura 
print("=+"*28,"\n"," "*20, "ALB System","\n","=+"*28,"\n")

for i in range(4):
    num1, num2,num3,num4 = input("Enter 4 values: ").split(" ")
    num1 = int(num1)
    num2 = int(num2)
    num3 = int(num3)
    num4 = int(num4)
    print(f"Group {i}\nIn the order read\n{num1}-{num2}-{num3}-{num4}") 
    if(num1 > num2):
        more = num1
        smaller = num2
    else:
        more = num2
        smaller = num1
    if(num3 > num4):
        more1 = num3
        smaller1 = num4
    else:
        more1 = num4
        smaller1 = num3
    if(more < more1):
        aux = more
        more = more1
        more1 = aux
    if(smaller > smaller1):
        aux = smaller
        smaller = smaller1
        smaller1 = aux
    if(more1 < smaller1):
        aux = more1
        more1 = smaller1
        smaller1 = aux
    print(f"In descending order\n{smaller}-{smaller1}-{more1}-{more}\nIn ascending order\n{more}-{more1}-{smaller1}-{smaller}")

        