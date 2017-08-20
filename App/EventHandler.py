from config import *
from pygame.locals import *

class EventHandler:
    event = None
    game = None

    def __init__(self, game, event):
        self.event = event
        self.game = game

    def handle(self, scene):
        if self.event.type == QUIT:
            self.game.quit()
        if self.event.type == KEYDOWN:
            self.keyPressed(self.event.key, self.event.mod, scene)

    def keyPressed(self, key, modifier, scene):
        if self.cmdPressed(modifier):
            if key == K_w:
                self.game.quit()

        if scene == GAME_SCENE:
            if key in [K_LEFT, K_RIGHT, K_UP, K_DOWN]:
                self.moveSnake(key)
            if key == K_ESCAPE:
                self.game.pause()
            if self.game.inDebugMode():
                if key == K_e:
                    self.game.end()
                if key == K_i:
                    self.game.snake.incrementLength()
                if key == K_d:
                    self.game.setDebug(False)
                if key == K_g:
                    self.game.toggleGrid()
                if key == K_t:
                    self.game.toggleStyle()
            else:
                if key == K_d:
                    self.game.setDebug(True)
        elif scene == PAUSE_SCENE:
            if key == K_ESCAPE:
                self.game.unpause()
            if key == K_SPACE:
                self.game.unpause()
            if key == K_q:
                self.game.quit()
        elif scene == GAME_OVER_SCENE:
            if key == K_ESCAPE:
                self.game.quit()
            if key == K_SPACE:
                self.game.reset()
                self.game.run()

    def moveSnake(self, key):
        if self.snake.direction != 1:
            if key == K_LEFT:
                self.snake.turnLeft()
        if self.snake.direction != 3:
            if key == K_RIGHT:
                self.snake.turnRight()
        if self.snake.direction != 0:
            if key == K_UP:
                self.snake.turnUp()
        if self.snake.direction != 2:
            if key == K_DOWN:
                self.snake.turnDown()

    # ---
    # Modifiers
    # ---

    def cmdPressed(self, modifier):
        return modifier in [KMOD_LMETA, KMOD_RMETA, KMOD_META]

    def altPressed(self, modifier):
        return modifier in [KMOD_LALT, KMOD_RALT, KMOD_ALT]

    def ctrlPressed(self, modifier):
        return modifier in [KMOD_LCTRL, KMOD_RCTRL, KMOD_CTRL]
