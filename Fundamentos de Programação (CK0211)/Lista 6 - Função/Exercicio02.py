'''Crie uma sub-rotina que receba três números inteiros como parâmetros, representando horas, minutos e segundos, e os converta em segundos. Exemplo: 2h, 40min e 10s correspondem a 9.610 segundos.'''

#minha assinatura 
print("=+"*28,"\n"," "*20, "ALB System","\n","=+"*28,"\n")

def sub_rotina(hora,min,seg):
    soma = 0
    soma+=hora*3600
    soma+=min*60
    soma+=seg
    return soma

hora,min,seg = input("Infome hora min e segundos ").split(" ")
hora = int(hora)
min = int(min)
seg = int(seg)
print(f"O total em segundos é {sub_rotina(hora,min,seg)}")