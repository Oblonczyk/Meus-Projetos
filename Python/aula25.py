# Interpolação básica de strings

# s - string
# d e i - int
# f - float
# x e X - Hexadecimal (ABCDEF0123456789)

nome = 'Viny'
preco = 1000.95897643
variavel = '%s, o preço total é R$%.2f' % (nome, preco)
print(variavel)
print('o hexadecimal de %d é %08X' % (15, 15))