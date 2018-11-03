class Bord(object):
    """ Defines a board. """
    def __init__(self, entrance):
        self.entrance = entrance
        self.coordinate = []

    def load(self, coordinate):
        self.coordinate.append(coordinate)

    def __str__(self):
        return(f"{self.coordinate}")
