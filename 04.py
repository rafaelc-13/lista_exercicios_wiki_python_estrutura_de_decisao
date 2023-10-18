'''4)Faça um Programa que verifique se uma letra digitada
é vogal ou consoante.'''
vogal = ("a","e","i","o","u")
letra = input("Digite uma letra: ")
if letra in vogal:
    print("Essa letra é uma vogal.")
else:
    print("Essa letra é uma consoante.")
