'''
12)Faça um programa para o cálculo de uma folha de pagamento,
 sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo)
  e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita).
   O Salário Líquido corresponde ao Salário Bruto menos os descontos.
    O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20%
Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
'''

valor_hora = float(input("Qual o valor da sua hora trabalhada? "))
qtd_horas = int(input("Quantas horas você trabalha por mês? "))
salario_bruto = valor_hora * qtd_horas
imposto = 0
FGTS = salario_bruto * 11 / 100

if salario_bruto <= 900:
    imposto = 0
elif 900 < salario_bruto <=1500:
    imposto = 5
elif 1500 < salario_bruto <= 2500:
    imposto = 10
else:
    imposto = 20

sindicato = 0.03 * salario_bruto
IR = (salario_bruto * imposto/100)
salario_liquido = salario_bruto - IR - sindicato + FGTS


print(f'''        Salário Bruto: ({valor_hora} * {qtd_horas})        : R$ {salario_bruto:.2f}
        (-) IR ({imposto}%)                     : R$   {IR:.2f} 
        (-) Sindicato (3%)                 : R$  {sindicato:.2f}
        FGTS (11%)                      : R$  {FGTS:.2f}
        Total de descontos              : R$  {IR + sindicato:.2f}
        Salário Liquido                 : R$  {salario_liquido:.2f}''')
