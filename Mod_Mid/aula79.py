#Exemplo de uso dos sets

letras = set()

while True:
    entrada = input('Digite uma letra:')
    letras.add(entrada.lower())
    if 'l' in letras:
        print('parabéns')
        break