'''8)Faça um programa que pergunte o preço de três produtos
e informe qual produto você deve comprar,
sabendo que a decisão é sempre pelo mais barato.'''
p1 = float(input("Digite o valor do 1º produro: "))
p2 = float(input("Digite o valor do 2º produro: "))
p3 = float(input("Digite o valor do 3º produro: "))
menor = p1
if p2 < menor:
    menor = p2
elif p3 < menor:
    menor = p3
print(f"É recomendado que você compre o mais barato, (R${menor}).")
