"""Exercício
(a) Faça um programa que permite selecionar e jogar os seguintes jogos (use funções):
    Jogo do galo;
    Jogo 4 em linha;
    Jogo da gloria;
    Jogo da forca;
    Jogo campo de minas (https://pt.wikipedia.org/wiki/Campo_minado).
(b) Cada vez que que pretende terminar sair de qualquer dos jogos sem o ter
terminado, deve guardar o status do jogo (use ficheiros). O mesmo acontece quando
pretende terminar o programa.
Cada vez que entra no jogo deve ser perguntado se pretende continuar o jogo
anterior (caso tenha saído a meio) ou se pretende iniciar um novo jogo.
. Deve guardar:
    - o nome dos jogadores que estão a jogar;
    - a pontuação por jogo e total;
Quando iniciar o programa deve ser perguntado se quer começar nova “sessão de
jogos” ou se pretende continuar uma que tenha guardado.
(c) Use programação modular. Cada um dos jogos referidos em (a) deve estar num
“ficheiro separado”.
"""

import json
import jogoGalo
import jogo4linha
import jogoGloria
import jogoForca
import minesweeper
import battleship 


abc = 'abcdefghijklmnopqrstuvwxyz'
jogos = [ {'nome': 'Jogo do galo',
          'vsPC': False,
          'func': jogoGalo.jogoGalo},
          {'nome': 'Jogo 4 em linha',
          'vsPC': False,
          'func': jogo4linha.jogo4linha},
          {'nome': 'Jogo da gloria',
          'vsPC': False,
          'func': jogoGloria.jogoGloria},
          {'nome': 'Jogo da forca',
          'vsPC': False,
          'func': jogoForca.jogoForca},
          {'nome': 'Jogo campo de minas',
          'vsPC': False,
          'func': minesweeper.jogoCampoMinado},
          {'nome': 'Jogo batalha naval',
          'vsPC': True,
          'func': battleship.jogoBatalhaNaval},
          ]
for module, i in zip(
        [jogoGalo, jogo4linha, jogoGloria, jogoForca, minesweeper, battleship],
    range(len(jogos)), strict=True):
    jogos[i]['savename'] = module.savename

while True:
    try:
        print('\nSelecione jogo:')
        for jogo in range(len(jogos)):
            print(abc[jogo] + '.', jogos[jogo]['nome'])
        print('Use "Control + C" para sair em qualquer momento.')

        try:
            i = abc.index(input().lower())
            if i >= len(jogos):
                raise ValueError
        # Continue while loop, until a valid option is selected
        except ValueError:
            continue

        # If it's a game playable against computer, select the mode
        vsPC = None
        if jogos[i]['vsPC']:
            print('Escolha modo de jogo:')
            while True:
                match input(' a. Jogador vs Computador\n b. Jogador vs Jogador\n').lower():
                    case 'a':
                        vsPC = True
                        jogos[i]['savename'] = jogos[i]['savename'][:-6] + "C.json"
                        break
                    case 'b':
                        vsPC = False
                        # Update savename in dict because default is vs. PC mode
                        jogos[i]['savename'] = jogos[i]['savename'][:-6] + "J.json"
                        break

        # Check if there's a save of the selected game before starting
        data = None
        try:
            with open(jogos[i]['savename'],'x') as jsonfile:
                jsonfile.write('{}')

        except FileExistsError:
            with open(jogos[i]['savename']) as jsonGuardado:
                data = json.load(jsonGuardado)

            if len(data) > 0:
                if input('Escreva "S" se pretende continuar o jogo anterior ou enter para iniciar um novo.\n'
                        ).lower() != 's':
                    data = None
            else:
                    data = None
                    
        finally:
            if vsPC is not None:
                jogos[i]['func'](vsPC, resume = data)
            else:
                jogos[i]['func'](resume = data)

    except KeyboardInterrupt:
        break
