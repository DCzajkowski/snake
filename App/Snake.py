from config import *

class Snake:
    width = 0
    headX = 0
    headY = 0
    headXChange = 0
    headYChange = 0
    speed = 0
    tail = []
    length = 1

    def __init__(self, width = SNAKE_WIDTH, headX = None, headY = None):
        self.width = width
        self.headX = headX if headX is not None else (WINDOW_WIDTH / 2 - width) - ((WINDOW_WIDTH / 2) % GRID_SIZE)
        self.headY = headY if headY is not None else (WINDOW_HEIGHT / 2 - width) - ((WINDOW_HEIGHT / 2) % GRID_SIZE)
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
        self.headX = (WINDOW_WIDTH / 2) - ((WINDOW_WIDTH / 2) % GRID_SIZE)
        self.headY = (WINDOW_HEIGHT / 2) - ((WINDOW_HEIGHT / 2) % GRID_SIZE)
        self.headXChange = 0
        self.headYChange = 0
        self.tail = []
        self.length = 1
        self.speed = self.width

    def turnLeft(self):
        self.setHeadChange(-self.speed, 0)

    def turnRight(self):
        self.setHeadChange(self.speed, 0)

    def turnUp(self):
        self.setHeadChange(0, -self.speed)

    def turnDown(self):
        self.setHeadChange(0, self.speed)

    def loopBack(self):
        if self.headX >= WINDOW_WIDTH:
            self.headX = -self.width
        elif self.headX < 0:
            self.headX = WINDOW_WIDTH
        elif self.headY >= WINDOW_HEIGHT:
            self.headY = -self.width
        elif self.headY < 0:
            self.headY = WINDOW_HEIGHT

    def incrementLength(self):
        self.length += 1

    def createTail(self):
        self.tail.append([self.headX, self.headY])

        if len(self.tail) > self.length:
            del self.tail[0]
