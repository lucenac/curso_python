"""Interpretador do Python

python mod.py (executa o mod)
python -u (unbuffered)
python -m mod (lib mod como script)
python -c 'cmd' (comando)
python -i mod.py (interativo com mod)

The Zen of Python, por Tim Peters

Bonito é melhor que feio.
Explícito é melhor que implícito.
Simples é melhor que complexo.
Complexo é melhor que complicado.
Plano é melhor que aglomerado.
Esparso é melhor que denso.
Legibilidade conta.
Casos especiais não são especiais o bastante para quebrar as regras.
Embora a praticidade vença a pureza.
Erros nunca devem passar silenciosamente.
A menos que sejam explicitamente silenciados.
Diante da ambiguidade, recuse a tentação de adivinhar.
Deve haver um -- e só um -- modo óbvio para fazer algo.
Embora esse modo possa não ser óbvio à primeira vista a menos que você seja holandês.
Agora é melhor que nunca.
Embora nunca frequentemente seja melhor que *exatamente* agora.
Se a implementação é difícil de explicar, é uma má ideia.
Se a implementação é fácil de explicar, pode ser uma boa ideia.
Namespaces são uma grande ideia -- vamos fazer mais dessas!
"""
from time import sleep
from os import system

cont = s1 = s2 = m1 = m2 = 0


while True:
    cont+=1
    s1+=1
    if s1 == 10:
        s1 = 0
        s2+=1
    if s2 == 6:
        s2 = 0
        m1+=1
    if m1 == 10:
        m1 = 0
        m2+=1
    if m2 == 6:
        m2 = 0
        break
    print(f'{m2}{m1}:{s2}{s1}')
    print(f'Clocks:{cont}')
    
    sleep(1)
    system('cls')
