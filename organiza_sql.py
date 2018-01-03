import re

entrada = open('popula_banco.sql')
saída = open('popula_banco_organizado.txt', 'w')
palavra = ''

for arquivo_lido in entrada.readlines():
    palavra += re.sub('\s+', ' ', arquivo_lido)
    palavra = palavra.replace(' ,', ', ')
    palavra = palavra.replace(' , ', ', ')
    palavra = palavra.replace(' insert ', '\ninsert ')
    palavra = palavra.replace('  ## ', '\n\n## ')
    palavra = palavra.replace('( ', '(')
    palavra = palavra.replace(' )', ')')
    palavra = palavra.replace(' ## ', '\n## ')
    palavra = palavra.replace(",  '", ', ')
    palavra = palavra.replace(',  ', ', ')

saída.write(palavra)
saída.close()
