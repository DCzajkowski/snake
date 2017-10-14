from config import *

class Settings:
    game = None
    position = 0
    elementsCount = 5

    def __init__(self, game):
        self.game = game

    def down(self):
        if self.position + 1 < self.elementsCount:
            self.position += 1
        else:
            self.position = 0

    def up(self):
        if self.position - 1 >= 0:
            self.position -= 1
        else:
            self.position = self.elementsCount - 1

    def enter(self):
        if self.position == self.elementsCount - 1:
            self.game.scene = MENU_SCENE

    def change(self, direction):
        if self.position == 0:
            self.toggleSpeed(direction)
        if self.position == 1:
            self.toggleStyle(direction)
        if self.position == 2:
            self.toggleMode(direction)
        if self.position == 3:
            self.toggleSize(direction)

    def toggleSpeed(self, direction):
        value = AVAILABLE_SPEEDS[self.calculatePosition(direction, (AVAILABLE_SPEEDS).index(self.game.config['framerate']), len(AVAILABLE_SPEEDS))]
        self.game.config['framerate'] = value
        self.game.db.change('speed', value)

    def toggleStyle(self, direction):
        value = AVAILABLE_STYLES[self.calculatePosition(direction, (AVAILABLE_STYLES).index(self.game.config['style']), len(AVAILABLE_STYLES))]
        self.game.config['style'] = value
        self.game.db.change('style', value)

    def toggleMode(self, direction):
        value = AVAILABLE_MODES[self.calculatePosition(direction, (AVAILABLE_MODES).index(self.game.config['mode']), len(AVAILABLE_MODES))]
        self.game.config['mode'] = value
        self.game.db.change('mode', value)

    def toggleSize(self, direction):
        value = AVAILABLE_SIZES[self.calculatePosition(direction, (AVAILABLE_SIZES).index(self.game.config['grid-size']), len(AVAILABLE_SIZES))]

        self.game.config.updateGridSize(value)
        self.game.db.change('grid-size', value)

    def calculatePosition(self, direction, position, length):
        if direction == 1:
            return position + direction if position + direction < length else 0
        if direction == -1:
            return position + direction if position + direction >= 0 else -1

    def display(self):
        text = self.game.font(30).render('Speed: ' + str(self.game.config['framerate']), True, COLOR_CLOUDS)
        self.game.display.blit(text, [WINDOW_WIDTH / 2 - text.get_rect().width / 2, 200])

        if self.game.config['style'] == 0:
            style = 'Simple'
        elif self.game.config['style'] == 1:
            style = 'Colourful'
        elif self.game.config['style'] == 2:
            style = 'Realistic'
        text = self.game.font(30).render('Theme: ' + style, True, COLOR_CLOUDS)
        self.game.display.blit(text, [WINDOW_WIDTH / 2 - text.get_rect().width / 2, 200 + 40])

        if self.game.config['mode'] == 0:
            mode = 'Classic Snake'
        elif self.game.config['mode'] == 1:
            mode = 'Curve Fever'
        text = self.game.font(30).render('Mode: ' + mode, True, COLOR_CLOUDS)
        self.game.display.blit(text, [WINDOW_WIDTH / 2 - text.get_rect().width / 2, 200 + 80])

        text = self.game.font(30).render('Grid size: ' + str(self.game.config['grid-size']), True, COLOR_CLOUDS)
        self.game.display.blit(text, [WINDOW_WIDTH / 2 - text.get_rect().width / 2, 200 + 120])

        text = self.game.font(30).render('Back to Menu', True, COLOR_CLOUDS)
        self.game.display.blit(text, [WINDOW_WIDTH / 2 - text.get_rect().width / 2, 200 + 160])

        self.game.display.blit(self.game.images['menu-selection'], [WINDOW_WIDTH / 2 - self.game.images['menu-selection'].get_rect().width / 2 - 150, 198 + (40 * self.position)])
