import copy


class Car(object):
    """
    Describes a car object.
    """
    def __init__(self, id, length, color, coordinate):
        """
        Initialization of a car object.

        id = integer, id of the car
        length = integer, length of the car
        color = string, color of the car
        coordinate = list, x and y coordinates of the car
        """
        self.id = id
        self.length = length
        self.color = color
        self.coordinate = coordinate
        self.direction = self.direction()

        self.x = 0
        self.y = 0

    def update_coordinates(self, command):
        """
        Updates the coordinates

        command = list
        """
        self.update_x_y(command)
        if type(self.x) == list:
            for i in range(len(self.x)):
                self.coordinate[i][0] = self.x[i]
        else:
            for i in range(len(self.y)):
                self.coordinate[i][1] = self.y[i]

    def update_x_y(self, command):
        """
        Creates x or y function for use in the update/temp functions.
        command = list
        """
        if self.direction == "x":
            self.x = command
        else:
            self.y = command

    def direction(self):
        """
        Sets direction atribute

        returns x or y (direction)
        """
        if self.coordinate[0][1] == self.coordinate[1][1]:
            return("x")
        else:
            return("y")

    def temp_coordinates(self, command):
        """
        Function that tests whether the command is valid.
        command = list

        returns temporary car coordinates
        """
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
