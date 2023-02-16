'''Faça um programa que receba duas cadeias de caracteres e verifique se a primeira cadeia digitada é permutação da segunda cadeia, ou seja, se todos os caracteres da primeira cadeia estão presentes na segunda cadeia, mesmo que em posições diferentes. Exemplo:
“abccde” é uma permutação de “cbadce”, mas não é de “abcdef” nem de “abcde”'''

#minha assinatura 
print("=+"*28,"\n"," "*20, "ALB System","\n","=+"*28,"\n")

def sub_rotina_comparar(tex1, tex2):
    lista1 = list(tex1)
    lista2 = list(tex2)
    for i in range(len(lista1)):
        if lista1[i] in lista2:
            if i+1 == len(lista1):
                print(f"{tex1} é permutação de {tex2}")
            continue
        else:
            print("Não")
            break
            
#Main
texto1 = input("Insira uma palavra: ").lower()
texto2 = input("Insira uma palavra: ").lower()
sub_rotina_comparar(texto1,texto2)