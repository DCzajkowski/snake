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
        if self.cmdPressed(modifier) and key == K_w:
                self.game.quit()

        if scene in [GAME_SCENE, MULTIPLAYER_GAME_SCENE]:
            self.handleGameScene(key, modifier)
        elif scene == PAUSE_SCENE:
            self.handlePauseScene(key, modifier)
        elif scene == MENU_SCENE:
            self.handleMenuScene(key, modifier)
        elif scene == SETTINGS_SCENE:
            self.handleSettingsScene(key, modifier)
        elif scene == GAME_OVER_SCENE:
            self.handleGameOverScene(key, modifier)

    # ---
    # Scenes
    # ---

    def handleGameScene(self, key, modifier):
        if key in [K_LEFT, K_RIGHT, K_UP, K_DOWN, K_w, K_s, K_a, K_d]:
            self.moveSnake(key)
        if key == K_ESCAPE:
            self.game.pause()
        if self.cmdPressed(modifier) and key == K_d:
            self.game.toggleDebug()
        if self.game.inDebugMode():
            if key == K_e:
                self.game.end()
            if key == K_i:
                for snake in self.game.snakes:
                    snake.incrementLength()
            if key == K_g:
                self.game.toggleGrid()
            if key == K_t:
                self.game.toggleStyle()

    def handlePauseScene(self, key, modifier):
        if key == K_ESCAPE:
            self.game.unpause()
        if key in [K_SPACE, K_RETURN]:
            self.game.unpause()
        if key == K_q:
            self.game.quit()
        if key == K_m:
            self.game.scene = MENU_SCENE

    def handleMenuScene(self, key, modifier):
        if key == K_DOWN:
            self.game.menu.down()
        if key == K_UP:
            self.game.menu.up()
        if key in [K_RETURN, K_SPACE]:
            self.game.menu.enter()

    def handleSettingsScene(self, key, modifier):
        if key == K_DOWN:
            self.game.settings.down()
        if key == K_UP:
            self.game.settings.up()
        if key in [K_RETURN, K_SPACE]:
            self.game.settings.enter()
        if key in [K_RIGHT, K_LEFT]:
            self.game.settings.change(1 if key == K_RIGHT else -1)

    def handleGameOverScene(self, key, modifier):
        if key == K_ESCAPE:
            self.game.quit()
        if key in [K_SPACE, K_RETURN]:
            self.game.scene = MENU_SCENE

    # ---
    # Snake movement
    # ---

    def moveSnake(self, key):
        if self.game.scene == GAME_SCENE:
            self.moveSnakeInSingleplayerMode(key)
        elif self.game.scene == MULTIPLAYER_GAME_SCENE:
            self.moveSnakeInMultiplayerMode(key)

    def moveSnakeInSingleplayerMode(self, key):
        if key in [K_LEFT, K_a]:
            self.game.snakes[0].turnLeft()
        if key in [K_RIGHT, K_d]:
            self.game.snakes[0].turnRight()
        if key in [K_UP, K_w]:
            self.game.snakes[0].turnUp()
        if key in [K_DOWN, K_s]:
            self.game.snakes[0].turnDown()

    def moveSnakeInMultiplayerMode(self, key):
        if key == K_LEFT:
            self.game.snakes[1].turnLeft()
        if key == K_a:
            self.game.snakes[0].turnLeft()
        if key == K_RIGHT:
            self.game.snakes[1].turnRight()
        if key == K_d:
            self.game.snakes[0].turnRight()
        if key == K_UP:
            self.game.snakes[1].turnUp()
        if key == K_w:
            self.game.snakes[0].turnUp()
        if key == K_DOWN:
            self.game.snakes[1].turnDown()
        if key == K_s:
            self.game.snakes[0].turnDown()

    # ---
    # Modifiers
    # ---

    def cmdPressed(self, modifier):
        return modifier in [KMOD_LMETA, KMOD_RMETA, KMOD_META]

    def altPressed(self, modifier):
        return modifier in [KMOD_LALT, KMOD_RALT, KMOD_ALT]

    def ctrlPressed(self, modifier):
        return modifier in [KMOD_LCTRL, KMOD_RCTRL, KMOD_CTRL]
