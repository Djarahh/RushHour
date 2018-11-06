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
            self.coordinate[0][1] = command[0]
            self.coordinate[1][1] = command[1]
        else:
            self.coordinate[0][0] = command[0]
            self.coordinate[1][0] = command[1]
        if len(self.coordinate) == 3:
            if self.direction == "x":
                self.coordinate[0][2] = command[2]
            else:
                self.coordinate[2][0] = command[2]

    def direction(self):
        if self.coordinate[0][0] == self.coordinate[1][0]:
            return("x")
        else:
            return("y")

    def return_coordinates(self):
        return(self.coordinate)

    def __str__(self):
        return(f"{self.coordinate}")
