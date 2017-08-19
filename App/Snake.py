from config import *

class Snake:
    width = 0
    headX = None
    headY = None
    headXChange = 0
    headYChange = 0
    speed = 0

    def __init__(self, width = SNAKE_WIDTH, headX = 0, headY = 0):
        self.width = width
        self.headX = headX
        self.headY = headY
        self.speed = width

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

    def turnLeft(self):
        self.setHeadChange(-self.speed, 0)

    def turnRight(self):
        self.setHeadChange(self.speed, 0)

    def turnUp(self):
        self.setHeadChange(0, -self.speed)

    def turnDown(self):
        self.setHeadChange(0, self.speed)

    def loopBackIfLeftTheScreen(self):
        if self.headX > WINDOW_WIDTH - self.width:
            self.headX = 0
        elif self.headX < 0:
            self.headX = WINDOW_WIDTH - self.width
        elif self.headY > WINDOW_HEIGHT - self.width:
            self.headY = 0
        elif self.headY < 0:
            self.headY = WINDOW_HEIGHT - self.width
