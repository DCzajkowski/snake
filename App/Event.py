from pygame.locals import *
from App.Handler import Handler

class Event:
    event = None
    handler = None
    game = None

    def __init__(self, game, event):
        self.handler = Handler(game.pygame)
        self.event = event
        self.game = game

    def handle(self, options = None):
        if self.event.type == QUIT:
            self.handler.quit()
        if self.event.type == KEYDOWN:
            self.keyPressed(self.event.key, self.event.mod)

    def keyPressed(self, key, modifier):
        if self.cmdPressed(modifier):
            if key == K_w:
                self.handler.quit()
        if key == K_LEFT:
            self.game.snake.changeHeadX(-10)
        if key == K_RIGHT:
            self.game.snake.changeHeadX(10)

    def cmdPressed(self, modifier):
        return modifier in [KMOD_LMETA, KMOD_RMETA, KMOD_META]

    def altPressed(self, modifier):
        return modifier in [KMOD_LALT, KMOD_RALT, KMOD_ALT]

    def ctrlPressed(self, modifier):
        return modifier in [KMOD_LCTRL, KMOD_RCTRL, KMOD_CTRL]
