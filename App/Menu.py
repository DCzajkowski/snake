from config import *

class Menu:
    game = None
    position = 0
    elements = ['Single Player', 'Two Players', 'Settings', 'Exit']

    def __init__(self, game):
        self.game = game

    def down(self):
        if self.position + 1 < len(self.elements):
            self.position += 1
        else:
            self.position = 0

    def up(self):
        if self.position - 1 >= 0:
            self.position -= 1
        else:
            self.position = len(self.elements) - 1

    def enter(self):
        if self.position == 0:
            self.game.play(1)
        if self.position == 1:
            self.game.play(2)
        elif self.position == 2:
            self.game.scene == SETTINGS_SCENE
        elif self.position == 3:
            self.game.quit()

    def display(self):
        i = 0
        for element in self.elements:
            self.game.display.blit(self.game.font(30).render(element, True, COLOR_CLOUDS), [WINDOW_WIDTH / 2 - 50, 200 + (40 * i)])
            i += 1

        self.game.display.blit(self.game.font(30).render('¬', True, COLOR_CLOUDS), [WINDOW_WIDTH / 2 - 70, 198 + (40 * self.position)])
