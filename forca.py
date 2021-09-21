import requests

word = requests.get('https://api.dicionario-aberto.net/random').json()['word'].upper()
attempt = 0
letras = []
palavra = len(word)*['_']
while (attempt<10 or ''.join(palavra)==word):

    print(f'Vc ainda tem {10-attempt} tentativas\n')
    print(f'Letras já tentadas {" ".join(letras)}\n')
    print(' '.join(palavra))
    letra = input('Digite a Letra').upper()
    letras.append(letra)
    for l in range(len(word)):
        if word[l] == letra:
            palavra[l] = letra
    else:
        attempt+=1
if attempt==10:
    print('Vc perdeu')
    print(f'A palavra era {word}')
else:
    print('Parabéns vc ganhou')