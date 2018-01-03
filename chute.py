# Estamos pegando da biblioteca random, apenas o randint
from random import randint

print('Bem vindo!')
chute = 0
sorteado = randint(1, 100)
while chute != sorteado:
	chute = int(input('Chute um número: '))
	if chute == sorteado:
		print('Você venceu !!!')
	else:
		if chute > sorteado:
			print('Alto')
		else:
			print('Baixo')
print('Fim do jogo !')