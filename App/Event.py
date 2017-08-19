from pygame.locals import *
from App.Handler import Handler

class Event:
    event = None
    handler = None

    def __init__(self, pygame, event):
        self.handler = Handler(pygame)
        self.event = event

    def handle(self, options = None):
        if self.event.type == QUIT:
            self.handler.quit()
        if self.event.type == KEYDOWN:
            self.keyPressed(self.event.key, self.event.mod)

    def keyPressed(self, key, modifier):
        if self.cmdPressed(modifier):
            if key == K_w:
                self.handler.quit()

    def cmdPressed(self, modifier):
        return modifier in [KMOD_LMETA, KMOD_RMETA, KMOD_META]

    def altPressed(self, modifier):
        return modifier in [KMOD_LALT, KMOD_RALT, KMOD_ALT]

    def ctrlPressed(self, modifier):
        return modifier in [KMOD_LCTRL, KMOD_RCTRL, KMOD_CTRL]
