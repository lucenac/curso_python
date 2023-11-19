def criar_multiplicador(calculo):
    def multiplicar(numero):
        return numero * calculo
    return multiplicar

duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

print(duplicar(2))
print(triplicar(4))
print(quadruplicar(5))