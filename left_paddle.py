#!/usr/bin/env python3

from paddle import *


class LeftPaddle(Paddle):

    def __init__(self, x, y, width, height, canvas, color):
        super().__init__(x, y, width, height, canvas, color)

    def draw(self):
        self.canvas.move(self.id, 0, self.speed)
        paddle_position = self.canvas.coords(self.id)
        # If paddle is not out of canvas, enable movement
        if paddle_position[1] > 0:
            self.canvas.bind_all('<KeyPress-w>', lambda event:
                                 self.move(event, self.active_speed * (-1)))
            self.canvas.bind_all('<KeyRelease-w>', self.stop_up)
        if paddle_position[3] < game.window_height:
            self.canvas.bind_all('<KeyPress-s>', lambda event:
                                 self.move(event, self.active_speed))
            self.canvas.bind_all('<KeyRelease-s>', self.stop_down)
        # If paddle is out of canvas, disable movement
        if paddle_position[1] <= 0:
            self.speed = 0
            self.canvas.unbind_all('<KeyPress-w>')
        if paddle_position[3] >= game.window_height:
            self.speed = 0
            self.canvas.unbind_all('<KeyPress-s>')

    # Paddle movement through x axis
    def move(self, evt, speed):
        self.speed = speed

    def stop_up(self, evt):
        if not self.speed > 0:
            self.speed = 0

    def stop_down(self, evt):
        if not self.speed < 0:
            self.speed = 0


left_paddle = LeftPaddle(game.window_xquarter // 2,
                         game.window_ycenter-game.window_yquarter // 2,
                         10, 100, game.canvas, 'green')

