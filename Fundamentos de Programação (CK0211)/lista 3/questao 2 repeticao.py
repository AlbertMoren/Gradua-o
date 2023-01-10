'''Uma companhia de teatro deseja montar uma série de espetáculos. A direção calcula que, a
R$ 5,00 o ingresso, serão vendidos 120 ingressos, e que as despesas serão de R$ 200,00. Diminuindo-se em
R$ 0,50 o preço dos ingressos, espera-se que as vendas aumentem em 26 ingressos. Faça um programa que
escreva uma tabela de valores de lucros esperados em função do preço do ingresso, fazendo-se variar esse pre-
ço de R$ 5,00 a R$ 1,00, de R$ 0,50 em R$ 0,50. Escreva, ainda, para cada novo preço de ingresso, o lucro
máximo esperado, o preço do ingresso e a quantidade de ingressos vendidos para a obtenção desse lucro.'''

ingresso = 5.00
pessoa = 120.00
despesa = 200.00
for i in range(9):
    ganho = ingresso*pessoa
    lucro = ganho-despesa
    print(f"valor  | Teremos  | Ganhos   | Despesa  | lucro ")
    print(f"R${ingresso:.2f} | {pessoa:.2f}   | R${ganho:.2f} | R${despesa:.2f} | R${lucro:.2f}")
    ingresso-=0.50
    pessoa+=16