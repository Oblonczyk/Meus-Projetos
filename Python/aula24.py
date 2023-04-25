# Operadores in e not in
# Strings são iteráveis
#   0 1 2 3 4 5
#   V i n y c i u s
#  -6-5-4-3-2-1 
 
# nome = 'Vinycius'
# print(nome[3])
# print(nome[-5])

# print('y' in nome)
# print('Cre' in nome)
# print(10 * '-')
# print('bene' not in nome)
# print('cius' not in nome)

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')