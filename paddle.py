#!/usr/bin/env python3

from game import *


class Paddle:

    def __init__(self, x, y, width, height, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, width, height, fill=color)
        self.canvas.move(self.id, x, y)
        self.active_speed = 2
        self.speed = 0

