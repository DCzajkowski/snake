from App.constants import *
from App.Core.ConfigManager import ConfigManager
from App.Core.EventHandler import EventHandler
from App.Core.Screen import Screen
from App.Objects.Apple import Apple
from App.Objects.Snake import Snake
from App.Scenes.Menu import Menu
from App.Scenes.Settings import Settings
from pygame.locals import *
import random
import time

class Game:
    # Just for reference to know which properties are available
    apple = None
    clock = None
    config = None
    frame = 1
    db = None
    display = None
    images = None
    menu = None
    pygame = None
    scene = MENU_SCENE
    screen = None
    settings = None
    snakes = None
    whoWon = None

    def __init__(self, pygame, db, images, width = 800, height = 600):
        self.pygame = pygame
        self.display = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        self.db = db

        self.images = images
        self.config = ConfigManager(self)

        self.menu = Menu(self)
        self.settings = Settings(self)
        self.screen = Screen(self)

        self.pygame.display.set_caption('The Snake Game')
        self.pygame.display.set_icon(self.pygame.image.load(self.db.read('path') + 'assets/icon.png'))

    def run(self):
        while True:
            # Used to eliminate collision of keys in the multiplayer game. It annoys me
            # to have it here, but there is no place to put it elsewhere. It must be
            # set in the game loop, just before the event loop is initialized.
            if self.scene == MULTIPLAYER_GAME_SCENE:
                lastKeys = []

            for event in self.pygame.event.get():
                # Used to eliminate collision of keys. It is an annoying bug where if two keys
                # are pressed too fast, the event loop is running before the game loop does
                if self.scene == MULTIPLAYER_GAME_SCENE and ('lastKeys' in globals() or 'lastKeys' in vars()) and self.didCollisionOfKeysAppear(lastKeys, event):
                    continue

                EventHandler(self, event).handle(self.scene)

                # Used to eliminate collision of keys. It is an annoying bug where if two keys
                # are pressed too fast, the event loop is running before the game loop does
                if event.type == KEYDOWN:
                    if self.scene == MULTIPLAYER_GAME_SCENE and ('lastKeys' in globals() or 'lastKeys' in vars()):
                        lastKeys.append(event.key)
                    elif self.scene == GAME_SCENE:
                        break

            if self.scene == GAME_OVER_SCENE:
                self.showGameOverScene()
            elif self.scene == MENU_SCENE:
                self.showMainMenuScene()
            elif self.scene == PAUSE_SCENE:
                self.showPauseScene()
            elif self.scene == SETTINGS_SCENE:
                self.showSettingsScene()
            elif self.scene == GAME_SCENE or self.scene == MULTIPLAYER_GAME_SCENE:
                self.showGameScene()

    # ---
    # Scenes
    # ---

    def showMainMenuScene(self):
        self.display.fill(COLOR_EMERALD)
        self.display.blit(self.images['main-menu'], (0, 0))

        self.menu.display()
        self.showHighScore(self.db.read('highscore'))
        self.screen.update()

    def showSettingsScene(self):
        self.display.fill(COLOR_EMERALD)
        self.display.blit(self.images['settings'], (0, 0))

        self.settings.display()
        self.screen.update()

    def showPauseScene(self):
        self.display.fill(COLOR_ASBESTOS)
        self.message('Paused', 'Press ESC or space bar to continue... Q quits the game.', COLOR_CLOUDS, COLOR_CLOUDS)

    def showGameOverScene(self):
        self.display.fill(COLOR_EMERALD)
        if self.inSingleplayerMode():
            self.message('Game Over (Your Score: ' + str(self.snakes[0].length) + ')', 'Press ESC to quit or space bar to continue...', COLOR_CLOUDS, COLOR_CLOUDS)
        elif self.inMultiplayerMode():
            if self.whoWon is None:
                self.message('Game Over. Noone wins.', 'Press ESC to quit or space bar to continue...', COLOR_CLOUDS, COLOR_CLOUDS)
            else:
                self.message('Game Over. ' + self.whoWon + ' wins.', 'Press ESC to quit or space bar to continue...', COLOR_CLOUDS, COLOR_CLOUDS)

    def showGameScene(self):
        self.frame += 1

        for snake in self.snakes:
            if self.didSnakeGoOffScreen(snake):
                snake.loopBack()
            else:
                snake.moveHead(snake.xVelocity, snake.yVelocity)

            snake.createTail(self)

        self.screen.initBackground()
        self.screen.draw().apple(self.apple.x, self.apple.y)
        for snake in self.snakes:
            self.screen.draw().snake(snake)
        self.screen.update()

        for snake in self.snakes:
            if self.didSnakeCollideWithAnApple(snake, self.apple):
                self.removeApple()
                self.generateNewApple()
                snake.incrementLength()
                if self.scene == GAME_SCENE:
                    self.updateHighscore()

        if self.inDebugMode():
            if self.config['showGrid']:
                self.screen.draw().grid()
            self.showDebugMessage()

        if self.scene == GAME_SCENE:
            self.showScore(self.snakes[0].length)
            self.showHighScore(self.db.read('highscore'))

            if self.didSnakeCollideWithItself(self.snakes[0]):
                self.end()

        if self.scene == MULTIPLAYER_GAME_SCENE:
            if self.didSnakeCollideWithItself(self.snakes[0]) and self.didSnakeCollideWithItself(self.snakes[1]):
                self.whoWon = None
                self.end()
            elif self.didSnakeCollideWithItself(self.snakes[0]):
                self.whoWon = self.snakes[1].name
                self.end()
            elif self.didSnakeCollideWithItself(self.snakes[1]):
                self.whoWon = self.snakes[0].name
                self.end()

            if self.didSnakesCollideHeadOn(self.snakes):
                self.whoWon = None
                self.end()

            if (self.didSnakeCollideWithOtherSnakesTail(self.snakes[0], self.snakes[1])
                and self.didSnakeCollideWithOtherSnakesTail(self.snakes[1], self.snakes[0])):
                self.whoWon = None
                self.end()
            elif self.didSnakeCollideWithOtherSnakesTail(self.snakes[0], self.snakes[1]):
                self.whoWon = self.snakes[1].name
                self.end()
            elif self.didSnakeCollideWithOtherSnakesTail(self.snakes[1], self.snakes[0]):
                self.whoWon = self.snakes[0].name
                self.end()

        self.clock.tick(self.config['framerate'])

    # ---
    # Setters and getters
    # ---

    def pause(self):
        self.scene = PAUSE_SCENE

    def unpause(self):
        if self.inSingleplayerMode():
            self.scene = GAME_SCENE
        elif self.inMultiplayerMode():
            self.scene = MULTIPLAYER_GAME_SCENE

    def play(self, players):
        if players == 1:
            self.snakes = [Snake(game = self, x = (round(self.config['tile-count-x'] / 2) - 1), y = (round(self.config['tile-count-y'] / 2) - 1), identifier = 0)]
            self.reset()
            self.scene = GAME_SCENE
        elif players == 2:
            self.snakes = [Snake(game = self, x = 0, y = 0, name = 'Player 1', identifier = 1), Snake(game = self, x = self.config['tile-count-x'] - 1, y = self.config['tile-count-y'] - 1, name = 'Player 2', identifier = 2)]
            self.reset()
            self.scene = MULTIPLAYER_GAME_SCENE
        else:
            raise NotImplementedError('No handling for more than two players.')

    def reset(self):
        self.whoWon = None
        self.frame = 1
        self.setDebug(False)
        for snake in self.snakes:
            snake.reset()
        self.generateNewApple()

    def end(self):
        self.scene = GAME_OVER_SCENE

    def generateNewApple(self):
        x = random.randrange(0, self.config['tile-count-x'])
        y = random.randrange(0, self.config['tile-count-y'])
        apple = Apple(x, y, self.config['grid-size'])

        for snake in self.snakes:
            if self.doesAppleOverlapSnake(apple, snake):
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

    def toggleDebug(self):
        self.config['debug'] = not self.config['debug']

    def currentStyle(self, el):
        return self.config['styles'][self.config['style']][el]

    def font(self, size):
        return self.pygame.font.SysFont(None, size)

    def inSingleplayerMode(self):
        return len(self.snakes) == 1

    def inMultiplayerMode(self):
        return len(self.snakes) > 1

    # ---
    # Actions
    # ---

    def quit(self):
        self.pygame.quit()
        quit()

    def didSnakeGoOffScreen(self, snake):
        return (snake.x > self.config['tile-count-x'] - 1
            or snake.x < 0
            or snake.y > self.config['tile-count-y'] - 1
            or snake.y < 0)

    def didSnakeCollideWithAnApple(self, snake, apple):
        return snake.x == apple.x and snake.y == apple.y

    def didSnakeCollideWithItself(self, snake):
        for segment in snake.tail[:-1]:
            if segment[0] == snake.x and segment[1] == snake.y:
                return True
        return False

    def didSnakeCollideWithOtherSnakesTail(self, snake1, snake2):
        for segment in snake2.tail[:-1]:
            if segment[0] == snake1.x and segment[1] == snake1.y:
                return True
        return False

    def didSnakesCollideHeadOn(self, snakes):
        if len(snakes) == 2:
            if snakes[0].x == snakes[1].x and snakes[0].y == snakes[1].y:
                return True
            return False
        raise NotImplementedError('No handling for else than two snakes')

    def doesAppleOverlapSnake(self, apple, snake):
        for segment in snake.tail:
            if segment[0] == apple.x and segment[1] == apple.y:
                return True
        return False

    def didCollisionOfKeysAppear(self, lastKeys, event):
        return (
            lastKeys != []
            and event.type == KEYDOWN
            and (
                (
                    event.key in [K_UP, K_DOWN, K_LEFT, K_RIGHT]
                    and (
                        K_UP in lastKeys
                        or K_DOWN in lastKeys
                        or K_LEFT in lastKeys
                        or K_RIGHT in lastKeys
                    )
                ) or (
                    event.key in [K_w, K_a, K_s, K_d]
                    and (
                        K_w in lastKeys
                        or K_a in lastKeys
                        or K_s in lastKeys
                        or K_d in lastKeys
                    )
                )
            )
        )

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
        scoreMessage = self.font(20).render('Current length: ' + str(score), True, COLOR_CLOUDS)
        self.display.blit(scoreMessage, [10, 10])
        self.screen.update()

    def showHighScore(self, score):
        highscoreMessage = self.font(20).render('Highscore: ' + str(score), True, COLOR_CLOUDS)
        self.display.blit(highscoreMessage, [WINDOW_WIDTH - highscoreMessage.get_rect().width - 10, 10])
        self.screen.update()

    def updateHighscore(self):
        if self.snakes[0].length > self.db.read('highscore'):
            self.db.change('highscore', self.snakes[0].length)
