import urllib.request

página = urllib.request.urlopen('http://www.terra.com.br')
texto = página.read().decode('utf8')
print(texto)