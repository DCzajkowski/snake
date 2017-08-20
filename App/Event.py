from config import *
from pygame.locals import *
from App.Handler import Handler

class Event:
    event = None
    handler = None
    game = None

    def __init__(self, game, event):
        self.handler = Handler(game)
        self.event = event
        self.game = game

    def handle(self, scene):
        if self.event.type == QUIT:
            self.handler.quit()
        if self.event.type == KEYDOWN:
            self.keyPressed(self.event.key, self.event.mod, scene)

    def keyPressed(self, key, modifier, scene):
        if self.cmdPressed(modifier):
            if key == K_w:
                self.handler.quit()

        if scene == GAME_SCENE:
            if key in [K_LEFT, K_RIGHT, K_UP, K_DOWN]:
                self.handler.moveSnake(key)
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
                self.handler.quit()
        elif scene == GAME_OVER_SCENE:
            if key == K_ESCAPE:
                self.handler.quit()
            if key == K_SPACE:
                self.game.reset()
                self.game.run()

    def cmdPressed(self, modifier):
        return modifier in [KMOD_LMETA, KMOD_RMETA, KMOD_META]

    def altPressed(self, modifier):
        return modifier in [KMOD_LALT, KMOD_RALT, KMOD_ALT]

    def ctrlPressed(self, modifier):
        return modifier in [KMOD_LCTRL, KMOD_RCTRL, KMOD_CTRL]
