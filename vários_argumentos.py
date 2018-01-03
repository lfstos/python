def somatório(*argumentos):
    for i in argumentos:
        print(i)

def soma(arg, arg1):
    return arg + arg1

def potenciação(arg):
    return arg ** 2

def quadrado(termo):
    termo ** 2

elementos = [1, 2, 3, 4, 5, 6]

map(quadrado, elementos)
