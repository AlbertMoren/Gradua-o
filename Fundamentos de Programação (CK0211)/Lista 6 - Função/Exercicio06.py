'''Crie uma sub-rotina que receba como parâmetro a altura (alt) e o sexo de uma pessoa e retorne seu peso ideal. Para homens, deverá calcular o peso ideal usando a fórmula: peso ideal = 72.7 *alt − 58; para mulheres: peso ideal = 62.1 *alt − 44.7'''

#minha assinatura 
print("=+"*28,"\n"," "*20, "ALB System","\n","=+"*28,"\n")

def sub_rotina(alt,sexo):
    if sexo == 'F':
        peso = 72.7*alt-58
        return peso
    else:
        peso = 62.1*alt-44.7
        return peso


altura, sexo = input("Informe a altura e o sexo: " ).split(" ")
altura = float(altura)

print(f"Seu peso idela é fe {sub_rotina(altura,sexo):.2f}")