'''10)Faça um Programa que pergunte em que turno você estuda.
 Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
  Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!"
   ou "Valor Inválido!", conforme o caso.
'''
turno = input('''Que turno você estuda:
M-matutino ou V-Vespertino ou N- Noturno \n:''')

if turno.lower() == "m":
    print("Bom dia!")
elif turno.lower() == "t":
    print("Boa tarde!")
elif turno.lower() == "n":
    print("Boa Noite!")
else:
    print("Turno inválido!")
