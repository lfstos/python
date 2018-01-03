arquivo = open('numeros.txt', 'r')

for i in arquivo.readlines():
    print(i.rstrip())
arquivo.close()
