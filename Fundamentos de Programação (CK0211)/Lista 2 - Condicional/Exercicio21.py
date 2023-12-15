'''Create a program that receives the price of a product and its origin code and shows its origin. The origin follows the table below.

ORIGIN CODE | ORIGIN
1           | South
2           | North
3           | East
4           | West
5 or 6      | Northeast
7 or 8 or 9 | Southeast
10 to 20    | Midwest
21 to 30    | Northeast'''

#minha assinatura 
print("=+"*28,"\n"," "*20, "ALB System","\n","=+"*28,"\n")

price = float(input("Enter product price: "))
code = int(input("Enter the product code:"))

if(code < 5 ):
    if(code == 1):
        print("the process of this product is from south")
    elif(code == 2):
        print("the process of this product is from north")
    elif(code == 3):
        print("the process of this product is from east")
    elif(code == 4):
        print("the process of this product is from west")
else:
    if(code == 5 or code ==6):
        print("the process of this product is from north east")
    elif(code >= 7 and code <=9):
        print("the process of this product is from southeast")
    elif(code >= 10 and code <=20):
        print("the process of this product is from midwest")
    elif(code >= 21 and code <=30):
        print("the process of this product is north east")