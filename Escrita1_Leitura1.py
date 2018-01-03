texto = open('mensagem.txt')
saida = open('crypto.txt', 'w')

for linha in texto.readlines():
    for caracter in linha:
        if caracter in 'aeiou':
            saida.write('*')
        else:
            saida.write(caracter)
texto.close()
saida.close()
            
