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

    def __init__(self, game = None, width = None, x = None, y = None, name = None, identifier = None):
        self.game = game
        self.width = self.game.config['grid-size']
        self.initX = x if x is not None else (round(self.game.config['tile-count-x'] / 2) - 1)
        self.initY = y if y is not None else (round(self.game.config['tile-count-y'] / 2) - 1)
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
        if self.x > self.game.config['tile-count-x'] - 1:
            self.x = 0
        elif self.x < 0:
            self.x = self.game.config['tile-count-x'] - 1
        elif self.y > self.game.config['tile-count-y'] - 1:
            self.y = 0
        elif self.y < 0:
            self.y = self.game.config['tile-count-y'] - 1

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
