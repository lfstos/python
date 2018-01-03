def cabeca(lista):
    return lista[0]

def remove_cabeca(lista):
    del(lista[0])

def cauda(lista):
    return lista[1:]

def troca(x, y):
    return y, x

def lista_aleatoria():
    import random
    i = 0
    lista = []
    while i <= 10:
        x = random.randint(0, 20)
        if x not in lista:
            lista.append(x)
            i += 1
    lista.sort()
    print(lista)

def conta_caracteres_repetidos(texto):
    '''
    Conta o numero de caracteres iguais em um texto...
    Utiliza-se lista
    '''
    lista = []
    lista_caracteres_repetidos = []
    contador = 0
    for i in range(len(texto)):
        if texto[i] not in lista:
            lista.append(texto[i])
        elif texto[i] not in lista_caracteres_repetidos:
            lista_caracteres_repetidos.append(texto[i])
            contador += 1
    print('Caracter repetido: ', lista_caracteres_repetidos, ' = ', contador)

def conta_caracteres_iguais(texto):
    '''
    Conta o numero de caracteres iguais em um texto...
    Utiliza-se dicionarios
    '''
    dic = {}
    i = 0
    for i in range(len(texto)):
        if texto[i] not in dic:
            dic[texto[i]] = 1
        elif texto[i] in dic:
            dic[texto[i]] += 1
    print(dic)


def teste_tupla():
    '''
    Usando tupla
    '''
    tupla = ('Fernando', 'Manon', 'Ana', 'Julia', 'Filho')
    print(tupla)

def dics():
    inventario = {'abacaxis': 430, 'bacanas': 312, 'laranjas': 525, 'peras': 217}
    print(inventario)
