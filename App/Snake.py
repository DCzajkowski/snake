from config import *

class Snake:
    width = 0
    headX = None
    headY = None
    headXChange = 0
    headYChange = 0

    def __init__(self, width = SNAKE_WIDTH, headX = 0, headY = 0):
        self.width = width
        self.headX = headX
        self.headY = headY

    def moveHead(self, x, y):
        self.headX += x
        self.headY += y

    def setHeadChange(self, x, y):
        if x is not None:
            self.headXChange = x
        if y is not None:
            self.headYChange = y

    def reset(self):
        self.headX = WINDOW_WIDTH / 2
        self.headY = WINDOW_HEIGHT / 2
        self.headXChange = 0
        self.headYChange = 0
