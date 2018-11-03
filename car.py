class Car(object):
    """
    Describes a car object.
    """
    def __init__(self, id, length, color, coordinate, car):
        # id of the car
        self.id = id
        #length of the car, amount of blocks
        self.length = length
        #color of the car
        self.color = color
        # coordinates of the cars
        self.coordinate = coordinate
        #whether the car is THE red car, yes or no
        self.car = car
    def move(new_location):
        self.location = new_location

    def return_coordinates(self):
        return(self.coordinate)

    # def update_coordinates(self, command):
    #     """updates coordinates"""
    #     self.coordinate

    def __str__(self):
        return(f"{self.coordinate}")
