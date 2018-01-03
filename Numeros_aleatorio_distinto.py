def numeros_aleatorios_distintos():
    import random
    lista = []
    i = 0
    while i <= 15:
        num = random.randint(1, 100)
        if num not in lista:
            lista.append(num)
            i += 1
        lista.sort()
    return lista
        
