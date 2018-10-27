#!/usr/bin/env python3

import sys
import os
import tkinter

class Game:

    def __init__(self, window_width, window_height):
        self.window_width = window_width
        self.window_height = window_height
        self.window_xthreequarters = window_width // 1.5
        self.window_ythreequarters = window_height // 1.5
        self.window_xcenter = window_width // 2
        self.window_ycenter = window_height // 2
        self.window_xquarter = window_width // 4
        self.window_yquarter = window_height // 4
        self.gamecanvas = self.canvas = tkinter.Canvas(root, width=window_width,
                                        height=window_height, bg='papaya whip')
        self.canvas.pack()
        self.end = False

    def reset(self):
        root.destroy()
        #game.canvas.delete('game.gamecanvas')
        python = sys.executable
        os.execl(python, python, * sys.argv)


root = tkinter.Tk()
root.title('PongTk')
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
game = Game(screen_width // 2, screen_height // 2)
