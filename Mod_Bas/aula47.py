"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
"""
palavra_secreta = 'python'
codificado = ['*'] * len(palavra_secreta)
cont = 0

while '*' in codificado:

    tentativa = input('Digite uma letra:')
    
    if len(tentativa) > 1:
        print('Você digitou mais de uma letra, tente novamente!')
        continue
    if tentativa in codificado:
        print('Você já digitou essa letra!')
        continue

    acertou = False
    for i in range(len(palavra_secreta)):
        if palavra_secreta[i] == tentativa:
            codificado[i] = tentativa
            acertou = True
    
    print('Palavra secreta:',''.join(codificado))        
    
    if not acertou:
        print('Você errou!')
    else:
        print('Você acertou!')
    
    cont += 1
print('Você acertou a palavra secreta!')
print(f'Número de tentativas: {cont}')
"""
import os

palavra_secreta = 'perfume'
letras_acertadas = ''
numero_tentativa = 0

while True:
    letra_digitada = input('Digite uma letra:')
    numero_tentativa +=1
    
    if len(letra_digitada) > 1:
        print('Digite uma letra')
        continue
    
    #adiciona a letra
    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada
    
    
    #imprimir asteriscos
    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada+='*'
            
    print('Palavra formada: ', palavra_formada)
    
    if palavra_formada == palavra_secreta:
        print('Você ganhou!')
        print('Tentativas: ', numero_tentativa)
        letras_acertadas = ''
        numero_tentativa = 0
        