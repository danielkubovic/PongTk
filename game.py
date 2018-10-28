#!/usr/bin/env python3

import os
import sys
import time
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
        self.canvas = tkinter.Canvas(root, width=window_width,
                                     height=window_height, bg='papaya whip')
        self.canvas.pack()
        self.end = False

    def quit(self):
        root.destroy()
        sys.exit()

    def reset(self):
        root.destroy()
        python = sys.executable
        os.execl(python, python, * sys.argv)
    '''
    def options(self):
        pass
        root.attributes("-fullscreen", True)
    '''

    def start_timer(self):
        for i in range(3, 0, -1):
            timer = self.canvas.create_text(self.window_xcenter,
                                            self.window_ycenter, text=str(i),
                                            font=('Helvetica', 40))
            root.update()
            time.sleep(1)
            self.canvas.delete(timer)


root = tkinter.Tk()
root.title('PongTk')
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
game = Game(screen_width // 1.5, screen_height // 1.5)

