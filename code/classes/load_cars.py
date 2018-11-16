from code.classes.car import Car
from code.classes.board import Board


class LoadCars(object):
    """Creates a string containing the cars for the initialization of the
    game. Requires a txt file of the cars"""
    def __init__(self, game):
        self.car_list = self.load_cars(f"data/cars{game}.txt")
        self.board = self.load_board(f"data/board{game}.txt")

    def load_cars(self, filename):
        """Loads the cars into rushhour"""
        car_list = []
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
                    coordinate_list = self.make_car_coordinate_list(file)
                    car = Car(id, length, color, coordinate_list, False)
                    car_list.append(car)
        return car_list

    def make_car_coordinate_list(self, file):
        """Makes list of coordinates of the car"""
        coordinate_list = []
        while True:
            coordinate = file.readline().strip().split(",")
            if coordinate[0] is not "":
                row = int(coordinate[0])
                column = int(coordinate[1])
                coordinate_list.append([row, column])
            else:
                break
        return coordinate_list

    def load_board(self, filename):
        """Function for loading the board"""
        self.board = Board()
        with open(filename, "r") as file:
            for text_line in file:
                text_line = text_line.strip()
                # check if line is information on board length or entrance
                if text_line.startswith("board"):
                    self.make_grid(text_line)
                elif text_line.startswith("entrance"):
                    self.make_entrance(text_line)
        return self.board

    def make_grid(self, text_line):
        """Make the grid of the board, consisting of a dictionary"""
        coordinate = {}
        text_line = text_line.rsplit()
        self.board.length = int(text_line[1])
        # create a coordinate system of (x, y), coupled to a dictionary
        for y in range(self.board.length):
            for x in range(self.board.length):
                # set dictionary value to zero(unoccupied )
                coordinate[x, y] = 0
        self.board.grid = coordinate

    def make_entrance(self, text_line):
        """Add entrance of board to self.board"""
        entrance_x_y = text_line.rsplit()[1].rsplit(',')
        self.board.entrance.append(int(entrance_x_y[0]))
        self.board.entrance.append(int(entrance_x_y[1]))
