from config import *

class Snake:
    width = 0
    x = 0
    y = 0
    xVelocity = 0
    yVelocity = 0
    speed = 0
    tail = []
    length = 1
    direction = 0

    def __init__(self, width = SNAKE_WIDTH, x = None, y = None):
        self.width = width
        self.x = x if x is not None else (WINDOW_WIDTH / 2 - width) - ((WINDOW_WIDTH / 2) % GRID_SIZE)
        self.y = y if y is not None else (WINDOW_HEIGHT / 2 - width) - ((WINDOW_HEIGHT / 2) % GRID_SIZE)
        self.speed = width

    def moveHead(self, x, y):
        self.x += x
        self.y += y

    def setHeadChange(self, x, y):
        if x is not None:
            self.xVelocity = x
        if y is not None:
            self.yVelocity = y

    def reset(self):
        self.x = (WINDOW_WIDTH / 2) - ((WINDOW_WIDTH / 2) % GRID_SIZE)
        self.y = (WINDOW_HEIGHT / 2) - ((WINDOW_HEIGHT / 2) % GRID_SIZE)
        self.xVelocity = 0
        self.yVelocity = 0
        self.tail = []
        self.length = 1
        self.speed = self.width
        self.direction = 0

    def turnLeft(self):
        self.setHeadChange(-self.speed, 0)
        self.direction = 3

    def turnRight(self):
        self.setHeadChange(self.speed, 0)
        self.direction = 1

    def turnUp(self):
        self.setHeadChange(0, -self.speed)
        self.direction = 2

    def turnDown(self):
        self.setHeadChange(0, self.speed)
        self.direction = 0

    def loopBack(self):
        print(self.x, WINDOW_WIDTH, self.width, WINDOW_WIDTH - self.width)
        if self.x >= WINDOW_WIDTH:
            self.x = -self.width
        elif self.x < 0:
            self.x = WINDOW_WIDTH
        elif self.y >= WINDOW_HEIGHT:
            self.y = -self.width
        elif self.y < 0:
            self.y = WINDOW_HEIGHT

    def incrementLength(self):
        self.length += 1

    def createTail(self):
        self.tail.append([self.x, self.y])

        if len(self.tail) > self.length:
            del self.tail[0]
