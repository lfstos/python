entrada = open('popula_banco.sql')
saída = open('popula_banco_organizado1.txt', 'w')
lido = ''

for lendo in entrada.read():
    lido += lendo.rstrip()
    lido = lido.replace('insertintocomclienvalues', '\ninsert into comclien values ')

saída.write(lido)
saída.close()
entrada.close()
