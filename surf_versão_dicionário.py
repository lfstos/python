f = open('surf.txt')
notas = {}
for linha in f:
    nome, pontos = linha.split()
    notas[float(pontos)] = nome
f.close()
for nota in sorted(notas, reverse = True):
    print('{} tem nota{}'.format(notas[nota], nota))
