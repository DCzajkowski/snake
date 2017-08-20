from config import *

class Snake:
    width = 0
    x = 0
    y = 0
    xVelocity = 0
    yVelocity = 0
    tail = []
    length = 1
    direction = 0

    def __init__(self, width = GRID_SIZE, x = None, y = None):
        self.width = width
        self.x = x if x is not None else ((TILE_COUNT_X / 2) - 1)
        self.y = y if y is not None else ((TILE_COUNT_X / 2) - 1)

    def moveHead(self, x, y):
        self.x += x
        self.y += y

    def setHeadChange(self, x, y):
        if x is not None:
            self.xVelocity = x
        if y is not None:
            self.yVelocity = y

    def reset(self):
        self.x = ((TILE_COUNT_X / 2) - 1)
        self.y = ((TILE_COUNT_X / 2) - 1)
        self.xVelocity = 0
        self.yVelocity = 0
        self.tail = []
        self.length = 1
        self.direction = 0

    def turnLeft(self):
        self.setHeadChange(-1, 0)
        self.direction = 3

    def turnRight(self):
        self.setHeadChange(1, 0)
        self.direction = 1

    def turnUp(self):
        self.setHeadChange(0, -1)
        self.direction = 2

    def turnDown(self):
        self.setHeadChange(0, 1)
        self.direction = 0

    def loopBack(self):
        if self.x > TILE_COUNT_X - 1:
            self.x = 0
        elif self.x < 0:
            self.x = TILE_COUNT_X - 1
        elif self.y > TILE_COUNT_Y - 1:
            self.y = 0
        elif self.y < 0:
            self.y = TILE_COUNT_Y - 1

    def incrementLength(self):
        self.length += 1

    def createTail(self):
        self.tail.append([self.x, self.y])

        if len(self.tail) > self.length:
            del self.tail[0]
