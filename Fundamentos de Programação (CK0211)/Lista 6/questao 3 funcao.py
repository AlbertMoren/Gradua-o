'''Elabore uma sub-rotina que receba dois números como parâmetros e retorne 0, se o primeiro número for divisível pelo segundo número. Caso contrário, deverá retornar o próximo divisor.'''

def sub_rotina(n1,n2):
    
    if n1%n2 == 0:
        return 0
    elif n2 > n1:
        return n1
    else:
        i = n2+1
        while(n1%i!=0):
            i= i+1
        return i
        
            

number1,number2 = input("Insira 2 números: ").split(" ")
number1 = int(number1)
number2 = int(number2)

if(sub_rotina(number1,number2) == 0):
    print(f"{number1} e {number2} são divisiveis entre si")
else:
    print(f"{number1} é divisivel por {sub_rotina(number1,number2)}")