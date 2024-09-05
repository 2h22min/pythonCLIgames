'''Exercício 4
Implemente o algoritmo e implemente o programa do jogo galo (jogo da velha ou três
em linha) (https://pt.wikipedia.org/wiki/Jogo_da_velha).
'''

import json

def jogoGalo():
    savename = 'saves/save_jogoGalo.json'
    
    try:
        novojogo = False
        try:
            with open(savename,'x') as jsonfile:
                jsonfile.write('{}')
            novojogo = True

        except FileExistsError:
            with open(savename) as jsonGuardado:
                data = json.load(jsonGuardado)
                if len(data) > 0:
                    if input('Escreva "S" se pretende continuar o jogo anterior ou enter para iniciar um novo.\n').lower() == 's':
                        jogador1 = data['jogadores'][0]
                        jogador2 = data['jogadores'][1]
                        tabela = data['tabela']
                    else:
                        novojogo = True
                else:
                    novojogo = True
        finally:          
            if novojogo:
                jogador1 = input('Nome 1: ')
                jogador2 = input('Nome 2: ')
                tabela = [9, [' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
            
            ganhou = ''

        while tabela[0] >= 0:
            for row in range(len(tabela)):
                if row == 0:
                    print('\n   A   B   C')
                else:
                    print(f'   {tabela[row][0]} | {tabela[row][1]} | {tabela[row][2]}')
                    print(f'{row} ___|___|___')

            if ganhou != '' or tabela[0] == 0:
                break

            if tabela[0] % 2 == 0:
                simb = 'O'
                aJogar = jogador1
            else:
                simb = 'X'
                aJogar = jogador2
            pos = input(f'{aJogar} ({simb}), insira posição na forma "B2": ').lower()
            while True:
                try:
                    pos_row = int(pos[1])
                    if pos_row < 1 or pos_row > 3:
                        raise ValueError
                    match pos[0]:
                        case 'a':
                            pos_col = 0
                        case 'b':
                            pos_col = 1
                        case 'c':
                            pos_col = 2
                        case _:
                            raise ValueError
                except:
                    pos = input(f'Erro. Insira posição na forma "B2": ').lower()
                    continue

                if tabela[pos_row][pos_col] == ' ':
                    tabela[pos_row][pos_col] = simb
                    tabela[0] -= 1
                    break
                else:
                    pos = input(f'Erro. Insira uma posição livre: ').lower()

            for row in tabela:
                if row == tabela[0]:
                    continue
                if (row[0] != ' ' and
                row[0] == row[1] and row[1] == row[2]):
                    ganhou = row[0]
                    break

            for col in range(3):
                if (tabela[1][col] != ' ' and
                tabela[1][col] == tabela[2][col] and tabela[2][col] == tabela[3][col]):
                    ganhou = tabela[1][col]
                    break

            if (tabela[2][1] != ' '
            and ((tabela[1][0] == tabela[2][1] and tabela[2][1] == tabela[3][2])
            or (tabela[1][2] == tabela[2][1] and tabela[2][1] == tabela[3][0])
            )):
                ganhou = tabela[2][1]

        if ganhou != '':
            print(f'Ganhou {ganhou}')
        else:
            print('Empate')
            
        with open(savename, "w") as json_save:
            json.dump({}, json_save)

    except KeyboardInterrupt:
        try:
            save_dict = {
                "jogadores": (jogador1, jogador2),
                "tabela": tabela         
            }
            with open(savename, "w") as json_save:
                json.dump(save_dict, json_save)
        except UnboundLocalError:
            pass


if __name__ == "__main__":
    jogoGalo()
