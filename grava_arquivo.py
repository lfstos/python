def p(palavra):
    saída = open('saída.txt', 'w')
    troca = ''
    for i in range(len(palavra)):
        if palavra[i] in 'aeiou':
            troca += '*'
        else:
            troca += palavra[i]
    saída.write(troca)
    saída.close()

if __name__ == '__main__':
    palavra = input('Palavra: ')
    p(palavra)
