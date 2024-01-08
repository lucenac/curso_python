while True:
    
    num1 = input('Digite um número:')
    num2 = input('Digite outro número: ')
    
    #CHECAGEM DE NÚMERO#
    try:
        float_num1=float(num1)
        float_num2=float(num2)
    except:
        print('Você não digitou um número válido!')
        continue
    
    #CHECAGEM DE OPERADOR#
    operador = input('Escolha um operador(+ - * /): ')    
    operadores_permitidos = '+-*/'
    if operador not in operadores_permitidos:
        print('Operador inválido!')
        continue
    
    if len(operador) > 1:
        print('Digite apenas um operador!')
    
    #OPERAÇÕES  
    if operador == '+':
        operacao = float(num1) + float(num2)
    elif operador == '-':
        operacao = float(num1) - float(num2)
    elif operador == '*':
        operacao = float(num1) * float(num2)
    elif operador == '/':
        operacao = float(num1) / float(num2)
        
    #RESULTADO#
    print(f'{num1} {operador} {num2} = {operacao}')
    
    #OPÇÃO DE SAIDA#
    sair = input('Quer sair? [s/n]: ').lower().startswith('s')
    if sair is True:
        break