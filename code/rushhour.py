import os
import sys

directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "code", "classes"))
sys.path.append(os.path.join(directory, "data"))

from car import Car
from board import Board
from archive import Archive
from random import randint
from visualize_board import BoardVisualization


class Rushhour(object):
    """docstring for Rushhour."""
    def __init__(self, game):
        self.load_cars(f"../data/cars{game}.txt")
        self.load_board(f"../data/board{game}.txt")
        self.archive_list = []
        self.counter = 0

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
                    coordinate_list = self.make_car_coordinate_list(file)
                    car = Car(id, length, color, coordinate_list, False)
                    self.car_list.append(car)

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

    def won(self):
        """Win condition for the game"""
        # if car 1 (red car) is on exit coordinate game is won
        command = [4, 5]
        self.move(command, 1)
        car = self.car_list[0].coordinate
        for coordinate in car:
            if coordinate == self.board.entrance:
                print("Congratulations, you won the game!")
                return True
        else:
            return False

    def make_possible_move(self):
        """Creates a list with possible moves"""
        move_list = []
        cars = []
        for command in [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]]:
            for car in self.car_list:
                option = self.check_move(car, command)
                if option:
                    if len(move_list) > 0:
                        # for indices in list that start with car.id
                        # if option in that list, do not add

                        for i in move_list:
                            if i[0] == car.id:
                                if option[0] not in i[1]:
                                    move_list.append([car.id, option])
                                    break
                            elif car.id not in cars:
                                cars.append(car.id)
                                move_list.append([car.id, option])

                    else:
                        move_list.append([car.id, option])
                        cars.append(car.id)

        return move_list

    def make_possible_commands(self):
        move_list = self.make_possible_move()
        possible_commands_list = []
        for i in range(len(move_list)):
            id = move_list[i][0]
            for j in range(len(move_list[i][1])):
                thing = id, tuple(move_list[i][1][j])
                possible_commands_list.append(thing)
        print(possible_commands_list)

    def move(self, command, id):
        """Function for moving the cars on the board"""
        # selecting the right car
        car = self.car_list[int(id) - 1]
        self.make_possible_commands()
        # check if coordinates are allowed
        if self.check_move(car, command) and self.inside_boundries(car, command):
            # do the move
            car.update_coordinates(command)
            self.counter += 1
            print(self.counter)
            old_board_hashed = hash(self.board)
            self.update_board()

            # put all information regarding move in archive
            step = [command, id]
            board_hashed = hash(self.board)
            archive = Archive(step, board_hashed, old_board_hashed)
            self.archive_list.append(archive)

    def check_move(self, car, command):
        """Checks if no other cars are in the way"""
        for car_rest in self.car_list:
            # the car is allowed to move on its own coordinates
            if car_rest is not car:
                # check all the coordinates in between the original coordinates
                # and the inputted coordinates
                # print(car.id, car_rest.id)
                if not self.try_temporary_command(command, car, car_rest):
                    return False
        # print(self.try_temporary_command(command, car, car_rest))
        return self.try_temporary_command(command, car, car_rest)

    def try_temporary_command(self, command, car, car_rest):
        """Perform control on temporary moves"""
        if car_rest is not car:
            # check every coordinate in between begin and end using steps of 1
            temp_command = self.make_temporary_command(command, car)
            # check temp_coordinates
            for command in temp_command:
                for coordinate in car.temp_coordinates(command):
                    if coordinate in car_rest.coordinate:
                        return False
        return self.make_temporary_command(command, car)

    def indexing_constant(self, car):
        """Returns a integer for the indexation of the coordinate system"""
        if car.direction == "x":
            i = 0
        else:
            i = 1
        return i

    def make_temporary_command(self, command, car):
        """Function for the creation of a temporary coordinate"""
        i = self.indexing_constant(car)
        # determine the direction of the move and change the steps accordingly
        temp_command_list = []
        for step in range(abs(car.coordinate[0][i] - command[0])):
            step += 1
            if range((car.coordinate[0][i] - command[0]) < 0):
                step = -step
            temp_command = []
            for j in range(len(car.coordinate)):
                temp_command.append(car.coordinate[j][i] - step)
            if (car.coordinate[j][i] - step) is not 6:
                temp_command_list.append(temp_command)
        return temp_command_list

    def inside_boundries(self, car, command):
        """Checks if move is inside board"""
        for coordinate in car.temp_coordinates(command):
            if tuple(coordinate) not in self.board.grid:
                return False
        return True

    def print_board(self):
        """Prints the board in the terminal"""
        counter = 0
        for y in range(self.board.length):
            for x in range(self.board.length):
                print(self.board.grid[x, y], end="  ")
                counter += 1
                if counter % self.board.length == 0:
                    print("\n")

    def update_board(self):
        """Sets the value of the coordinates to the id of the car occupying
        the coordinate"""
        self.board.set_zero()
        for car in self.car_list:
            for coordinate in car.coordinate:
                x = coordinate[0]
                y = coordinate[1]
                self.board.grid[x, y] = int(car.id)

    def play(self):
        """Lets play a game"""
        # update board
        self.update_board()
        # print boards
        self.print_board()
        print("This is russhour!!")
        while not self.won():
            command = input("> ").upper()
            # call update board function
            if command:
                if command[0].isdigit():
                    command = command.split()
                    id = command[0]
                    command = self.clean_input(command[1])
                    if self.check_command(command):
                        self.move(command, id)
            # update board
            self.update_board()
            # print boards
            self.print_board()
            # visualize board
            visual = BoardVisualization(self.board, self.car_list, self.counter)
            visual.done()

    def clean_input(self, command):
        """Converts input to usable list of integers"""
        command = command.split(",")
        # convert command to integers
        command_clean = []
        for i in command:
            i = int(i)
            command_clean.append(i)
        return command_clean

    def check_command(self, command):
        """Checks if the command is valid"""
        if len(command) == 2:
            if abs(int(command[0]) - int(command[1])) == 1:
                return True
        elif len(command) == 3:
            if abs(int(command[0]) - int(command[2])) == 2:
                return True
        return False

    def willekeurig(self):
        """
        Genereert willekeurige commands voor de auto's in het spel
        """
        # while not self.won
        while not self.won():
            # pick a random car (in case of 3 cars)
            amount_cars = len(self.car_list)
            rand_id = randint(1, amount_cars)
            # find length of this car (2 or 3)
            for car in self.car_list:
                if rand_id == car.id:
                    length = car.length
            # pick a random coordinate this car should go to
            # inside the borders of the board: 6x6
            command = []
            # give three coordinates if car is length 3
            if length > 2:
                coordinate = randint(0, 3)
                command.append(coordinate)
                command.append(coordinate + 1)
                command.append(coordinate + 2)
            # give two coordinates if car is length 2
            else:
                coordinate = randint(0, 4)
                command.append(coordinate)
                command.append(coordinate + 1)
            self.move(command, rand_id)


if __name__ == "__main__":
    rushhour = Rushhour("3")
    rushhour.play()
    # rushhour.visualize_board()
