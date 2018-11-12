import pygame as pg

pg.init()



# moet nog ge-dehardcoded worden
WINDOW_SIZE = (255, 255)
WIDTH = 40
HEIGHT = 40
MARGIN = 2
screen = pg.display.set_mode(WINDOW_SIZE)
pg.display.set_caption("RushHour")

clock = pg.time.Clock()
carImg = pg.image.load('red_car.png')

quit = False


def car(x, y):
    screen.blit(carImg, (x, y))


x = (255 * 0.50)
y = (255 * 0.33)

x_change = 0

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

    screen.fill((0, 0, 0))
    for row in range(6):
        for column in range(6):
            color = (255, 255, 255)
            pg.draw.rect(screen, color,
                         [(MARGIN + WIDTH) * column + MARGIN,
                          (MARGIN + HEIGHT) * row + MARGIN, WIDTH,
                          HEIGHT])
    x += x_change
    car(x, y)

    pg.display.update()
    clock.tick(60)
pg.quit()
quit()
