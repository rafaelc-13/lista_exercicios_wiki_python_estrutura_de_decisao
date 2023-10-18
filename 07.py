'''7)Faça um Programa que leia três números
 e mostre o maior e o menor deles.'''
n1 = float(input("Digite o 1º numero: "))
n2 = float(input("Digite o 2º numero: "))
n3 = float(input("Digite o 3º numero: "))
maior = n1
menor = n1

if n2 > maior:
    maior = n2
elif n2 < menor:
    menor = n2

if n3 > maior:
    maior = n3
elif n3 < menor:
    menor = n3
print(f"Maior valor é: {maior}")
print(f"Menor valor é: {menor}")
