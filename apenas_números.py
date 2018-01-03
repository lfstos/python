i = 0
while i < 5:
    try:
        num = int(input('Digite um valor: '))
        i += 1
    except:
        print('Apenas números!!!')
