lista = ['spam!', 1, ['Brie', 'Roquefort', 'Pol lê Veq'], [1, 2, 3]]

for i in range(len(lista)):
    if type(lista[i]) == list:
        for k in range (3):
            print(lista[i][k], len(str(lista[i][k])))
    else:
        print(lista[i], len(str(lista[i])))
