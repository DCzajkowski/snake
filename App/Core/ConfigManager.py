from config import *

class ConfigManager:
    config = {}

    def __init__(self, game):
        self.config = {
            'style': game.db.read('style'),
            'debug': False,
            'showGrid': False,
            'mode': game.db.read('mode'), # 0 is one apple = one tile. 1 is one apple = 5 tiles
            'framerate': game.db.read('speed'),
            'grid-size': game.db.read('grid-size'),
            'styles': [
                {
                    'bg-color': COLOR_MIDNIGHT_BLUE,
                    'snake0-head': lambda snake, x, y: game.pygame.draw.rect(game.display, COLOR_CLOUDS, [x + 1, y + 1, snake.width - 2, snake.width - 2]),
                    'snake0-body': lambda snake, x, y: game.pygame.draw.rect(game.display, COLOR_CLOUDS, [x + 1, y + 1, snake.width - 2, snake.width - 2]),
                    'snake1-head': lambda snake, x, y: game.pygame.draw.rect(game.display, COLOR_CLOUDS, [x + 1, y + 1, snake.width - 2, snake.width - 2]),
                    'snake1-body': lambda snake, x, y: game.pygame.draw.rect(game.display, COLOR_CLOUDS, [x + 1, y + 1, snake.width - 2, snake.width - 2]),
                    'snake2-head': lambda snake, x, y: game.pygame.draw.rect(game.display, COLOR_CLOUDS, [x + 1, y + 1, snake.width - 2, snake.width - 2]),
                    'snake2-body': lambda snake, x, y: game.pygame.draw.rect(game.display, COLOR_CLOUDS, [x + 1, y + 1, snake.width - 2, snake.width - 2]),
                    'apple': lambda x, y: game.pygame.draw.rect(game.display, COLOR_POMEGRANATE, [x + 1, y + 1, self.config['grid-size'] - 2, self.config['grid-size'] - 2]),
                }, {
                    'bg-color': COLOR_MIDNIGHT_BLUE,
                    'snake0-head': lambda snake, x, y: game.pygame.draw.rect(game.display, COLOR_CLOUDS, [x + 1, y + 1, snake.width - 2, snake.width - 2]),
                    'snake0-body': lambda snake, x, y: game.pygame.draw.rect(game.display, COLOR_CLOUDS, [x + 1, y + 1, snake.width - 2, snake.width - 2]),
                    'snake1-head': lambda snake, x, y: game.pygame.draw.rect(game.display, COLOR_BELIZE_HOLE, [x + 1, y + 1, snake.width - 2, snake.width - 2]),
                    'snake1-body': lambda snake, x, y: game.pygame.draw.rect(game.display, COLOR_BELIZE_HOLE, [x + 1, y + 1, snake.width - 2, snake.width - 2]),
                    'snake2-head': lambda snake, x, y: game.pygame.draw.rect(game.display, COLOR_PUMPKIN, [x + 1, y + 1, snake.width - 2, snake.width - 2]),
                    'snake2-body': lambda snake, x, y: game.pygame.draw.rect(game.display, COLOR_PUMPKIN, [x + 1, y + 1, snake.width - 2, snake.width - 2]),
                    'apple': lambda x, y: game.pygame.draw.rect(game.display, COLOR_POMEGRANATE, [x + 1, y + 1, self.config['grid-size'] - 2, self.config['grid-size'] - 2]),
                }, {
                    'bg-color': COLOR_DARK_GREY,
                    'snake0-head': lambda snake, x, y: game.display.blit(game.pygame.transform.rotate(game.images['snake-head'], 90 * (snake.direction if snake.direction is not None else 0)), (x, y)),
                    'snake0-body': lambda snake, x, y: game.display.blit(game.images['snake-body'], (x, y)),
                    'snake1-head': lambda snake, x, y: game.display.blit(game.pygame.transform.rotate(game.images['snake-head'], 90 * (snake.direction if snake.direction is not None else 0)), (x, y)),
                    'snake1-body': lambda snake, x, y: game.display.blit(game.images['snake-body'], (x, y)),
                    'snake2-head': lambda snake, x, y: game.display.blit(game.pygame.transform.rotate(game.images['snake-head'], 90 * (snake.direction if snake.direction is not None else 0)), (x, y)),
                    'snake2-body': lambda snake, x, y: game.display.blit(game.images['snake-body'], (x, y)),
                    'apple': lambda x, y: game.display.blit(game.images['apple'], (x, y)),
                },
            ]
        }

        self.config['tile-count-x'] = round(WINDOW_WIDTH / self.config['grid-size'])
        self.config['tile-count-y'] = round(WINDOW_HEIGHT / self.config['grid-size'])

    def updateGridSize(self, size):
        self.config['grid-size'] = size
        self.config['tile-count-x'] = round(WINDOW_WIDTH / size)
        self.config['tile-count-y'] = round(WINDOW_HEIGHT / size)

    def __getitem__(self, name):
        return self.config[name]

    def __setitem__(self, name, value):
        self.config[name] = value
