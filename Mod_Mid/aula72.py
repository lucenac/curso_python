def multiplicacao(*args):
    cont = 1
    for i in args:
        cont*= i
    return cont
    
    
numeros = multiplicacao(1,2,3,4,5)
print(numeros)


def par_impar(x):
    if x % 2 == 0:
        return f'{x} é par'
    return f'{x} é impar'
    
print(par_impar(3))