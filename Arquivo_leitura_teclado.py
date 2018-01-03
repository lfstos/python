palavra = input('Palavra: ')
saida = open('palavras.txt', 'w')

while palavra != 'sair':
    palavra = input('Palavra: ')
    saida.write(palavra)
    
saida.close()
