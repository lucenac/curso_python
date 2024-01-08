lista = list(range(1,17))

for i in range(len(lista)//2):
    lista[i], lista[-1-i] = lista[-1-i], lista[i]
print(lista)