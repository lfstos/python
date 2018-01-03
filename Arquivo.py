arquivo = open('numeros.txt', 'w')
for i in range(1, 101):
    arquivo.write('%d\n ' %i)
arquivo.close()
