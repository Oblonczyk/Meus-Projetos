# Operadores lógicos
# and (e) or (ou) not (não)
# and - Todas as condições precisam ser verdadeiras
# Se qualquer valor for considerado falso, a expressão inteira será avaliada naquele valor
# São considerados falsy (que você ja viu) 0 0.0 '' False
# Também existe o tipo None, que é usado para representar um não valor

# entrada = input('[E]ntrar [S]air ')
# senha_digitada = input('Senha: ')
# senha_permitida = '123456'

# if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
#     print('Você entrou!')
# elif senha_digitada != senha_permitida:
#     print('Senha incorreta!')
# elif entrada == 'S' or entrada == 's': 
#     print('Você saiu!')
# else:
#     print('Dado não reconhecido')

#AVALIAÇÃO DE CURTO CIRCUITO
senha = input('Senha: ') or 'Sem senha'
print(senha)