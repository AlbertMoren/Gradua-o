'''Foi feita uma pesquisa entre os habitantes de uma região. Foram coletados os dados de idade, sexo (M/F) e salário. Faça um programa que calcule e mostre:
■ a média dos salários do grupo;
■ a maior e a menor idade do grupo;
■ a quantidade de mulheres com salário até R$ 200,00;
■ a idade e o sexo da pessoa que possui o menor salário.
Finalize a entrada de dados ao ser digitada uma idade negativa.'''

#my signature 
print("=+"*28,"\n"," "*20, "ALB System","\n","=+"*28,"\n")

counterSalary = 0
minorSex = 0
cont = 0
majorAge = 0
minorAge = 999999
counterWomans = 0

while True:
    age = int(input("Enter your age: "))
    if age < 0:
        break
    sex = input("Enter your gender[M/F]: ")
    salary = float(input("Enter your salary: "))
    
    counterSalary+=salary
    cont+=1
    
    if age > majorAge:
        majorAge = age
    if age < minorAge:
        minorAge = age
        minorSex = sex
    
    if sex == 'F':
        if salary > 200.00:
            counterWomans+=1

print(f"the average salary of the group is {counterSalary/cont:.2f}\nthe oldest is {majorAge} and youngest age is {minorAge}\nthe number of women earning up to R$ 200.00 is {counterWomans}\nthe age and sex of the person with the lowest salary is {minorAge} and {minorSex}")

