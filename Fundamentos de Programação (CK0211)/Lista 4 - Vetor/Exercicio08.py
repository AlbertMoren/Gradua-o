'''Faça um programa que preencha um vetor com os nomes de sete alunos e carregue outro vetor com a média final desses alunos. Calcule e mostre:
■ o nome do aluno com maior média (desconsiderar empates);
■ para cada aluno não aprovado, isto é, com média menor que 7, mostrar quanto esse aluno precisa tirar na prova de exame final para ser aprovado. Considerar que a média para aprovação no exame é 5'''
#minha assinatura 
print("=+"*28,"\n"," "*20, "ALB System","\n","=+"*28,"\n")

aluno = []
medias = [0]*7
maior = [0]*2
for i in range(len(medias)):
    aluno_novo = input("Nome do Aluno: ")
    if aluno_novo in aluno:
        flag = 1
        while(flag == 1):
            aluno_novo = input("Valor incorreto, Valor já existe em nosso banco de dados: ")
            if aluno_novo not in aluno:
                flag == 0
    aluno.append(aluno_novo)
    medias[i] = float(input("Insira a média desse aluno: "))        #trexo responsavel por pegar a maior nota
    if medias[i] > maior[0]:
        maior[0] = medias[i]
        maior[1] = i

print(f"O aluno {aluno[maior[1]]} obteve a maior média, {maior[0]:.2f}\n")
for i in range(len(medias)):
    if medias[i] < 7 and medias[i] >= 4:
        print(f"O aluno {aluno[i]} precisa tirar {10-medias[i]:.2f} para ser aprovado")
            

