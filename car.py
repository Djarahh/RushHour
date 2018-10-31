class Car(object):
    """
    Describes a car object.
    """
    def __init__(self, length, color, direction, location, car):
        #length of the car, amount of blocks
        self.length = length
        #color of the car
        self.color = color
        #direction the car can move in, x direction or y direction
        self.direction = direction
        #two coordinates on the board between which the car exists
        self.location = location
        #whether the car is THE red car, yes or no
        self.car = car
    def move(new_location):
        self.location = new_location
