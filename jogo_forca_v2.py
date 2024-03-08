from os import system, name


def limpaTela():
    # Windows
    if name == 'nt':
        _ = system('cls')
    # Mac / Linux
    else:
        _ = system('clear')


def sorteiaPalavra():
    import random

    with open('./vocabulario.txt', 'r', encoding='utf-8') as arquivo:
        conteudo = arquivo.read()
        palavras = conteudo.split('\n')

    return random.choice(palavras)


def displayForca(vidas):
    # Lista com os estágios da forca
    stages = [
        '''
            ----------
            |        |
            |        X
            |       \\|/
            |        |
            |       / \\
            |
            -
        ''', '''
            ----------
            |        |
            |        0
            |       \\|/
            |        |
            |       / 
            |
            -
        ''',
        '''
            ----------
            |        |
            |        0
            |       \\|/
            |        |
            |       
            |
            -
        ''',
        '''
            ----------
            |        |
            |        0
            |       \\|/
            |        
            |       
            |
            -
        ''',
        '''
            ----------
            |        |
            |        0
            |       \\|
            |        
            |       
            |
            -
        ''',
        '''
            ----------
            |        |
            |        0
            |       
            |        
            |       
            |
            -
        ''',
        '''
            ----------
            |        |
            |        
            |       
            |        
            |       
            |
            -
        '''
    ]
    return stages[vidas]


def executaGame():

    from unidecode import unidecode

    limpaTela()
    print('Bem vindo(a) ao jogo da FORCA!')
    print('Adivinhe a palavra abaixo antes de se enrolar...')

    # Escolhe aleatoriamente uma palavra
    palavra_chave = sorteiaPalavra()

    # Palavra sem acentos ou cedilha
    palavra_chave_limpa = unidecode(palavra_chave)

    # Máscara da palavra chave
    letras_descobertas = ['_' for letra in palavra_chave]

    # Número de vidas máximas
    vidas = 6

    # Lista de letras erradas
    letras_erradas = []

    while vidas > 0:

        # Preenche hífen
        if "-" in palavra_chave:
            index = 0
            for letra in palavra_chave:
                if letra == "-":
                    letras_descobertas[index] = "-"
                index += 1

        # Print
        print(displayForca(vidas))
        print(" ".join(letras_descobertas))
        print("Vidas Restantes: ", vidas)
        print("Letras erradas: ", " ".join(letras_erradas))
        print("")

        # Tentativa
        tentativa = input("\nEscolha uma letra: ").lower()
        tentativa = unidecode(tentativa)

        # Verifica se a letra está na palavra
        if tentativa in palavra_chave_limpa:
            index = 0
            for letra in palavra_chave_limpa:
                if letra == tentativa:
                    letras_descobertas[index] = palavra_chave[index]
                index += 1
        else:
            vidas -= 1
            letras_erradas.append(tentativa)

        # Verifica se o jogador venceu
        if '_' not in letras_descobertas:
            print("Parabéns! Você descobriu a palavra: ", palavra_chave)
            break

    # Verifica se o jador perdeu
    if '_' in letras_descobertas:
        print("Mais sorte na próxima vez! A palavra era: ", palavra_chave)


if __name__ == '__main__':
    executaGame()
