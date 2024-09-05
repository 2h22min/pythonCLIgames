"""Exercício
Faça um programa que permite selecionar e jogar os seguintes jogos (use funções):
(a) Jogo do galo;
(b) Jogo 4 em linha;
(c) Jogo da gloria (ex. https://i.pinimg.com/originals/db/5f/89/db5f8973323b0c78a1d96d69563491f7.jpg);
+ Jogo da forca;
+ Jogo campo de minas (https://pt.wikipedia.org/wiki/Campo_minado)
"""

from jogoGalo import jogoGalo
from jogo4linha import jogo4linha
from jogoGloria import jogoGloria
from jogoForca import jogoForca
from minesweeper import jogoCampoMinado


jogos = {
    'a': jogoGalo,
    'b': jogo4linha,
    'c': jogoGloria,
    'd': jogoForca,
    'e': jogoCampoMinado,
}

while True:
    print('\nSelecione jogo:\n a. Jogo do galo\n b. Jogo 4 em linha\n c. Jogo da gloria\
          \n d. Jogo da forca\n e. Jogo campo de minas')
    try:
        jogos[input().lower()]()
    except KeyError:
        break
