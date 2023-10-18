'''9)Faça um Programa que leia três números
e mostre-os em ordem decrescente.'''
n1 = int(input("Digite o 1º numero: "))
n2 = int(input("Digite o 2º numero: "))
n3 = int(input("Digite o 3º numero: "))
if n1 > n2 > n3:
    print ("Na ordem decrescente temos: ",n1,n2,n3)
    if n2 < n3:
        print("Na ordem decrescente temos: ",n1,n3,n2)
elif n2 > n3 > n1:
    print ("Na ordem decrescente temos: ",n2,n3,n1)
    if n3 < n1:
        print("Na ordem decrescente temos: ",n2,n1,n3)
elif n3 > n2 > n1:
    print ("Na ordem decrescente temos: ",n3,n2,n1)
    if n2 < n1:
        print("Na ordem decrescente temos: ",n3,n1,n2)

