import copy

class Car(object):
    """
    Describes a car object.
    """
    def __init__(self, id, length, color, coordinate, car):
        # id of the car
        self.id = id
        # length of the car, amount of blocks
        self.length = length
        # color of the car
        self.color = color
        # coordinates of the cars
        self.coordinate = coordinate
        # direction of car
        self.direction = self.direction()
        # I want another atribute in Car: depending on the direction, the
        # coordinates must be saved as the move input (list, only x or y)
        self.x = 0
        self.y = 0

    def update_coordinates(self, command):
        """Updates the coordinates"""
        self.update_x_y(command)
        if type(self.x) == list:
            for i in range(len(self.x)):
                self.coordinate[i][0] = self.x[i]
        else:
            for i in range(len(self.y)):
                self.coordinate[i][1] = self.y[i]

    def update_x_y(self, command):
        """Creates x or y function for use in the update/temp functions"""
        if self.direction == "x":
            self.x = command
        else:
            self.y = command

    def direction(self):
        """Sets direction atribute"""
        if self.coordinate[0][1] == self.coordinate[1][1]:
            return("x")
        else:
            return("y")

    def temp_coordinates(self, command):
        """Function for testing if the inputted command is valid"""
        self.update_x_y(command)
        temp = copy.deepcopy(self.coordinate)
        if type(self.x) == list:
            for i in range(len(self.x)):
                temp[i][0] = self.x[i]
        else:
            for i in range(len(self.y)):
                temp[i][1] = self.y[i]
        return temp

    def __str__(self):
        return(f"{self.coordinate}")
