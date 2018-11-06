class Block(object):
    """
    Describes a coordinateself.
    """
    def __init__(self, coordinate):
        self.coordinate = coordinate
        self.occupied = False
        self.car_id = None

    def occupy(self, bool):
        self.occupied = bool

    def __str__(self):
        return(f"{self.coordinate}. {self.occupied}")
