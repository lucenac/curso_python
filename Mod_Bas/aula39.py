"""
Iterando strings com while
"""

nome = 'Luiz Otávio'  # Iteráveis


print(nome)
nova_string = ''
cont = 0
while cont < len(nome):
    nova_string += f'*{nome[cont]}'
    cont+=1
    print(nova_string)
nova_string+='*'