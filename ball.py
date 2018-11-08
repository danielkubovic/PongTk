#!/usr/bin/env python3

import winsound

from game import *
from paddle import *
from left_paddle import *
from right_paddle import *
from score import *


class Ball:

    def __init__(self, x, y, color, canvas, left_paddle, right_paddle):
        self.canvas = canvas
        self.left_paddle = left_paddle
        self.right_paddle = right_paddle
        self.id = canvas.create_oval(0, 0, x, y, fill=color)
        self.canvas.move(self.id, game.window_xcenter, game.window_ycenter)
        self.xspeed = -5
        self.yspeed = -5

    def draw(self):
        self.canvas.move(self.id, self.xspeed, self. yspeed)
        ball_position = self.canvas.coords(self.id)
        if ball_position[1] <= 0 or ball_position[3] >= game.window_height:
            self.yspeed *= -1
        if ball_position[0] <= 0:
            self.xspeed *= -1
            score.player2 += 1
            game.canvas.itemconfig(score.board_player2,
                                   text=str(score.player2))
        if ball_position[2] >= game.window_width:
            self.xspeed *= -1
            score.player1 += 1
            game.canvas.itemconfig(score.board_player1,
                                   text=str(score.player1))

        if self.hit_paddle(ball_position):
            self.xspeed *= -1
            winsound.PlaySound('sound\hit.wav', winsound.SND_ASYNC)

        if score.player1 is score.final or score.player2 is score.final:
            game.canvas.delete(score.board_player1, score.board_player2,
                               score.board)
            game.end = True

    def hit_paddle(self, ball_pos):
        left_paddle_pos = self.canvas.coords(self.left_paddle.id)
        right_paddle_pos = self.canvas.coords(self.right_paddle.id)

        if ball_pos[1] >= left_paddle_pos[1] \
           and ball_pos[3] <= left_paddle_pos[3] \
           and ball_pos[0] <= left_paddle_pos[2]:
            return True

        if ball_pos[1] >= right_paddle_pos[1] \
           and ball_pos[3] <= right_paddle_pos[3] \
           and ball_pos[2] >= right_paddle_pos[0]:
            return True


ball = Ball(15, 15, 'red', game.canvas, left_paddle, right_paddle)

