'''
11)As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
1- salários até R$ 280,00 (incluindo) : aumento de 20%
2- salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
3- salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
4- salários de R$ 1500,00 em diante : aumento de 5%.
Após o aumento ser realizado, informe na tela:
o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento.
'''

salario = float(input("Quanto você ganha atualmente? R$"))
salario_antigo = salario
percentual_aumento = 0
aumento = 0

if salario <= 280.0:
    percentual_aumento = 20
    aumento = 0.2 * salario
    salario += aumento
elif salario > 280.0 and salario <= 700.0:
    percentual_aumento = 15
    aumento = 0.15 * salario
    salario += aumento
elif salario > 700 and salario <= 1500:
    percentual_aumento = 10
    aumento = 0.10 * salario
    salario += aumento
else:
    percentual_aumento = 5
    aumento = 0.05 * salario
    salario += aumento

print(f"O salário antes do reajuste era: R${salario_antigo}")
print(f"O percentual de aumento aplicado foi de {percentual_aumento}%")
print(f"O valor do aumento foi de: R${aumento}")
print(f"O novo salário, após o aumento, é: R${salario}")
