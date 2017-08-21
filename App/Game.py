from config import *
from App.EventHandler import EventHandler
from App.Screen import Screen
from App.Apple import Apple
import time
from pygame.locals import *
import random
from App.Menu import Menu

class Game:
    pygame = None
    display = None
    snake = None
    clock = None
    apple = None
    images = None
    config = None
    highscore = None
    scene = MENU_SCENE
    screen = None
    menu = None

    def __init__(self, pygame, snake, highscore = None, width = 800, height = 600):
        self.pygame = pygame
        self.snake = snake
        self.display = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        self.highscore = highscore if highscore is not None else 0
        self.menu = Menu(self)

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

    def run(self):
        self.generateNewApple()

        while True:
            for event in self.pygame.event.get():
                EventHandler(self, event).handle(self.scene)

                if event.type == KEYDOWN:
                    break

            if self.scene == GAME_OVER_SCENE:
                self.showGameOverScene()
            elif self.scene == MENU_SCENE:
                self.showMainMenuScene()
            elif self.scene == PAUSE_SCENE:
                self.showPauseScene()
            elif self.scene == SETTINGS_SCENE:
                self.showSettingsScene()
            elif self.scene == GAME_SCENE:
                self.showGameScene()

    # ---
    # Scenes
    # ---

    def showMainMenuScene(self):
        self.display.fill(COLOR_ASBESTOS)
        header = self.font(40).render('The Snake Game', True, COLOR_CLOUDS)

        self.display.blit(header, [WINDOW_WIDTH / 2 - header.get_rect().width / 2, 50])
        self.menu.display()
        self.showHighScore(self.highscore)
        self.screen.update()

    def showSettingsScene(self):
        pass

    def showPauseScene(self):
        self.display.fill(COLOR_ASBESTOS)
        self.message('Paused', 'Press ESC or space bar to continue... Q quits the game.', COLOR_CLOUDS, COLOR_CLOUDS)

    def showGameOverScene(self):
        self.display.fill(COLOR_EMERALD)
        self.message('Game Over (Your Score: ' + str(self.snake.length) + ')', 'Press ESC to quit or space bar to continue...', COLOR_CLOUDS, COLOR_CLOUDS)

    def showGameScene(self):
        if self.didSnakeGoOffScreen(self.snake):
            self.snake.loopBack()
        else:
            self.snake.moveHead(self.snake.xVelocity, self.snake.yVelocity)

        self.snake.createTail()

        self.screen.initBackground()
        self.screen.draw().apple(self.apple.x, self.apple.y)
        self.screen.draw().snake(self.snake)
        self.screen.update()

        if self.didSnakeCollideWithAnApple(self.snake, self.apple):
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

        if self.didSnakeCollideWithItself(self.snake):
            self.end()

        self.clock.tick(FRAMERATE)

    # ---
    # Setters and getters
    # ---

    def pause(self):
        self.scene = PAUSE_SCENE

    def unpause(self):
        self.scene = GAME_SCENE

    def play(self):
        self.scene = GAME_SCENE

    def reset(self):
        self.scene = GAME_SCENE
        self.setDebug(False)
        self.snake.reset()
        self.generateNewApple()

    def end(self):
        self.scene = GAME_OVER_SCENE

    def generateNewApple(self):
        x = random.randrange(0, TILE_COUNT_X)
        y = random.randrange(0, TILE_COUNT_Y)
        apple = Apple(x, y, GRID_SIZE)

        if self.doesAppleOverlapSnake(apple, self.snake):
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

    def currentStyle(self, el):
        return self.config['styles'][self.config['style']][el]

    def font(self, size):
        return self.pygame.font.SysFont(None, size)

    # ---
    # Actions
    # ---

    def quit(self):
        self.pygame.quit()
        quit()

    def didSnakeGoOffScreen(self, snake):
        return (snake.x > TILE_COUNT_X - 1
            or snake.x < 0
            or snake.y > TILE_COUNT_Y - 1
            or snake.y < 0)

    def didSnakeCollideWithAnApple(self, snake, apple):
        return snake.x == apple.x and snake.y == apple.y

    def didSnakeCollideWithItself(self, snake):
        for segment in snake.tail[:-1]:
            if segment[0] == snake.x and segment[1] == snake.y:
                return True
        return False

    def doesAppleOverlapSnake(self, apple, snake):
        for segment in snake.tail[:-1]:
            if segment[0] == apple.x and segment[1] == apple.y:
                return True
        return False

    # ---
    # Messaging
    # ---

    def message(self, header, span, headerColor, spanColor):
        header = self.font(40).render(header, True, headerColor)
        span = self.font(25).render(span, True, spanColor)
        self.display.blit(header, [WINDOW_WIDTH / 2 - header.get_rect().width / 2, WINDOW_HEIGHT / 2 - 15])
        self.display.blit(span, [WINDOW_WIDTH / 2 - span.get_rect().width / 2, WINDOW_HEIGHT / 2 + 15])
        self.screen.update()

    def showDebugMessage(self):
        debugMessage = self.font(15).render('In Debug Mode', True, COLOR_CLOUDS)
        self.display.blit(debugMessage, [WINDOW_WIDTH - debugMessage.get_rect().width, WINDOW_HEIGHT - debugMessage.get_rect().height])
        self.screen.update()

    def showScore(self, score):
        debugMessage = self.font(20).render('Current length: ' + str(score), True, COLOR_CLOUDS)
        self.display.blit(debugMessage, [10, 10])
        self.screen.update()

    def showHighScore(self, score):
        highscoreMessage = self.font(20).render('Highscore: ' + str(score), True, COLOR_CLOUDS)
        self.display.blit(highscoreMessage, [WINDOW_WIDTH - highscoreMessage.get_rect().width - 10, 10])
        self.screen.update()

    def updateHighscore(self):
        if self.snake.length > self.highscore:
            self.highscore = self.snake.length
        open('db.txt', 'w').write('highscore=' + str(self.highscore))
