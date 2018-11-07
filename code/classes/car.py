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
        # whether the car is THE red car, yes or no
        self.car = car

    def update_coordinates(self, command):
        # command = command.split(",")
        if self.direction == "x":
            if command == "+":
                self.coordinate[0][1] += 1
                self.coordinate[1][1] += 1
            else:
                self.coordinate[0][1] -= 1
                self.coordinate[1][1] -= 1
        else:
            if command == "+":
                self.coordinate[0][0] -= 1
                self.coordinate[1][0] -= 1
            else:
                self.coordinate[0][0] += 1
                self.coordinate[1][0] += 1
        if len(self.coordinate) == 3:
            if self.direction == "x":
                if command == "+":
                    self.coordinate[0][2] += 1
                else:
                    self.coordinate[0][2] -= 1
            else:
                if command == "+":
                    self.coordinate[2][0] -= 1
                else:
                    self.coordinate[2][0] += 1

    def direction(self):
        if self.coordinate[0][0] == self.coordinate[1][0]:
            return("x")
        else:
            return("y")

    def temp_coordinates(self, command):
        temp = copy.deepcopy(self.coordinate)
        if self.direction == "x":
            if command == "+":
                temp[0][1] += 1
                temp[1][1] += 1
            else:
                temp[0][1] -= 1
                temp[1][1] -= 1
        else:
            if command == "+":
                temp[0][0] -= 1
                temp[1][0] -= 1
            else:
                temp[0][0] += 1
                temp[1][0] += 1
        if len(temp) == 3:
            if self.direction == "x":
                if command == "+":
                    temp[0][2] += 1
                else:
                    temp[0][2] -= 1
            else:
                if command == "+":
                    temp[2][0] -= 1
                else:
                    temp[2][0] += 1
        return temp

    def return_coordinates(self):
        return(self.coordinate)

    def __str__(self):
        return(f"{self.coordinate}")
