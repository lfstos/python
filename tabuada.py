def tabuada(n):
    i = 0
    print('Tabuada do n!')
    while i <= 10:        
        print('%s * %s = %s' %(n, i, (n * i)))
        i += 1

tab = int(input('Qual tabuada: '))
tabuada(tab)
