# Sets - Conjuntos em Python (tipo set)
# Conjuntos são ensinados na matemática
# https://brasilescola.uol.com.br/matematica/conjunto.htm
# Representados graficamente pelo diagrama de Venn
# Sets em Python são mutáveis, porém aceitam apenas
# tipos imutáveis como valor interno.

# Criando um set
# set(iterável) ou {1, 2, 3}

# s1 = set()
# s2 = {'joão',1,2,3}
# print(s1,type(s1))
# print(s2,type(s2))

# Sets são eficientes para remover valores duplicados
# de iteráveis.
# - Não aceitam valores mutáveis;
# - Seus valores serão sempre únicos;
# - não tem índexes;
# - não garantem ordem;
# - são iteráveis (for, in, not in)

# l1 = [1,2,3,3,3,3,2,4]
# print(l1)
# s1 = set(l1)
# print(s1)
# l1 = list(s1)
# print(l1)

# Métodos úteis:
# add, update, clear, discard

# s1 = set()
# s1.add('João')
# s1.add(1)
# s1.update(('Olá Mundo',1,2,3))
# # s1.clear()
# s1.discard('Olá Mundo')
# print(s1)

# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos

s1 = {1,2,3}
s2 = {2,3,4}

s3 = s1 | s2
# s3 = s1 & s2
# s3 = s1 - s2
# s3 = s1 ^ s2
print(s3)