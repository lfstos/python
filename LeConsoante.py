i = 1
letras = []

while i <= 10:    
    letras.append(input('Letra: '))  
    i += 1

i = 0
cons = 0
while i < len(letras):
    if letras[i] not in 'aeiou':
        cons += 1
    i += 1
print(cons)


