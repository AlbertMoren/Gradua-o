'''Uma escola deseja saber se existem alunos cursando, simultaneamente, as disciplinas Lógica e Linguagem de Programação. Coloque os números das matrículas dos alunos que cursam Lógica em um vetor, quinze alunos. Coloque os números das matrículas dos alunos que cursam Linguagem de Programação em outro vetor, dez alunos. Mostre o número das matrículas que aparecem nos dois vetores.'''

logica = [0]*15
linguagen = [0]*10
intersec = []
for i in range(len(logica)):
    matrcua = int(input(f"Matricula do aluno {i+1}° de logica  "))
    if matrcua in logica:
        flag = 1
        while(flag == 1):
            matrcua = int(input("Valor já existe em nosso banco, insira um válido"))
            if matrcua not in logica:
                flag = 0
    logica.append(matrcua)
    if 0 in logica:
        logica.remove(0)
for i in range(len(linguagen)):
    matrcua = int(input(f"Matricula do aluno {i+1}° de Linguagem  "))
    if matrcua in linguagen:
        flag = 1
        while(flag == 1):
            matrcua = int(input("Valor já existe em nosso banco, insira um válido: "))
            if matrcua not in linguagen:
                flag = 0
    linguagen.append(matrcua)
    if 0 in logica:
        logica.remove(0)
for i in logica:
    for j in linguagen:
        if i == j:
            intersec.append(i)
print(intersec)
    