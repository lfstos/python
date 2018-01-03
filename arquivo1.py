def subs_vogal_ast(texto):
    '''
    Este metodo le uma palavra, e substitui uma vogal por asterisco.
    '''
    entrada = open('cripto1.txt', 'w')
    txt = ''
    i = 0
    while i < len(texto):
        if texto[i].lower() in 'aeiou':
            txt += '*'
        else:
            txt += texto[i]
        i += 1
    entrada.write(txt)
    entrada.close()

def le_arquivo1():
    arquivo = open('cripto1.txt', 'r')
    for arq in arquivo:
        print(arq)
    arquivo.close()

def copia_arquivo():
    arquivo1 = open('cripto1.txt', 'r')
    arquivo2 = open('cripto2.txt', 'w')

    for arq in arquivo1:
        arquivo2.write(arq)
    arquivo2.close()
    arquivo1.close()

def le_arquivo2():
    arquivo = open('cripto2.txt')
    for arq in arquivo:
        print(arq)
    arquivo.close()

def le_arquivo_de_outro_local(arquivo):
    caminho = open(arquivo)
    for arq in caminho:
        print(arq)
    camino.close()

def gravando_numeros(numero):
    arquivo = open('grava_numeros.txt', 'w')
    num = str(numero)
    arquivo.write(num)
    arquivo.close()
    

def lendo_arquivo_numeros():
    gravando_numeros(str(1024))
    arquivo = open('grava_numeros.txt')
    for arq in arquivo:
        print(arq)
    arquivo.close()

def relatorio(salarios):
    estudantes = salarios.keys()
    estudantes.sort()
    for estudante in estudantes:
        print ("%-20s %12.02f" % (estudante, salarios[estudante]))
