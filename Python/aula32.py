# Faça um programa que peça ao usuário para digitar umm número inteiro, informe se este número é par ou impar. Caso o usuário não digite um número inteiro, informe que não é um número inteiro.

numero_int = input('Digite um número inteiro: ')

if numero_int.isdigit():
    inteiro = int(numero_int)
else:
    print('Você não digitou um numero inteiro')

    if inteiro % 2 == 0:
        print('Este número é par.')
    elif inteiro % 2 == 1:
        print('Este número é impar.')

# Faça um programa que pergunte a hora ao usuário e, baseando-se no horário descrito, exiba  a saudação apropriada.Ex.:
#Bom dia 0-11, Boa Tarde 12-17 e Boa noite 18-23. 

hora_atual = input('Digite as horas aqui: ')
hora_certa = float(hora_atual)

if hora_certa >= 0 and hora_certa <= 11:
    print('Bom dia!')
elif hora_certa > 11 and hora_certa <= 18:
    print('Boa Tarde')
else:
    print('Boa noite')

# Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letrass ou menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva "Seu nome é normal"; maior que 6 escreva "Seu nome é grande"

prim_nome = input('escreva aqui seu primeiro nome: ')
numero_caract = len(prim_nome)

if numero_caract <= 4:
    print('Seu nome é curto.')
elif numero_caract == 5 or numero_caract == 6:
    print('Seu nome tem tamanho normal.')
else:
    print('Você possui um grande nome.') 