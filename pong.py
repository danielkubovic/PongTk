#!/usr/bin/env python3

import time
import tkinter

from game import *
from paddle import *
from ball import *
from score import *


class Pong:

    def mainloop(self):
        root.wm_protocol("WM_DELETE_WINDOW", game.quit)
        ball.draw()
        left_paddle.draw()
        right_paddle.draw()
        game.start_timer()

        while not game.end:
            ball.draw()
            left_paddle.draw()
            right_paddle.draw()
            root.update()
            time.sleep(0.01)
        self.over()

    def over(self):
        finalscore1 = 'P1 score: ' + str(score.player1)
        finalscore2 = 'P2 score: ' + str(score.player2)

        if score.player1 > score.player2:
            winner = "Player 1 wins!"
        elif score.player1 < score.player2:
            winner = "Player 2 wins!"

        game.canvas.create_text(game.window_xcenter,
                                game.window_ycenter-60,
                                text=winner,
                                font=('Helvetica', 20))
        game.canvas.create_text(game.window_xcenter,
                                game.window_ycenter - 30, text=finalscore1,
                                font=('Helvetica', 20))
        game.canvas.create_text(game.window_xcenter,
                                game.window_ycenter, text=finalscore2,
                                font=('Helvetica', 20))

        self.reset = tkinter.Button(root, command=game.reset,
                                    text='Reset', font=('Helvetica', 18))
        self.reset.place(x=game.window_xcenter,
                         y=game.window_ycenter+40,
                         anchor=tkinter.CENTER)
        root.update_idletasks()


pong = Pong()
pong.mainloop()
root.mainloop()

