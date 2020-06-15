# AlphaSweeper
An AI that playes Minesweeper with winrate: beginner 89%, intermediate 87%, expert 40% (sample size = 3000)

#### Ranked #1 in UCI Spring 2020 CS171 Minesweeper AI tournament.

## Final Report PDF
https://github.com/Stevenhunter167/AlphaSweeper/blob/master/AlphaSweeper_Final_Report.pdf

## Overview:
/WorldGenerator

contains two .sh bash executable file that generates random boards with specific level of difficulties.

/dataset

contains some game history analysis and game data

/src

all the required file for running the AI

/src/MyAI.py

contains the AI logic

## AI routine:
phase 1: New game started
  1. MyAI instance gets constructed by the game
  2. constructor inputs
    1. board size
    2. first move location (garranteed to be safe)
    3. number of mines
  3. get action gets called with input of the number that was just unveiled
  
phase 2: During game:
  1. MyAI's getAction is called, which does the analysis of the result of last move (getAction inputs a number that was just uncoverd).
  2. return what MyAI believes is a good move by returning Action objects

phase 3: End of game
  1. Winning is when all the tiles that are not mines are uncoverd.
  2. Losing is when not all tiles that are not mines are uncoverd, and a mine is uncoverd.

