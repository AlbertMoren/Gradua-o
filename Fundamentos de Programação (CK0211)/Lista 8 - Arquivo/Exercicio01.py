'''Faça um programa para criar os arquivos a seguir:'''
#minha assinatura 
print("=+"*28,"\n"," "*20, "ALB System","\n","=+"*28,"\n")
#Declaração de dados que irão para os arquivos
cliente = ['Cod_cli','nome','Endereço','Nome']
recebimentos = ['Num_doc','Valor_doc','Data_Emissao','Data_vecimento','Cod_Cli']

#Criando o arquivo cliente.txt e inserindo campos nele
with open('/home/albert/Área de Trabalho/Graduacao/Fundamentos de Programação (CK0211)/Lista 8/Clientes.txt','w') as arquivo1:
    for i in cliente:
        arquivo1.write(i+'\n')
    print("Arquivo criado com sucesso")

#Criando o arquivo Recebimentos.txt e inserindo campos nele
with open('Recebimentos.txt','w') as arquivo2:
    for i in recebimentos:
        arquivo2.write(i+'\n')
    print("Arquivo criado com sucesso")