class Rushhour(object):
    """
    The game Rushhour
    """
    def __init__(self, car_list, board):
        """
        Initalization for Rushhour.

        car_list = list, contains car objects
        board = board object"""
        self.car_list = car_list
        self.board = board
        self.counter = 0

    def won(self):
        """
        Win condition for the game

        Returns boolean
        """
        # if car 1 (red car) is on exit coordinate game is won
        command = [(self.board.entrance[0] - 1),
                   self.board.entrance[0]]
        car = self.car_list[0]
        if self.check_move(car, command) and self.inside_boundries(
                                                  car, command):
            self.move(command, 1, self.car_list)

            for coordinate in car.coordinate:
                if coordinate == self.board.entrance:
                    return True
        return False

    def make_possible_move(self):
        """
        Creates a list with possible moves

        returns list with possible moves (moves = [car_id, command])
        """
        move_list = []
        for i in range(self.board.length):
            command = [i, (i + 1)]
            for car in self.car_list:
                option = self.check_move(car, command)
                if option:
                    for i in option:
                        if [car.id, i] not in move_list:
                            move_list.append([car.id, i])
        return move_list

    def make_possible_move_with_input(self, car_list):
        """
        Creates a list with possible moves, but does not actually
        move the car

        car_list = list of car objects
        Returns list of possible moves (moves = [car_id, command])
        """
        move_list = []
        for i in range(self.board.length):
            command = [i, (i + 1)]
            for car in car_list:
                option = self.check_move_with_input(car, command,
                                                    car_list)
                if option:
                    for i in option:
                        if [car.id, i] not in move_list:
                            move_list.append([car.id, i])
        return move_list

    def move(self, command, id, car_list):
        """
        Function for moving the cars on the board

        command = list, contains either x or y coordinates
        id = int, represents the car
        car_list = list of car objects
        """
        # selecting the right car
        self.car_list = car_list
        car = self.car_list[int(id) - 1]
        car.update_coordinates(command)

    def check_move(self, car, command):
        """
        Checks if no other cars are in the way

        command = list, contains either x or y coordinates
        car = car object
        Returns false or tries the command
        """
        for car_rest in self.car_list:
            # the car is allowed to move on its own coordinates
            if car_rest is not car:
                # check all the coordinates in between the original
                # coordinates and the input of coordinates
                if not self.try_temporary_command(command, car,
                                                  car_rest):
                    return False
        return self.try_temporary_command(command, car, car_rest)

    def check_move_with_input(self, car, command, car_list):
        """
        Checks if no other cars are in the way

        command = list, contains either x or y coordinates
        car = car object
        car_list = list of car objects
        Returns False or tries the command
        """
        for car_rest in car_list:
            # the car is allowed to move on its own coordinates
            if car_rest is not car:
                # check all the coordinates in between the original
                # coordinate and the input of coordinates
                if not self.try_temporary_command(command, car,
                                                  car_rest):
                    return False
        return self.try_temporary_command(command, car, car_rest)

    def try_temporary_command(self, command, car, car_rest):
        """
        Perform control on temporary moves

        command = list, contains either x or y coordinates
        car = car object
        car_rest = car object, from the car_list
        Returns false or makes command
        """
        if car_rest is not car:
            # check coordinates in between begin and end, steps of 1
            temp_command = self.make_temporary_command(command, car)
            # check temp_coordinates
            for command in temp_command:
                # combine this with grid idea
                if car.direction == "y":
                    # get x coordinate
                    x = car.coordinate[0][0]
                    # [x,y] and [x,y]...
                    coordinate_list = [[x, command[0]],
                                       [x, command[1]]]
                    if car.length == 3:
                        coordinate_list = [[x, command[0]],
                                           [x, command[1]],
                                           [x, command[1] + 1]]

                else:
                    y = car.coordinate[0][1]
                    coordinate_list = [[command[0], y],
                                       [command[1], y]]
                    if car.length == 3:
                        coordinate_list = [[command[0], y],
                                           [command[1], y],
                                           [command[1] + 1, y]]
                for coordinate in coordinate_list:
                    if coordinate in car_rest.coordinate:
                        return False
        return self.make_temporary_command(command, car)

    def indexing_constant(self, car):
        """
        Returns a integer for the indexation of the coordinate system

        car = car object
        Returns int
        """
        if car.direction == "x":
            i = 0
        else:
            i = 1
        return i

    def make_temporary_command(self, command, car):
        """
        Function for the creation of a temporary coordinate

        command = list, contains either x or y coordinates
        car = car object
        Returns list with possible commands
        """
        i = self.indexing_constant(car)
        # determine the direction of the move and change the steps
        # accordingly
        temp_command_list = []
        for step in range(abs(car.coordinate[0][i] - command[0])):
            step += 1
            if range((car.coordinate[0][i] - command[0]) < 0):
                step = -step
            temp_command = []
            for j in range(len(car.coordinate)):
                temp_command.append(car.coordinate[j][i] - step)
            if (car.coordinate[j][i] - step) < self.board.length:
                temp_command_list.append(temp_command)
        return temp_command_list

    def inside_boundries(self, car, command):
        """
        Checks if move is inside board

        command = list, contains either x or y coordinates
        car = car object
        Returns boolean
        """
        for coordinate in car.temp_coordinates(command):
            if tuple(coordinate) not in self.board.grid:
                return False
        return True

    def print_board(self):
        """
        Prints the board in the terminal
        """
        counter = 0
        for y in range(self.board.length):
            for x in range(self.board.length):
                print(self.board.grid[x, y], end="  ")
                counter += 1
                if counter % self.board.length == 0:
                    print("\n")

    def update_board(self):
        """
        Sets the value of the coordinates to the id of the car
        occupying the coordinate
        """
        self.board.set_zero()
        for car in self.car_list:
            for coordinate in car.coordinate:
                x = coordinate[0]
                y = coordinate[1]
                self.board.grid[x, y] = int(car.id)

    def return_car_list(self):
        """
        Returns the self.car_list
        """
        return self.car_list

    def try_solution(self, solution):
        """
        Tries using a list of moves as input

        Returns boolean
        """
        for move in solution:
            command_list = move.split()
            command = command_list[1].split(",")
            command = [int(command[0]), int(command[1])]
            self.move(command, int(command_list[0]), self.car_list)
            if self.won():
                return True
        return False
