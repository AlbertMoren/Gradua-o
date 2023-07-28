'''Faça um programa que verifique a validade de uma senha fornecida pelo usuário. A senha é 4531. O
programa deve mostrar uma mensagem de permissão de acesso ou não.'''

#minha assinatura 
print("=+"*28,"\n"," "*20, "ALB System","\n","=+"*28,"\n")

senha = input("Enter the password: ")

if(senha == 4531):
    print("Permission grated")
else:
    print("Aceess denied")