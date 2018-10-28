#!/usr/bin/env python3

from game import *


class Score:

    def __init__(self):
        self.player1 = 0
        self.player2 = 0
        self.board_player1 = game.canvas.create_text(game.window_xcenter-25, 5,
                                                     font=('Helvetica', '30'),
                                                     anchor='nw', text='0')
        self.board = game.canvas.create_text(game.window_xcenter, 5,
                                             font=('Helvetica', '30'),
                                             anchor='nw', text='-')
        self.board_player2 = game.canvas.create_text(game.window_xcenter+17, 5,
                                                     font=('Helvetica', '30'),
                                                     anchor='nw', text='0')


score = Score()

