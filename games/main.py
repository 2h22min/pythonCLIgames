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
from jogoGalo import jogoGalo
from jogo4linha import jogo4linha
from jogoGloria import jogoGloria
from jogoForca import jogoForca
from minesweeper import jogoCampoMinado
from battleship import jogoBatalhaNaval


abc = 'abcdefghijklmnopqrstuvwxyz'
jogos = [ {'nome': 'Jogo do galo',
          'func': jogoGalo},
          {'nome': 'Jogo 4 em linha',
          'func': jogo4linha},
          {'nome': 'Jogo da gloria',
          'func': jogoGloria},
          {'nome': 'Jogo da forca',
          'func': jogoForca},
          {'nome': 'Jogo campo de minas',
          'func': jogoCampoMinado},
          {'nome': 'Jogo batalha naval',
          'func': jogoBatalhaNaval},
          ]

while True:
    print('\nSelecione jogo:')
    for jogo in range(len(jogos)):
        print(abc[jogo] + '.', jogos[jogo]['nome'])
    print('Use as teclas "Control" + "C" para sair em qualquer momento.')
    try:
        i = abc.index(input().lower())
        jogos[i]['func']()
    except (ValueError, IndexError, KeyboardInterrupt):
        break
    