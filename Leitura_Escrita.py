texto = open('mensagens.txt')
saida = open('cripto.txt', 'w')

for i in texto.readlines():
    for k in i:
        if k in 'aeiou':
            saida.write('*')
        else:
            saida.write(k)
texto.close()
saida.close()
