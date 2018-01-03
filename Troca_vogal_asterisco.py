palavra = input('Palavra: ')

i = 0
troca = ''

while i < len(palavra):
    if palavra[i] in 'aeiou':
        troca += '*'
    else:
        troca += palavra[i]
    i += 1
print(troca)

