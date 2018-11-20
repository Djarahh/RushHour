class Board(object):
    """ Defines a board. """
    def __init__(self):
        """Initialization of Board object."""
        self.entrance = []
        self.grid = 0
        self.length = 0

    def set_zero(self):
        """Sets all dictionary values of grid to 0"""
        for y in range(self.length):
            for x in range(self.length):
                self.grid[x, y] = 0

    def __str__(self):
        return(f"{self.coordinate}")
