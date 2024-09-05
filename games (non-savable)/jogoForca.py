'''Exercício
Faça o algoritmo e implemente o programa do Jogo da forca
(https://pt.wikipedia.org/wiki/Jogo_da_forca)
'''

def jogoForca(palavra = 'palavra'):
    adivinhar = list(palavra.upper())
    display = []
    for char in adivinhar:
        if char in 'abcdefghijklmnopqrstuvwxyz'.upper():
            display.append('_')
        else:
            display.append(char)
    erros = []

    def desenharEnforcado():
        partes = {0: """
      _______
     |/      |
     |      
     |       
     |       
     |
  ___|___
 |_______|""",
                  1: """
      _______
     |/      |
     |      (_)
     |       
     |       
     |
  ___|___
 |_______|""",
                  2: """
      _______
     |/      |
     |      (_)
     |       |
     |       |
     |       
  ___|___
 |_______|""",
                  3: """
      _______
     |/      |
     |      (_)
     |       |
     |       |
     |      /
  ___|___
 |_______|""",
                  4: """
      _______
     |/      |
     |      (_)
     |       |
     |       |
     |      / \\
  ___|___
 |_______|""",
                  5: """
      _______
     |/      |
     |     (o.o)
     |      /|
     |       |
     |      / \\
  ___|___
 |_______|""",
                  6: """
      _______
     |/      |
     |     (0.0)
     |      /|\\
     |       |
     |      / \\
  ___|___
 |_______|""",
                  7: """
      _______
     |/      |
     |     (x_x)
     |      /|\\
     |       |
     |      / \\
  ___|___
 |_______|"""}
        print(partes[len(erros)], end='   ')

    def mostrarEstado():
        desenharEnforcado()
        for char in display:
            print(char,end='')
        print()
        if len(erros) > 0:
            print('Não tem:',end=' ')
            for l in range(len(erros) - 1):
                print(erros[l],end=' - ')
            else:
                print(erros[-1])
        print()

    def verificar(guess):
        nonlocal display
        while guess in erros or guess in display:
            guess = input('Introduza uma letra nova: ').upper()
        if guess == palavra.upper():
            display = adivinhar
            return
        if guess in adivinhar:
            for char in range(len(adivinhar)):
                if guess == adivinhar[char]:
                    display[char] = guess
        else:
            erros.append(guess)

    while display != adivinhar and len(erros) < 7:
        mostrarEstado()
        verificar( input('Introduza letra: ').upper())
    else:
        mostrarEstado()
        print(f'A resposta era "{palavra}".')
        if display == adivinhar:
            print('Ganhou :)')


if __name__ == "__main__":
    jogoForca()
