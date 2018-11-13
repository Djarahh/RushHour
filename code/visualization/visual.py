import pygame as pg


class Visual(object):
    """Visualizes output data of algorithms"""
    def __init__(self):
        pg.init()

    def load_screen(self):
        """Loads the screen of the gameboard"""

        # moet nog ge-dehardcoded worden
        self.WINDOW_SIZE = (255, 255)
        self.WIDTH = 40
        self.HEIGHT = 40
        self.MARGIN = 2
        self.screen = pg.display.set_mode(self.WINDOW_SIZE)
        pg.display.set_caption("RushHour")

        self.clock = pg.time.Clock()
        self.carImg = pg.image.load('red_car.png')

    def car(self, x, y):
        """Loads cars to the board"""
        self.screen.blit(self.carImg, (x, y))

    def move(self, id, x, y):
        """Moves a car around"""

    def play(self):

        x = (255 * 0.50)
        y = (255 * 0.33)

        x_change = 0

        quit = False
        while not quit:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    quit = True
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_LEFT:
                        x_change = -5
                    elif event.key == pg.K_RIGHT:
                        x_change = 5
                if event.type == pg.KEYUP:
                    if event.key == pg.K_LEFT or event.key == pg.K_RIGHT:
                        x_change = 0

            self.screen.fill((0, 0, 0))
            for row in range(6):
                for column in range(6):
                    color = (255, 255, 255)
                    pg.draw.rect(self.screen, color,
                                 [(self.MARGIN + self.WIDTH) * column + self.MARGIN,
                                  (self.MARGIN + self.HEIGHT) * row + self.MARGIN, self.WIDTH,
                                  self.HEIGHT])
            x += x_change
            self.car(x, y)

            pg.display.update()
            self.clock.tick(60)
        pg.quit()
        quit()

if __name__ == '__main__':
    game = Visual()
    game.play()
