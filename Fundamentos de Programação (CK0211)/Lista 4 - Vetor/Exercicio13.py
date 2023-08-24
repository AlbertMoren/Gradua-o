'''Faça um programa que receba o nome e a nota de oito alunos e mostre o relatório a seguir:
Digite o nome do 1o aluno: Carlos
Digite a nota do Carlos: 8
Digite o nome do 2o aluno: Pedro
Digite a nota do Pedro: 5
Relatórios de notas
Carlos 8.0
Pedro 5.0
..
..
..
Média da classe = ??'''

vectorNote = []
vectorName = []

for i in range(8):
    name = input(f"Enter the name of the {i+1}st student: ")
    note = float(input(f"Enter {name}' note: "))
    vectorName.append(name)
    vectorNote.append(note)

for i in range(8):
    print(f"{vectorName[i]} {vectorNote[i]:.1f}")

everage = sum(vectorNote)/8
print(f"class everage = {everage:.2f}")
