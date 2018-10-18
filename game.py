#!/usr/bin/env python3

import tkinter

class Game:

    def __init__(self, window_width, window_height):
        self.window_width = window_width
        self.window_height = window_height
        self.window_xcenter = window_width // 2
        self.window_ycenter = window_height // 2
        self.window_xquarter = window_width // 4
        self.window_yquarter = window_height // 4
        self.gamecanvas = self.canvas = tkinter.Canvas(root, width=window_width,
                                        height=window_height, bg='papaya whip')
        self.score = self.canvas.create_text(5, 5, font=('Helvetica', '15'),
                                            anchor='nw', text='Score: 0')
        self.canvas.pack()


root = tkinter.Tk()
root.title('Pong')
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
game = Game(screen_width // 2, screen_height // 2)
