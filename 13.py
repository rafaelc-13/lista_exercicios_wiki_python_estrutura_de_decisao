'''
13)Faça um Programa que leia um número e exiba o dia correspondente da semana.
(1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.
'''
semana = ['Domingo','Segunda','Terça','Quarta','Quinta','Sexta','Sabado']
dia = int(input("Digite um número e exiba o dia correspondente da semana (1-Domingo, 2- Segunda, etc.): "))

if 1 <= dia <= 7:
    print("Corresponde ao dia", semana[dia-1])
else:
    print("Valor inválido!")
