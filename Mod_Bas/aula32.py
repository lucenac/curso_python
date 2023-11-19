"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

'''
num = input('Digite um número inteiro: ')
try:
    num_int=int(num)
    if num_int % 2 == 0:
        print(f'{num} é um número par!')
    else:
        print(f'{num} é um número impar!')
except:
    print('Você não digitou um número inteiro!')
'''
    
"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""


'''
time = input('Digite a hora: ')
time_int= int(time)

if time_int <= 11:
    print('Bom dia!')
    
elif time_int <= 17:
    print('Boa tarde!')

elif time_int <= 23:
    print('Boa noite!')
else:
    print('Você digitou uma hora inválida') 
'''

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input('Digite seu primeiro nome: ')
len_nome = len(nome)

if len_nome <=4:
    print('Seu nome é pequeno!')
elif len_nome <= 6:
    print('Seu nome é normal!')
else:
    print('Seu nome é muito grande!')
