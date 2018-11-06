class Bord(object):
    """ Defines a board. """
    def __init__(self, entrance):
        self.entrance = entrance
        self.coordinate = []

    def load(self, coordinate):
        self.coordinate.append(coordinate)

    def is_occupied(self):
        for block in self.coordinate:
            if block:
                return False
            else:
                return True

    def __str__(self):
        return(f"{self.coordinate}")
