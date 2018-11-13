import os
import sys
import pygame as pg
directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "code", "classes"))
sys.path.append(os.path.join(directory, "data"))

from block import Block
from car import Car
from board import Board
from random import randint


class Rushhour(object):
    """docstring for Rushhour."""
    def __init__(self, game):
        self.load_cars(f"data/cars{game}.txt")
        self.load_board(f"data/board{game}.txt")

    def load_cars(self, filename):
        """Loads the cars into rushhour"""
        self.car_list = []

        with open(filename, 'r') as file:
            for text_line in file:
                text_line = text_line.strip()
                if text_line.isdigit():
                    id = int(text_line)
                elif text_line.startswith("length"):
                    length = int(text_line.rsplit()[1])
                elif text_line.startswith("color"):
                    color = text_line.rsplit()[1]
                elif text_line.startswith("location"):
                    coordinate_list = []
                    while True:
                        coordinate = file.readline().strip().split(",")
                        if coordinate[0] is not "":
                            row = int(coordinate[0])
                            column = int(coordinate[1])
                            coordinate_list.append([row, column])
                        else:
                            break
                    # moet nog de car attribute uit car.py halen!!
                    car = Car(id, length, color, coordinate_list, False)
                    self.car_list.append(car)

    def load_board(self, filename):
        """Function for loading the board"""
        # grid moet toegevoegd aan board.py
        self.grid = []

        with open(filename, "r") as file:
            for text_line in file:
                text_line = text_line.strip()
                # check if line is information on board length
                if text_line.startswith("board"):
                    text_line = text_line.rsplit()
                    for row in range(int(text_line[1])):
                        self.grid.append([])
                        for column in range(int(text_line[1])):
                            self.grid[row].append(0)
                elif text_line.startswith("entrance"):
                    bla = text_line.rsplit()[1].rsplit(',')
                    entrance = []
                    entrance.append(int(bla[0]))
                    entrance.append(int(bla[1]))

        for car in self.car_list:
            for coordinate in car.coordinate:
                row = coordinate[0]
                column = coordinate[1]
                self.grid[row][column] = int(car.id)

    def visualize_board(self):
        """
        Shows a visual respresentation of the board
        """
        WIDTH = 40
        HEIGHT = 40
        MARGIN = 2

        pg.init()

        WINDOW_SIZE = [255, 255]
        screen = pg.display.set_mode(WINDOW_SIZE)

        pg.display.set_caption("RushHour")
        done = False
        clock = pg.time.Clock()

        # -------- Main Program Loop -----------
        while not done:
            for event in pg.event.get():  # User did something
                if event.type == pg.QUIT:  # If user clicked close
                    done = True  # Flag that we are done so we exit this loop

            # Set the screen background
            screen.fill((0, 0, 0))

            # Draw the grid
            for row in range(6):
                for column in range(6):
                    if not self.grid[row][column] == 0:
                        color = (255, 0, 0)
                        # car_id = self.grid[row][column]
                        # for car in self.car_list:
                        #     if car.id == car_id:
                        #         color = car.color
                    else:
                        color = (255, 255, 255)

                    pg.draw.rect(screen, color, [(MARGIN + WIDTH) * column + MARGIN,
                                (MARGIN + HEIGHT) * row + MARGIN, WIDTH, HEIGHT])

            # Limit to 60 frames per second
            clock.tick(60)

            # Go ahead and update the screen with what we've drawn.
            pg.display.flip()

        # Be IDLE friendly. If you forget this line, the program will 'hang'
        # on exit.
        pg.quit()


if __name__ == "__main__":
    rushhour = Rushhour("1")
    for row in rushhour.grid:
        print(row)
    rushhour.visualize_board()
