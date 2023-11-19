#sistema de pergunta e respostas

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1','3','4','5'],
        'Resposta': '4',
        'Item' : '2',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25','55','10','51'],
        'Resposta': '25',
        'Item' : '0',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4','5','2','1'],
        'Resposta': '5',
        'Item' : '1',
    },
        {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4','5','2','1'],
        'Resposta': '5',
        'Item' : '1',
    },
]
acertos = 0

for questao in range(len(perguntas)):
    print(f'Pergunta:', perguntas[questao]['Pergunta'])
    print('\nOpções:')
    acessar = perguntas[questao]["Opções"]
    
    for item in range(len(acessar)):
        print(f'{item}) {acessar[item]}')

    #entrada de usuário
    entrada = input('Escolha uma opção: ').replace(' ', '')
    
    if entrada == perguntas[questao]['Item']:
        acertos += 1
        print('Acertou!✅\n')
    else:
        print('Errou!❌\n')
        
print(f'Você acertou {acertos} de {len(perguntas)} perguntas.')

