# Exercício 
# Peça ao usuário para digitar seu nome
# Peça ao usuário para digitar sua idade
# Se nome e idade forem digitados:
#     Exiba:
#         Seu nome é {nome}
#         Seu nome ivertido é {nome invertido}
#         Seu nome contém (ou não) espaços
#         Seu nome tem {n} letras
#         A primeira letra do seu nome é {letra}
#         A última letra do seu nome é {letra}
# Se nada for digitado em nome ou idade:
#     Exiba:
#         "Desculpe, você deixou campos vazios."

nome = input('Digite aqui seu nome: ')
idade = input('Digite aqui sua idade: ')
n_letras = len(nome)
p_letra = nome[0]
u_letra = nome[-1]

if nome and idade:
    print(f'Seu nome é {nome} e sua idade é {idade} anos.')
    print(f'Seu nome invertido seria {nome[::-1]}')

    if ' ' in nome:
        print('Seu nome contém espaços.')
    else:
        print('Seu nome não contém espaços.')
    
    print(f'Seu nome possui {n_letras} letras.')
    print(f'A primeira letra do seu nome é {p_letra} e a última é {u_letra}')
else:
    print('Desculpe, você deixou campos vazios.')