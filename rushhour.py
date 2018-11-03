from block import Block
from car import Car
from bord import Bord

class Rushhour(object):
    """docstring for Rushhour."""
    def __init__(self, game):
        self.game = self.load_board(f"data/{game}.txt")

    def load_board(self, filename):
        """Function for loading the board"""
        self.bord = Bord(("2","6"))
        self.car_list = []
        coordinate_list = []
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
                            # use bord.load function to append coordinates to the board
                                self.bord.load(Coordinate(x,y))
                # the order of cars: id, length, colour, location
                if text_line.isdigit():
                    id = text_line
                if text_line.startswith("length"):
                    text_line = text_line.rsplit()
                    length = text_line[1]
                if text_line.startswith("color"):
                    text_line = text_line.rsplit()
                    color = text_line[1]
                    if color == "red":
                        car = True
                    else:
                        car = False
                if text_line.startswith("location"):
                    while file.readline() is not "":
                        coordinate = file.readline().split(",")
                        x = coordinate[0]
                        y = coordinate[1]
                        # appending coordinates in a list (temporay solution?)
                        coordinate_list.append(x, y)
                    # make car objects
                    car = Car(id, length, colour, location, car)
                    # make list of cars
                    self.car_list.append(car)

    def move():
        """Function for moving the cars on the board"""
        pass

    def won():
        """Win condition for the game"""
        False
        pass


    def play():
        """Lets play a game"""

        print("This is russhour!!")

        while not self.won:
            command = input("> ").upper()
            print(command)
            print(self.board)
            print(self.car_list)


        pass

if __name__ == "__main__":
    rushhour = Rushhour("boards1")
    russhour.play()
