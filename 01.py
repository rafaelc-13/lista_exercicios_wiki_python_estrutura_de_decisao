'''1)Faça um Programa que peça dois números e imprima o maior deles.'''
n1 = float(input("Digite um valor: "))
n2 = float(input("Digite outro valor: "))
if n1 != n2:
    if n1 > n2:
        print("O maior volor é",n1)
    else:
        print("O maior volor é",n2)
else:
    print("Valores iguais.")
