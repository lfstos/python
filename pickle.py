import pickle

def grava_numero(numero):
    arquivo = open ('cripto3.txt', 'wb')
    pickle.dump(numero, arquivo )
    arquivo.close()
    
def le_numero():
    numero = int(input('Numero: '))
    grava_numero(numero)
    arquivo = open('critpo3.txt', 'rb')
    x = pickle.load(arquivo)
    for arq in x:
        print(arq)
    arquivo.close()
