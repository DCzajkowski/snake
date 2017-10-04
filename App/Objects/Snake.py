from config import *

class Snake:
    width = 0
    x = 0
    y = 0
    initX = None
    initY = None
    xVelocity = 0
    yVelocity = 0
    tail = []
    length = 1
    direction = None
    name = None
    identifier = None

    def __init__(self, width = GRID_SIZE, x = None, y = None, name = None, identifier = None):
        self.width = width
        self.initX = x if x is not None else (round(TILE_COUNT_X / 2) - 1)
        self.initY = y if y is not None else (round(TILE_COUNT_Y / 2) - 1)
        self.name = name
        self.identifier = identifier

    def moveHead(self, x, y):
        self.x += x
        self.y += y

    def setHeadChange(self, x, y):
        if x is not None:
            self.xVelocity = x
        if y is not None:
            self.yVelocity = y

    def reset(self):
        self.x = self.initX
        self.y = self.initY
        self.xVelocity = 0
        self.yVelocity = 0
        self.tail = [[self.x, self.y]]
        self.length = 1
        self.direction = None

    def turnLeft(self):
        if self.direction != 1:
            self.setHeadChange(-1, 0)
            self.direction = 3

    def turnRight(self):
        if self.direction != 3:
            self.setHeadChange(1, 0)
            self.direction = 1

    def turnUp(self):
        if self.direction != 0:
            self.setHeadChange(0, -1)
            self.direction = 2

    def turnDown(self):
        if self.direction != 2:
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

    def createTail(self, game):
        if game.config['mode'] == 1 and game.scene == MULTIPLAYER_GAME_SCENE:
            if self.xVelocity != 0 or self.yVelocity != 0:
                if (game.frame % 10) not in [5, 6, 7, 8, 9]:
                    self.tail.append([self.x, self.y])

        elif game.config['mode'] == 0 or game.scene == GAME_SCENE:
            self.tail.append([self.x, self.y])

            if len(self.tail) > self.length:
                del self.tail[0]
