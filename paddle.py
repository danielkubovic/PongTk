#!/usr/bin/env python3

from game import *

class Paddle:

    def __init__(self, length, width, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, length, width, fill=color)
        self.canvas.move(self.id, 200, game.window_xcenter)
        self.speed = 3
        self.xspeed = 0
        self.yspeed = 0

    def draw(self):
        self.canvas.move(self.id, self.xspeed, self.yspeed)
        paddle_position = self.canvas.coords(self.id)
        # If paddle is not touching the edge of canvas, enable that movement button
        if paddle_position[0] > 0:
            self.canvas.bind_all('<KeyPress-Left>',
            lambda event, arg=("x"): self.move(event, arg, self.speed * (-1)))
            self.canvas.bind_all('<KeyRelease-Left>', self.stop_left)
        if paddle_position[2] < game.window_width:
            self.canvas.bind_all('<KeyPress-Right>', lambda event, arg=("x"):
									self.move(event, arg, self.speed))
            self.canvas.bind_all('<KeyRelease-Right>', self.stop_right)
        if paddle_position[1] > 0:
            self.canvas.bind_all('<KeyPress-Up>', lambda event, arg=("y"):
									self.move(event, arg, self.speed * (-1)))
            self.canvas.bind_all('<KeyRelease-Up>', self.stop_up)
        if paddle_position[3] < game.window_width:
            self.canvas.bind_all('<KeyPress-Down>', lambda event,
								arg=("y"): self.move(event, arg, self.speed))
            self.canvas.bind_all('<KeyRelease-Down>', self.stop_down)
        # If paddle is touching the edge of canvas, disable that movement button
        if paddle_position[1] <= game.window_ycenter:
            self.yspeed = 0
            self.canvas.unbind_all('<KeyPress-Up>')
        if paddle_position[3] >= game.window_height:
            self.yspeed = 0
            self.canvas.unbind_all('<KeyPress-Down>')
        if paddle_position[0] <= 0:
            self.xspeed = 0
            self.canvas.unbind_all('<KeyPress-Left>')
        if paddle_position[2] >= game.window_width:
            self.xspeed = 0
            self.canvas.unbind_all('<KeyPress-Right>')

    # Paddle movement through x, y axis
    def move(self, evt, axis, speed):
        if axis is "x":
            self.xspeed = speed
        elif axis is "y":
            self.yspeed = speed
    def stop_left(self, evt):
        if not self.xspeed > 0:
            self.xspeed = 0
    def stop_right(self, evt):
        if not self.xspeed < 0:
            self.xspeed = 0
    def stop_up(self, evt):
        if not self.yspeed > 0:
            self.yspeed = 0
    def stop_down(self, evt):
        if not self.yspeed < 0:
            self.yspeed = 0


paddle = Paddle(100, 10, game.canvas, 'blue')
