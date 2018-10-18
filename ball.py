#!/usr/bin/env python3

import random
import winsound
from game import *
from paddle import *

class Ball:

    def __init__(self, canvas, color, size, paddle):
        self.canvas = canvas
        self.paddle = paddle
        self.id = canvas.create_oval(0, 0, size, size, fill=color)
        self.canvas.move(self.id, 245, 100)
        self.xspeed = random.randrange(-3,3)
        self.yspeed = -3
        self.player_score = 0
        self.hit_bottom = False

    def draw(self):
        self.canvas.move(self.id, self.xspeed, self.yspeed)
        ball_position = self.canvas.coords(self.id)
        if ball_position[1] <= 0:
            self.yspeed = 3
        if ball_position[3] >= game.window_height:
            self.hit_bottom = True
        if ball_position[0] <= 0:
            self.xspeed = 3
        if ball_position[2] >= game.window_width:
            self.xspeed = -3
        if self.hit_paddle(ball_position) == True:
            self.yspeed = -3
            self.xspeed = random.randrange(-3,3)
            self.player_score += 1
            game.canvas.itemconfig(game.score, text='Score: '
                                    + str(self.player_score))
            winsound.PlaySound('sound/hit.wav', winsound.SND_ASYNC)

    def hit_paddle(self, ball_position):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if ball_position[2] >= paddle_pos[0] and ball_position[0] <= paddle_pos[2]:
            if ball_position[3] >= paddle_pos[1] and ball_position[3] <= paddle_pos[3]:
                return True
        return False


ball = Ball(game.canvas, 'red', 15, paddle)
