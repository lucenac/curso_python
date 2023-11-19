"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""
import os
LISTA = []
lista_compras=[]

while True:
    print('Selecione uma opção')
    escolha = input('[i]nserir, [a]pagar, [l]istar: ').lower()
    if escolha == 'i':
        os.system('cls')
        inserir = input('Valor:')
        lista_compras.append(inserir)
        os.system('cls')
        
    elif escolha == 'a':
        os.system('cls')
        if not lista_compras:
            print('A lista está vazia!')
            continue
        apagar = input('Escolha o índice para apagar: ')
        try:
            int_apagar = int(apagar)
        except ValueError:
            print('Você não digitou um número')
            continue
        if int_apagar < 0 or int_apagar >= len(lista_compras):
            print('Índice inválido!')
            continue
        del lista_compras[int_apagar]
        
    elif escolha == 'l':
        if lista_compras == LISTA:
            os.system('cls')
            print('A lista está vazia!')
            continue
        os.system('cls')
        for indice, nome in enumerate(lista_compras):
            print(indice, lista_compras[indice])
    else:
        os.system('cls')
        print('Escolha uma opção válida')
        continue