'''Exercício
Jogo da batalha naval (https://pt.wikipedia.org/wiki/Batalha_naval_(jogo)), com 2 vertentes:
(a) Jogador vs Computador: o computador deve escolher a posição onde são
colocados os barcos, o computador escolhe as posições dos tiros aleatoriamente
(opção: ou com algumas regras).
(b) Jogador1 vs Jogador2: cada jogador escolhe a posição dos seus barcos.
'''

import json
import random
import time


def jogoBatalhaNaval():
    class board():
        def __init__(self):
            self.rows = []
            for row in range(10):
                self.rows.append(['-','-', '-','-', '-','-', '-','-', '-','-'])

        def show(self):
            for row in range(len(self.rows)-1, -1, -1):
                print(row,end='  ')
                for pos in self.rows[row]:
                    print(f'|_{pos}',end='_')
                print()
            print('     A   B   C   D   E   F   G   H   I   J\n\n')

    class player():
        def __init__(self, nome, shipsboard, attackboard, human = True):
            self.nome = nome

            nomesBarcos = ["Porta-aviões", "Navio-tanque",
            "Contratorpedeiro", "Submarino", "Navio-patrulha"]
            self.ships = []

            for squares in range( 5, 0, -1):
                self.ships.append({
                    'nome': nomesBarcos[ -squares],
                    'squares': 0,
                    'A': [],
                    'B': [],
                    'pos': []})
                self.ships[-1]['squares'] = squares
                for square in range(squares):
                    self.ships[-1]['pos'].append([])
                
                if squares < 3:
                    self.ships[-1]['squares'] += 1
                    self.ships[-1]['pos'].append([])

            self.turn = False
            self.won = False

            self.shipsboard = shipsboard
            self.attackboard = attackboard
            self.bot = not human
        
        def shipsquares(self):
            somaq = 0
            for ship in self.ships:
                somaq += ship['squares']
            return somaq

    def boards(jogador):
        '''Prints the user's main board (with their own ships) and their attack board (with their attacks to the enemy ships).'''
        jogador.attackboard.show()
        jogador.shipsboard.show()
        time.sleep(0.8)

    def mensagem_grande(msg):
        print(f"""





                          
            {msg}


                          



                    """)
        time.sleep(1.2)

    def yx_to_str(posyx):
        '''Converts a position list with row (0) and column (1) elements to an "A4" type of string.'''
        row = str(posyx[0])
        match posyx[1]:
            case 0:
                col = 'A'
            case 1:
                col = 'B'
            case 2:
                col = 'C'
            case 3:
                col = 'D'
            case 4:
                col = 'E'
            case 5:
                col = 'F'
            case 6:
                col = 'G'
            case 7:
                col = 'H'
            case 8:
                col = 'I'
            case 9:
                col = 'J'
        return f'{col}{row}'

    def valid_pos_input(inp):
        '''Confirms a valid "A1" kind of input string and converts it to a position list with 2 elements (row, and then column).'''
        while 1:
            try:
                row = int(inp[1])
                col = inp[0]
                if col == 'a':
                    col = 0
                elif col == 'b':
                    col = 1
                elif col == 'c':
                    col = 2
                elif col == 'd':
                    col = 3
                elif col == 'e':
                    col = 4
                elif col == 'f':
                    col = 5
                elif col == 'g':
                    col = 6
                elif col == 'h':
                    col = 7
                elif col == 'i':
                    col = 8
                elif col == 'j':
                    col = 9
                else:
                    raise ValueError

                return [row, col]

            except ValueError:
                inp = input('Error. Tente novamente. ').lower()
            except IndexError:
                inp = input('Error. Tente novamente. ').lower()


    def place(ship, board, user = True):
        '''Places ship in own player's board.'''
        nonlocal possible_position
        squares = ship['squares']
        right_dir = [ship['A'][0], ship['A'][1] + squares - 1]
        up_dir = [ship['A'][0] + squares - 1, ship['A'][1]]
        left_dir = [ship['A'][0], ship['A'][1] - squares + 1]
        down_dir = [ship['A'][0] - squares + 1, ship['A'][1]]
        end_options = [right_dir, up_dir, left_dir, down_dir]

        final_options = []
        for dir in range(4):
            pos = [ship['A'][0], ship['A'][1]]
            for square in range(squares):
                match dir:
                    case 0:
                        pos[1] = ship['A'][1] + square
                    case 1:
                        pos[0] = ship['A'][0] + square
                    case 2:
                        pos[1] = ship['A'][1] - square
                    case 3:
                        pos[0] = ship['A'][0] - square
        
                if pos[0] >= 0 and pos[0] <= 9 and pos[1] >= 0 and pos[1] <= 9:
                    if board.rows[pos[0]][pos[1]] == '-':
                        if square == squares - 1:
                            final_options.append(end_options[dir])
                    else:
                        break
                else:
                    break
        
        if final_options == []:
            if user:
                print('Não é possível colocar o seu barco com uma extremidade nesse ponto. Tente noutro lado')
        else:
            possible_position = True

            if user:
                str_options = ''
                for finaloption in range(len(final_options)):
                    str_options += f'{yx_to_str(final_options[finaloption])}'
                    if finaloption < len(final_options) - 2:
                        str_options += ', '
                    elif finaloption == len(final_options) - 2:
                        str_options += ' ou '

                pos2_input = input(f'Onde gostaria de colocar a outra extremidade do seu barco? Escreva {str_options}.\n').lower()
                while 1:
                    posB = valid_pos_input(pos2_input)
                    if posB not in final_options:
                        pos2_input = input(f'Error. Escreva {str_options}.\n').lower()
                    else:
                        ship['B'] = posB
                        break

            else:
                ship['B'] = random.choice(final_options)

            if ship['A'][0] == ship['B'][0]:
                if ship['A'][1] < ship['B'][1]:
                    for square in range(squares):
                        board.rows[ship['A'][0]][ship['A'][1] + square] = '#'
                        ship['pos'][square] = [ship['A'][0], ship['A'][1] + square]
                else:
                    for square in range(squares):
                        board.rows[ship['A'][0]][ship['B'][1] + square] = '#'
                        ship['pos'][square] = [ship['A'][0], ship['B'][1] + square]
            else:
                if ship['A'][0] < ship['B'][0]:
                    for square in range(squares):
                        board.rows[ship['A'][0] + square][ship['A'][1]] = '#'
                        ship['pos'][square] = [ship['A'][0] + square, ship['A'][1]]
                else:
                    for square in range(squares):
                        board.rows[ship['B'][0] + square][ship['A'][1]] = '#'
                        ship['pos'][square] = [ship['B'][0] + square, ship['A'][1]]

    def attack(pos, board, playr):
        '''Player attacks a position in their board.'''
        playing = playr.nome
        if playr == jogA:
            enemy_board = jogB.shipsboard
            enemy = jogB
        else:
            enemy_board = jogA.shipsboard
            enemy = jogA

        hit = False
        if board.rows[pos[0]][pos[1]] == '-':
            for ship in enemy.ships:
                if hit: break
                if ship['squares'] == 0:
                    continue
                for square in ship['pos']:
                    if pos == square:
                        if playr.bot:
                            playr.tracking.append(pos)
                        board.rows[pos[0]][pos[1]] = '@' # marca no próprio tabuleiro que há barco naquele quadrado
                        enemy_board.rows[pos[0]][pos[1]] = '!'
                        ship['squares'] -= 1
                        if ship['squares'] > 0:
                            print(f'Atingiu!',end=' ')
                        else:
                            print(f'{playing} afundou um navio!',end=' ')
                            if playr.bot:
                                playr.tracking = []
                        if enemy.shipsquares() > 0:
                            print(f'{playing} joga outra vez.')
                        else:
                            print()
                            playr.turn = False
                            playr.won = True
                        hit = True
                        break
            if not hit:
                if playr.bot:
                    if len(playr.tracking) > 1:
                        playr.times_dir_switched.append(1)
                        if len(playr.times_dir_switched) > 2:
                            playr.tracking = []
                            playr.times_dir_switched = []
                board.rows[pos[0]][pos[1]] = 'X' # marca no próprio tabuleiro que há água naquele quadrado
                enemy_board.rows[pos[0]][pos[1]] = 'X'
                print(f'{playing} falhou!')
                playr.turn = False
            time.sleep(1.4)
            print()
            if not playr.bot:
                boards(playr)
        else:
            if not playr.bot:
                print('Já atacou esta posição! Tente noutro sítio.')
            return False
        return hit

    try:
        print('Escolha modo de jogo:')
        while True:
            match input(' a. Jogador vs Computador\n b. Jogador vs Jogador\n').lower():
                case 'a':
                    vsComputador = True
                    savename = "saves/save_jogoBatalhaNaval_JcC.json"
                    break

                case 'b':
                    vsComputador = False
                    savename = "saves/save_jogoBatalhaNaval_JcJ.json"
                    break

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
                        jAdict = data["jog A"]
                        sboard_A = board()
                        sboard_A.rows = jAdict['shipsboard']
                        aboard_A = board()
                        aboard_A.rows = jAdict['attackboard']
                        jogA = player( jAdict['nome'], sboard_A, aboard_A, not jAdict['bot'])
                        jogA.ships = jAdict['ships']
                        jogA.turn = jAdict['turn']
                        jogA.won = jAdict['won']

                        jBdict = data["jog B"]
                        sboard_B = board()
                        sboard_B.rows = jBdict['shipsboard']
                        aboard_B = board()
                        aboard_B.rows = jBdict['attackboard']
                        jogB = player( jBdict['nome'], sboard_B, aboard_B, not jBdict['bot'])
                        jogB.ships = jBdict['ships']
                        jogB.turn = jBdict['turn']
                        jogB.won = jBdict['won']
                        if vsComputador:
                            jogB.tracking = jBdict['tracking']
                            jogB.times_dir_switched = jBdict['times_dir_switched']
                        
                        vez = data['vez']

                    else:
                        novojogo = True
                else:
                    novojogo = True
        finally:          
            if novojogo:
                sboard_A = board()
                aboard_A = board()
                sboard_B = board()
                aboard_B = board()

                possible_position = False

                if vsComputador:
                    jogA = player('O utilizador', sboard_A, aboard_A)
                    jogB = player('O computador', sboard_B, aboard_B, False)
                    jogB.tracking = []
                    jogB.times_dir_switched = []

                    # bot ships positioning
                    for ship in jogB.ships:
                        while not possible_position:
                            ship['A'] = [random.randrange(12 - ship['squares']), random.randrange(12 - ship['squares'])] 
                            place(ship, sboard_B, False)
                        possible_position = False

                else:                    
                    jogA = player( input('Nome do jogador 1: '), sboard_A, aboard_A)
                    while True:
                        segundoJNome = input('Nome do jogador 2: ')
                        if segundoJNome != jogA.nome:
                            jogB = player(segundoJNome, sboard_B, aboard_B)
                            break
                        else:
                            print('Os jogadores devem ter nomes diferentes.')
                       
                # first player ships positioning
                for ship in range(5):
                    while not possible_position:
                        sboard_A.show()
                        b = jogA.ships[ship]
                        b['A'] = valid_pos_input( input( f'{jogA.nome}, onde gostaria de colocar \
o seu {b['nome']} ({b['squares']} quadrados)? Escreva uma das suas posições finais como "A1"\n').lower())
                        place(b, sboard_A)
                    possible_position = False
                
                # second player ships positioning
                if not vsComputador:
                    mensagem_grande("Barcos do primeiro jogador colocados")
                    for ship in range(5):
                        while not possible_position:
                            sboard_B.show()
                            b = jogB.ships[ship]
                            b['A'] = valid_pos_input(input(f'{jogB.nome}, onde gostaria de colocar\
o seu {b['nome']} ({b['squares']} quadrados)? Escreva uma das suas posições finais como "A1"\n').lower())
                            place(jogB.ships[ship], sboard_B)
                        possible_position = False
                                    
                mensagem_grande("Todos os barcos colocados")
            
            mensagem_grande('')

        while jogA.shipsquares() > 0 and jogB.shipsquares() > 0:
            for jogador in [jogA, jogB]:
                if not novojogo:
                    if vez != jogador.nome:
                        continue
                    else:
                        novojogo = True
                else:
                    vez = jogador.nome

                jogador.turn = True
                mensagem_grande(f"Joga {jogador.nome.lower()}")
                if not vsComputador:
                    mensagem_grande('"Enter" para continuar...')
                    input()

                if not jogador.bot:
                    boards(jogador)
                    while jogador.turn:
                        attack_square = valid_pos_input(input('Escreva uma posição como "A1" para atacar o seu inimigo\n'))
                        attack(attack_square, jogador.attackboard, jogador)
                        time.sleep(2)

                else:
                    while jogador.turn:
                        if len(jogador.tracking) == 0:
                            attack_square = [random.randint(0,9), random.randint(0,9)]
                        elif len(jogador.tracking) == 1:
                            while 1:
                                if random.randint(0, 1) > 0:
                                    attack_square = [jogador.tracking[0][0] + random.choice([-1, 1]), jogador.tracking[0][1]]
                                else:
                                    attack_square = [jogador.tracking[0][0], jogador.tracking[0][1] + random.choice([-1, 1])]
                                
                                if (attack_square[0] >= 0 and attack_square[0] <= 9 and
                                    attack_square[1] >= 0 and attack_square[1] <= 9):
                                    break
                        else:
                            if len(jogador.times_dir_switched) == 1:
                                prevpos = jogador.tracking[0]
                                prev2pos = jogador.tracking[1]
                                jogador.times_dir_switched.append(1)
                            else:
                                prevpos = jogador.tracking[-1]
                                if (prevpos[0] - jogador.tracking[0][0])**2 == 1 or (prevpos[1] - jogador.tracking[0][1])**2 == 1:
                                    prev2pos = jogador.tracking[0]
                                else:
                                    prev2pos = jogador.tracking[-2]
                            if jogador.tracking[0][0] == jogador.tracking[1][0]: # se o barco está horizontal
                                attack_square = [jogador.tracking[0][0], prevpos[1] - (prev2pos[1] - prevpos[1])]
                            else: # caso vertical 
                                attack_square = [prevpos[0] - (prev2pos[0] - prevpos[0]), jogador.tracking[0][1]]
                            
                            if (attack_square[0] < 0 or attack_square[0] > 9 or
                                attack_square[1] < 0 or attack_square[1] > 9):
                                jogador.tracking = []
                                jogador.times_dir_switched = []
                                attack_square = [random.randint(0,9), random.randint(0,9)]


                        if not attack(attack_square, jogador.attackboard, jogador) and len(jogador.tracking) > 1:
                            jogador.tracking = []
                            jogador.times_dir_switched = []

                if jogador.won:
                    winner = jogador
                    break
            
        mensagem_grande(f'\n{winner.nome} ganhou!')
        boards(winner)

        with open(savename, "w") as json_save:
            json.dump({}, json_save)

    except KeyboardInterrupt:
        try:
            save_dict = {
                "jog A": jogA.__dict__,
                "jog B": jogB.__dict__,
                "vez": vez
            }
            save_dict['jog A']['shipsboard'] = save_dict['jog A']['shipsboard'].rows
            save_dict['jog B']['shipsboard'] = save_dict['jog B']['shipsboard'].rows
            save_dict['jog A']['attackboard'] = save_dict['jog A']['attackboard'].rows
            save_dict['jog B']['attackboard'] = save_dict['jog B']['attackboard'].rows
            
            
            with open(savename, "w") as json_save:
                json.dump(save_dict, json_save)

        except UnboundLocalError:
            pass


if __name__ == "__main__":
    jogoBatalhaNaval()
