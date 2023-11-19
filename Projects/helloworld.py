from time import sleep

palavra = 'hello world'
palavra_formada = ''
alfabeto = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ']

for letra_palavra in range(0, len(palavra)):
    for letra_alfabeto in range(0, len(alfabeto)):
        if alfabeto[letra_alfabeto] == palavra[letra_palavra]:
            palavra_formada += alfabeto[letra_alfabeto]
            sleep(0.03)
            print(palavra_formada)
            break
        
        else:
            if palavra_formada == '':
                sleep(0.03)
                print(alfabeto[letra_alfabeto])
                
            elif palavra[letra_palavra] == letra_alfabeto:
                sleep(0.03)
                print(palavra_formada)
            
            else:
                sleep(0.03)
                soma = palavra_formada + alfabeto[letra_alfabeto]
                print(soma)

