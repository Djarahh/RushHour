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
        self.game = self.load_board(f"data/{game}.txt")

    def load_board(self, filename):
        """Function for loading the board"""
        self.car_list = []
        self.grid = []

        # open file in read mode
        with open(filename, "r") as file:
            # itterate over text and strip line
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
                # the order of cars: id, length, colour, location
                elif text_line.isdigit():
                    id = text_line
                elif text_line.startswith("length"):
                    text_line = text_line.rsplit()
                    length = text_line[1]
                elif text_line.startswith("color"):
                    text_line = text_line.rsplit()
                    color = text_line[1]
                    if color == "(255, 0, 0)":
                        car = True
                    else:
                        car = False
                elif text_line.startswith("location"):
                    coordinate_list = []
                    while True:
                        coordinate = file.readline().strip().split(",")
                        if coordinate[0] is not "":
                            x = int(coordinate[0])
                            y = int(coordinate[1])
                            # appending coordinates in a list
                            # (temporay solution?)
                            coordinate_list.append([x, y])
                        else:
                            break
                    # make car objects
                    car = Car(id, length, color, coordinate_list, car)
                    # make list of cars
                    self.car_list.append(car)
                self.board = Board(entrance)

    def move(self, command, id):
        """Function for moving the cars on the board"""

        # selecting the right car
        car = self.car_list[int(id) - 1]
        # convert command to integers

        # check if coordinates are allowed
        if self.check_move(command, id) and self.inside_boundries(id, command):
            # do the move
            car.update_coordinates(command)
        else:
            print("invalid move!!")

    def check_move(self, move, car_id):
        """checks if the move is legal"""

        # counter = 0
        car = self.car_list[int(car_id) - 1]
        for car_not in self.car_list:
            if car_not == car:
                pass
            else:
                for coordinate in car_not.coordinate:
                    if coordinate in car.temp_coordinates(move):
                        return False
        return True

    def won(self):
        """Win condition for the game"""
        # if car 1 (red car) is on exit coordinate game is won
        car = self.car_list[0].coordinate
        for coordinate in car:
            if coordinate == self.board.entrance:
                print("Congratulations, you won the game!")
                return True
        else:
            return False

    def update_board(self):
        """Function for updating the current board"""
        # reset board to all False in case of move
        for block in self.board.coordinate:
            block.occupy(False)
        # set occupied blocks to True
        for car in self.car_list:
            for coordinate in car.return_coordinates():
                # for each block of the board
                # (blocks are stored in the coordinates)
                for block in self.board.coordinate:
                    if coordinate == block.coordinate:
                        block.occupy(True)
                        block.car_id = car.id

    def print_board(self):
        board = self.grid
        for row in range(6):
            for column in range(6):
                print(board[row][column], end='')
            print('\n')

    def inside_boundries(self, id, command):
        """checks if move is inside board"""
        block_list = []
        car = self.car_list[int(id) - 1]
        for coordinate in car.temp_coordinates(command):
            for block in self.board.coordinate:
                block_list.append(block.coordinate)
            if coordinate not in block_list:
                return False
        return True

    def play(self):
        """Lets play a game"""

        print("This is russhour!!")
        self.show_board()
        while not self.won():
            command = input("> ").upper()
            # call update board function
            if command:
                if command[0].isdigit():
                    command = command.split()
                    id = command[0]
                    command = command[1]
                    if self.check_command(command):
                        self.move(command, id)
            self.update_board()
            # print boards
            self.print_board()
            self.show_board()

    def show_board(self):
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

        # fill the screen with black
        screen.fill((0, 0, 0))

        for row in range(6):
            for column in range(6):
                if self.grid[row][column] == 0:
                    color = (255, 255, 255)
                pg.draw.rect(screen,
                                 color,
                                 [(MARGIN + WIDTH) * column + MARGIN,
                                  (MARGIN + HEIGHT) * row + MARGIN,
                                  WIDTH,
                                  HEIGHT])

        pg.display.flip()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()

if __name__ == "__main__":
    rushhour = Rushhour("board_game1")
    rushhour.play()
