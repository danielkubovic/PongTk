#!/usr/bin/env python3

import os
import sys
import time
import tkinter
from game import *
from ball import *
from paddle import *

# Clasic pong game
class Pong:

    def __init__(self):
        self.running = True

    def quit(self):
        root.destroy()
        sys.exit()

    def mainloop(self):
        while self.running is True:
            root.wm_protocol("WM_DELETE_WINDOW", self.quit)
            while not ball.hit_bottom:
                ball.draw()
                paddle.draw()
                root.update()
                time.sleep(0.01)
            self.game_over()
            self.running = False

    def again(self):
        root.destroy()
        #game.canvas.delete('game.gamecanvas')
        python = sys.executable
        os.execl(python, python, * sys.argv) 

    def game_over(self):
        finalscore = 'Score: ' + str(ball.player_score)
        game_over = game.canvas.create_text(game.window_xcenter,
                                            game.window_ycenter - 30,
                                            text='Game over',
                                            font=('Helvetica', 20))
        score = game.canvas.create_text(game.window_xcenter,
                                        game.window_ycenter, text=finalscore,
                                        font=('Helvetica', 20))
        try_again = tkinter.Button(root, command=self.again, text='Try again',
                                   font=('Helvetica', 18))
        try_again.place(x=game.window_xcenter,
						y=game.window_ycenter + 40,
						anchor=tkinter.CENTER)
        root.update_idletasks()


pong = Pong()
pong.mainloop()
root.mainloop()
