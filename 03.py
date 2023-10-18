'''3)Faça um Programa que verifique se uma letra digitada é "F" ou "M".
Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido'''
genero = input('''Digite:
M - Masculinp
F - Feminino
: ''')

if genero.lower() == "M":
    print("Sexo escolhido - Masculino")
elif genero.lower() == "F":
    print("Sexo escolhido - Feminino")
else:
    print("Sexo inválido.")
