from config import *
from App.Handler import Handler
from App.Event import Event
from App.Screen import Screen
from App.Apple import Apple
import time
from pygame.locals import *
import random

class Game:
    pygame = None
    handler = None
    display = None
    snake = None
    clock = None
    gameOver = False
    apple = None
    images = None
    config = None
    highscore = None
    paused = False

    def __init__(self, pygame, snake, highscore = None, display = None, clock = None, handler = None, width = 800, height = 600):
        self.pygame = pygame
        self.snake = snake
        self.display = display if display is not None else pygame.display.set_mode((width, height))
        self.clock = clock if clock is not None else pygame.time.Clock()
        self.handler = handler if handler is not None else Handler(self)
        self.highscore = highscore if highscore is not None else 0

        self.pygame.display.set_caption('The Snake Game')
        self.pygame.display.set_icon(self.pygame.image.load('/Users/Darek/Documents/Development/Python/dc-snake/assets/icon.png'))

        self.images = {
            'snake-head': self.pygame.image.load('/Users/Darek/Documents/Development/Python/dc-snake/assets/snake_head.png'),
            'snake-body': self.pygame.image.load('/Users/Darek/Documents/Development/Python/dc-snake/assets/snake_body.png'),
            'apple': self.pygame.image.load('/Users/Darek/Documents/Development/Python/dc-snake/assets/apple.png')
        }
        self.config = {
            'style': 0,
            'debug': False,
            'showGrid': False,
            'styles': [
                {
                    'bg-color': COLOR_MIDNIGHT_BLUE,
                    'snake-head': lambda snake, x, y: self.pygame.draw.rect(self.display, SNAKE_HEAD_COLOR, [x + 1, y + 1, snake.width - 2, snake.width - 2]),
                    'snake-body': lambda snake, x, y: self.pygame.draw.rect(self.display, SNAKE_HEAD_COLOR, [x + 1, y + 1, snake.width - 2, snake.width - 2]),
                    'apple': lambda x, y: self.pygame.draw.rect(self.display, APPLE_COLOR, [x + 1, y + 1, GRID_SIZE - 2, GRID_SIZE - 2])
                }, {
                    'bg-color': COLOR_GREEN_SEA,
                    'snake-head': lambda snake, x, y: self.display.blit(self.pygame.transform.rotate(self.images['snake-head'], 90 * (snake.direction if snake.direction is not None else 0)), (x, y)),
                    'snake-body': lambda snake, x, y: self.display.blit(self.images['snake-body'], (x, y)),
                    'apple': lambda x, y: self.display.blit(self.pygame.transform.scale(self.images['apple'], (GRID_SIZE, GRID_SIZE)), (x, y))
                }
            ]
        }
        self.screen = Screen(self)

    def pause(self):
        self.paused = True

    def unpause(self):
        self.paused = False

    def showPauseScreen(self):
        self.display.fill(COLOR_ASBESTOS)
        self.message('Paused', 'Press ESC or space bar to continue... Q quits the game.', COLOR_CLOUDS, COLOR_CLOUDS)

    def currentStyle(self, el):
        return self.config['styles'][self.config['style']][el]

    def font(self, size):
        return self.pygame.font.SysFont(None, size)

    def message(self, header, span, headerColor, spanColor):
        header = self.font(40).render(header, True, headerColor)
        span = self.font(25).render(span, True, spanColor)
        self.display.blit(header, [WINDOW_WIDTH / 2 - header.get_rect().width / 2, WINDOW_HEIGHT / 2 - 15])
        self.display.blit(span, [WINDOW_WIDTH / 2 - span.get_rect().width / 2, WINDOW_HEIGHT / 2 + 15])
        self.pygame.display.update()

    def reset(self):
        self.gameOver = False
        self.setDebug(False)
        self.snake.reset()
        self.generateNewApple()

    def end(self):
        self.gameOver = True

    def updateHighscore(self):
        if self.snake.length > self.highscore:
            self.highscore = self.snake.length
        open('db.txt', 'w').write('highscore=' + str(self.highscore))

    def showGameOverScreen(self):
        self.display.fill(COLOR_EMERALD)
        self.message('Game Over (Your Score: ' + str(self.snake.length) + ')', 'Press ESC to quit or space bar to continue...', COLOR_CLOUDS, COLOR_CLOUDS)

    def showDebugMessage(self):
        debugMessage = self.font(15).render('In Debug Mode', True, COLOR_CLOUDS)
        self.display.blit(debugMessage, [WINDOW_WIDTH - debugMessage.get_rect().width, WINDOW_HEIGHT - debugMessage.get_rect().height])
        self.pygame.display.update()

    def showScore(self, score):
        debugMessage = self.font(20).render('Current length: ' + str(score), True, COLOR_CLOUDS)
        self.display.blit(debugMessage, [10, 10])
        self.pygame.display.update()

    def showHighScore(self, score):
        highscoreMessage = self.font(20).render('Highscore: ' + str(score), True, COLOR_CLOUDS)
        self.display.blit(highscoreMessage, [WINDOW_WIDTH - highscoreMessage.get_rect().width - 10, 10])
        self.pygame.display.update()

    def generateNewApple(self):
        x = random.randrange(0, TILE_COUNT_X)
        y = random.randrange(0, TILE_COUNT_Y)
        apple = Apple(x, y, GRID_SIZE)

        if self.handler.doesAppleOverlapSnake(apple, self.snake):
            self.generateNewApple()
        else:
            self.apple = apple

    def removeApple(self):
        self.apple = None

    def toggleGrid(self):
        self.config['showGrid'] = not self.config['showGrid']

    def toggleStyle(self):
        if self.config['style'] + 1 < len(self.config['styles']):
            self.config['style'] += 1
        else:
            self.config['style'] = 0

    def inDebugMode(self):
        return self.config['debug']

    def setDebug(self, value):
        self.config['debug'] = value

    def run(self):
        self.generateNewApple()

        while True:
            if self.gameOver:
                scene = GAME_OVER_SCENE
                self.showGameOverScreen()
            elif self.paused:
                scene = PAUSE_SCENE
                self.showPauseScreen()
            else:
                scene = GAME_SCENE

            for event in self.pygame.event.get():
                Event(self, event).handle(scene)

            if not self.gameOver and not self.paused:
                if self.handler.didSnakeGoOffScreen(self.snake):
                    self.snake.loopBack()
                else:
                    self.snake.moveHead(self.snake.xVelocity, self.snake.yVelocity)

                self.snake.createTail()

                self.screen.initBackground()
                self.screen.draw().apple(self.apple.x, self.apple.y)
                self.screen.draw().snake(self.snake)
                self.screen.update()

                if self.handler.didSnakeCollideWithAnApple(self.snake, self.apple):
                    self.removeApple()
                    self.generateNewApple()
                    self.snake.incrementLength()
                    self.updateHighscore()

                if self.inDebugMode():
                    if self.config['showGrid']:
                        self.screen.draw().grid()
                    self.showDebugMessage()

                self.showScore(self.snake.length)
                self.showHighScore(self.highscore)

                if self.handler.didSnakeCollideWithItself(self.snake):
                    self.end()

                self.clock.tick(FRAMERATE)
