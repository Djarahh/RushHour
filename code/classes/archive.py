class Archive(object):
    """docstring for Archive."""
    def __init__(self, sequency, current_board, old_board):
        self.sequency = sequency
        self.hash = current_board
        self.parent = old_board
        self.neighbour = 0
