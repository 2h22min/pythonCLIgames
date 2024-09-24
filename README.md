# pythonCLIgames
Some python games exercises assigned in programming class at UAlg

## Overview
This CLI-based Python app offers a simple menu to select and play several classic games:
+ Tic-tac-toe (_Jogo do galo_);
+ Connect Four (_4 em linha_);
+ Game of the Goose (_Jogo da glória_);
+ Hangman (_Jogo da forca_);
+ Minesweeper (_Campo minado_);
+ Battleship (_Batalha naval_) (only in the [savable games](games)).

## Repository Structure
This repository contains a collection of exercises from a Programming class at the University of Algarve (UAlg) in 2023.\
It is organized into two main directories, each with its own _main.py_ program (and game modules) corresponding to the earlier or later exercises given:

### I. [games (non-savable)](https://github.com/2h22min/pythonCLIgames/tree/main/games%20(non-savable))
First exercises focused on building the games logic and each of the modules with functions.

### II. [games](games)
The same package with the addition of: 

+ The **Battleship Game**, with 2 modes:
    - Player vs. Computer
    - Player vs. player
+ The **Save Feature**, allowing players to interrupt and quit the program using `Ctrl + C` (saving the game state) at any point, and optionally resume a previous game the next time it's launched.

# Usage
## Setup
To run this project locally:

1. Clone the repository\
`git clone https://github.com/2h22min/pythonCLIgames.git`

1. Navigate to a games directory in the repo\
`cd pythonCLIgames/games`

1. Run main script to launch the game menu:\
`python main.py`

## Requirements
* Python 3.x