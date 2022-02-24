"""Test script for the game board.
"""

from __future__ import print_function
from minesweeper.msgame import MSGame
import os

game = MSGame(10, 10, 5)

game.help()

print(game.get_mine_map())
print(game.get_info_map())



while game.game_status == 2:
    # play move
    # clear = lambda: os.system('cls')
    # clear()
    game.print_board()
    move = input("Move: ")
    game.play_move_msg(move)
    print(game.get_info_map())


