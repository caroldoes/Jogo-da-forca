import random

palavras_programa = ['beijo', 'rodrigo', 'carol', 'bola', 'gato']
palavra_selecionada = random.choice(palavras_programa)
#print(palavra_selecionada)
tentativas = 10
acertos = []

for tentativa in range(tentativas):
    chute = input(f'Tentativa {tentativa+1} -  Chute uma letra: ')
    
    if chute in palavra_selecionada:
        acertos.append(chute)
        print('Acertou!')
    else:
        print('Errou!')

    texto_forca = ''
    ganhou = True
    for letra in palavra_selecionada:
        if letra in acertos:
            texto_forca += f'{letra}'
        else:
            ganhou = False
            texto_forca += '_'

    print(texto_forca)

    if ganhou:
        break

if ganhou:
    print('Parabéns! Você ganhou!')
else:
    print('Você perdeu!')
    print(f'A palavra era {palavra_selecionada}')