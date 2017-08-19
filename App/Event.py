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
        if scene == GAME_SCENE:
            if self.event.type == QUIT:
                self.handler.quit()
            if self.event.type == KEYDOWN:
                self.keyPressed(self.event.key, self.event.mod)
        elif scene == GAME_OVER_SCENE:
            if self.event.type == KEYDOWN:
                if self.event.key == K_ESCAPE:
                    self.handler.quit()
                else:
                    self.game.reset()
                    self.game.run()

    def keyPressed(self, key, modifier):
        if self.cmdPressed(modifier):
            if key == K_w:
                self.handler.quit()
        if key in [K_LEFT, K_RIGHT, K_UP, K_DOWN]:
            self.handler.moveSnake(key)
        if key == K_g:
            self.game.end()

    def cmdPressed(self, modifier):
        return modifier in [KMOD_LMETA, KMOD_RMETA, KMOD_META]

    def altPressed(self, modifier):
        return modifier in [KMOD_LALT, KMOD_RALT, KMOD_ALT]

    def ctrlPressed(self, modifier):
        return modifier in [KMOD_LCTRL, KMOD_RCTRL, KMOD_CTRL]
