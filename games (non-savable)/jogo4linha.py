'''Exercício 5
Implemente o algoritmo e implemente o programa do jogo 4 em linha
(https://brainking.com/pt/GameRules?tp=13).
'''

def jogo4linha():
    def mostrar_tabuleiro():
        print('\n  1   2   3   4   5   ')
        for row in tabuleiro:
            print('_____________________',end='\n|')
            for square in row:
                print(f' {square} ',end='|')
            print()
        print('_____________________\n')


    def verificar_se_ganhou():
        for row in tabuleiro:
            if (row[1] != ' '
            and row[1] == row[2] and row[2] == row[3]
            and (row[0] == row[1] or row[3] == row[4])):
                return row[2]

        for col in range(5):
            if (tabuleiro[1][col] != ' '
            and tabuleiro[1][col] == tabuleiro[2][col] and tabuleiro[2][col] == tabuleiro[3][col]
            and (tabuleiro[0][col] == tabuleiro[1][col] or tabuleiro[3][col] == tabuleiro[4][col])):
                return tabuleiro[2][col]

        if (tabuleiro[2][2] != ' '
        and ((tabuleiro[1][1] == tabuleiro[2][2] and tabuleiro[2][2] == tabuleiro[3][3]
            and (tabuleiro[0][0] == tabuleiro[1][1] or tabuleiro[3][3] == tabuleiro[4][4]))
        or (tabuleiro[1][3] == tabuleiro[2][2] and tabuleiro[2][2] == tabuleiro[3][1]
            and (tabuleiro[0][4] == tabuleiro[1][3] or tabuleiro[3][1] == tabuleiro[4][0]))
        )):
            return tabuleiro[2][2]

        elif (tabuleiro[3][2] != ' '
        and ((tabuleiro[1][0] == tabuleiro[2][1] and tabuleiro[2][1] ==
              tabuleiro[3][2] and tabuleiro[3][2] == tabuleiro[4][3])
        or (tabuleiro[1][4] == tabuleiro[2][3] and tabuleiro[2][3] ==
            tabuleiro[3][2] and tabuleiro[3][2] == tabuleiro[4][1])
        )):
            return tabuleiro[3][2]

        return False

    tabuleiro = [[' ', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', ' ', ' ']]
    casas = 25
    acabou = False

    while casas > 0 and not acabou:
        mostrar_tabuleiro()

        if casas % 2 == 0:
            simb = '#'
        else:
            simb = '@'

        joga = input(f'Jogador {simb}, escolha coluna: ')
        while True: # para confirmar jogada
            try:
                joga = int(joga)
                if joga < 1 or joga > 5:
                    raise ValueError

                col_index = joga - 1
                if tabuleiro[0][col_index] == ' ':
                    for r in range(4, -1, -1):
                        if tabuleiro[r][col_index] == ' ':
                            tabuleiro[r][col_index] = simb
                            casas -= 1
                            break
                    break
                else:
                    joga = input('Essa coluna está cheia, escolha outra: ')
            except:
                joga = input('Tente novamente: ')

        acabou = verificar_se_ganhou()

    else:
        mostrar_tabuleiro()
        if not acabou:
            print('Empate')
        else:
            print(f'Ganhou {acabou}')


if __name__ == "__main__":
    jogo4linha()
