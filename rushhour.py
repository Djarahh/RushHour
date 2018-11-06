import os
import sys
directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "code", "classes"))
sys.path.append(os.path.join(directory, "data"))

from block import Block
from car import Car
from board import Board


class Rushhour(object):
    """docstring for Rushhour."""
    def __init__(self, game):
        self.game = self.load_board(f"data/{game}.txt")

    def load_board(self, filename):
        """Function for loading the board"""
        self.board = Board([2, 6])
        self.car_list = []

        # open file in read mode
        with open(filename, "r") as file:
            # itterate over text and strip line
            for text_line in file:
                text_line = text_line.strip()
                # check if line is information on board length
                if text_line.startswith("board"):
                    text_line = text_line.rsplit()
                    for x in range(int(text_line[1])):
                        for y in range(int(text_line[1])):
                            # use board.load function to append coordinates
                            # to the board
                                self.board.load(Block([x, y]))
                # the order of cars: id, length, colour, location
                elif text_line.isdigit():
                    id = text_line
                elif text_line.startswith("length"):
                    text_line = text_line.rsplit()
                    length = text_line[1]
                elif text_line.startswith("color"):
                    text_line = text_line.rsplit()
                    color = text_line[1]
                    if color == "red":
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

    def move(self, command, id):
        """Function for moving the cars on the board"""

        # selecting the right car
        car = self.car_list[int(id) - 1]
        # convert command to integers
        move = []
        for i in command:
            i = int(i)
            move.append(i)

        # check if coordinates are allowed
        if self.check_move(move, id):
            print("dont you fucking move")
            # do the move
            # car.update_coordinates(move)
        else:
            print("invalid move!!")


    def check_move(self, move, car_id):
        """checks if the move is legal"""
        self.print_board()
        print(1)
        counter = 0
        car = self.car_list[int(car_id) - 1]
        for coordinate in car.temp_coordinates(move):
            for block in self.board.coordinate:
                if coordinate == block.coordinate:
                    # if both blocks are occupied
                    counter += 1
        if counter < len(car.temp_coordinates(move)):
            return True
        else:
            return False

    def won():
        """Win condition for the game"""
        True
        pass

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
        counter = 0
        for block in self.board.coordinate:
            if block.occupied:
                # printing car id on spot in grid
                for car in self.car_list:
                    for coordinate in car.coordinate:
                        if block.coordinate == coordinate:
                            print(car.id, end="  ")
            else:
                print("0", end="  ")
            counter += 1
            # place enter at end of the row
            if counter % 6 == 0:
                print("\n")


    def play(self):
        """Lets play a game"""

        print("This is russhour!!")
        while self.won:
            command = input("> ").upper()
            # call update board function
            if command.startswith("MOVE"):
                command = command.split()
                id = command[2]
                command = command[1].split(",")

                self.move(command, id)
            self.update_board()
            # print boards
            self.print_board()
        pass


if __name__ == "__main__":
    rushhour = Rushhour("boards1")
    rushhour.play()
