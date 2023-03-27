'''Faça um programa para cadastrar clientes no arquivo criado no Exercício 1.'''

caminho_arquivo = "/home/albert/Área de Trabalho/Graduacao/Fundamentos de Programação (CK0211)/Lista 8/Clientes.txt"
cliente = ['Cod_cli','nome','Endereço','Nome']

#Abri o arquivo para pegar os campos existente nele
def ler_campos_do_arqivo(caminho_arquivo):
    with open(caminho_arquivo,'r') as arquivo:
        return arquivo.readlines()

#Organiza os valores para ser inserido no arquivo
def pegar_valores(campos):
    valores = []
    for campo in campos:
        valor = input(f"Informe o valor para {campo.strip()}: ")
        valores.append(f"{campo.strip()} {valor}\n")
    return valores

# Escrever a lista modificada de volta no arquivo
def escrever_no_arquivo(caminho_arquivo,valores):
    with open(caminho_arquivo, 'w') as arquivo:
        arquivo.writelines(valores)

# Criar arquivo com campos iniciais
def criar_arquivo(caminho_arquivo):   
    with open(caminho_arquivo,'w') as arquivo:
        for campo in cliente:
            arquivo.write(campo + '\n')
    print("Arquivo criado com sucesso")
    return arquivo

#Imprimi na tela o conteúdo do arquivo
def printar_arquivo(caminho_arquivo):
    with open(caminho_arquivo,'r') as arquivo:
        conteudos = arquivo.readlines()
        for conteudo in conteudos:
            print(conteudo)

# Modificar a lista com os valores que deseja adicionar ao lado de cada campo
def trabalhando_os_dados(caminho_arquivo):
    campos = ler_campos_do_arqivo(caminho_arquivo)
    valores = pegar_valores(campos)
    escrever_no_arquivo(caminho_arquivo, valores)
    print("Valores adicionados com sucesso!")

def union_funcoes(caminho_arquivo):
    criar_arquivo(caminho_arquivo)
    trabalhando_os_dados(caminho_arquivo)
    printar_arquivo(caminho_arquivo)

def main():
    print("=+"*28,"\n"," "*20, "ALB System","\n","=+"*28,"\n")
    union_funcoes(caminho_arquivo)

main()