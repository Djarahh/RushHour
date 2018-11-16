class Rushhour(object):
    """docstring for Rushhour."""
    def __init__(self, car_list, board):
        self.car_list = car_list
        self.board = board
        self.counter = 0

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
        for command in [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]]:
            for car in self.car_list:
                option = self.check_move(car, command)
                if option:
                    for i in option:
                        if [car.id, i] not in move_list:
                            move_list.append([car.id, i])
        return move_list

    def move(self, command, id):
        """Function for moving the cars on the board"""
        # selecting the right car
        car = self.car_list[int(id) - 1]
        self.make_possible_move()
        # check if coordinates are allowed
        if self.check_move(car, command) and self.inside_boundries(car, command):
            # do the move
            car.update_coordinates(command)
            self.counter += 1
            print(self.counter)
            self.update_board()
            self.print_board()

    def check_move(self, car, command):
        """Checks if no other cars are in the way"""
        for car_rest in self.car_list:
            # the car is allowed to move on its own coordinates
            if car_rest is not car:
                # check all the coordinates in between the original coordinates
                # and the inputted coordinates
                if not self.try_temporary_command(command, car, car_rest):
                    return False
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
            if (car.coordinate[j][i] - step) is not self.board.length:
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

    def return_car_list(self):
        """Returns the self.car_list"""
        return self.car_list
