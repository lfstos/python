dia, mes, ano = input('Data(d/mm/aaaa) ').split('/')

meses = [ 'janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho',
        'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']

print('Voce nasceu em:')
print('%s de %s de %s'%(dia, meses[int(mes - 1)], ano))
