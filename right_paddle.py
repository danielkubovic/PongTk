#!/usr/bin/env python3

from paddle import *

class RightPaddle(Paddle):

    def __init__(self, x, y, width, height, canvas, color):
        super().__init__(x, y, width, height, canvas, color)

    def draw(self):
        self.canvas.move(self.id, 0, self.speed)
        paddle_position = self.canvas.coords(self.id)
        # If paddle is not touching the edge of canvas, enable that movement button
        if paddle_position[1] > 0:
            self.canvas.bind_all('<KeyPress-Up>', lambda event: self.move(event, self.active_speed * (-1)))
            self.canvas.bind_all('<KeyRelease-Up>', self.stop_up)
        if paddle_position[3] < game.window_height:
            self.canvas.bind_all('<KeyPress-Down>', lambda event: self.move(event, self.active_speed))
            self.canvas.bind_all('<KeyRelease-Down>', self.stop_down)
        # If paddle is touching the edge of canvas, disable that movement button
        if paddle_position[1] <= 0:
            self.speed = 0
            self.canvas.unbind_all('<KeyPress-Up>')
        if paddle_position[3] >= game.window_height:
            self.speed = 0
            self.canvas.unbind_all('<KeyPress-Down>')

    # Paddle movement through x axis
    def move(self, evt, speed):
        self.speed = speed
    def stop_up(self, evt):
        if not self.speed > 0:
            self.speed = 0
    def stop_down(self, evt):
        if not self.speed < 0:
            self.speed = 0


right_paddle = RightPaddle(game.window_xthreequarters * 1.3, game.window_ycenter, 10, 100, game.canvas, 'blue')
