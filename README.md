Mastermind Game

A GUI-based implementation of the classic Mastermind code-breaking game, built in Python with Tkinter. Developed using Test-Driven Development.

How to Play

The program secretly chooses six distinct colors from a set of ten. The player tries to guess the exact colors and positions.

After each guess, the program gives feedback:

Black peg — a color is correct and in the correct position
Silver peg — a color is correct but in the wrong position

Example: if the program selected green, red, blue, white, orange, purple and the player guessed cyan, yellow, blue, orange, violet, red, the feedback would be black, silver, silver.

The player wins by guessing all six colors in the correct positions within 20 attempts. The player can also give up at any time, at which point the program reveals the answer.

Tech Stack
Python
Tkinter — GUI
unittest — test suite, written using TDD


