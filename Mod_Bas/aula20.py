primeiro_valor= input('Digite um valor:')
segundo_valor= input('Digite outro valor:')

if primeiro_valor > segundo_valor:
    print(f'primeiro_valor = {primeiro_valor} é maior que segundo_valor= {segundo_valor}')
elif segundo_valor > primeiro_valor:
    print(f'segundo_valor={segundo_valor} é maior que primeiro_valor={primeiro_valor}')
else:
    print(f'primeiro_valor={primeiro_valor} é igual à segundo_valor={segundo_valor}')
    