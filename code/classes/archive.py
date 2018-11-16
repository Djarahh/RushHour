class Archive(object):
    """docstring for Archive."""
    def __init__(self, step, current_board, old_board):
        self.step = step
        self.hash = current_board
        self.parent = old_board
        self.distance = 0
        self.visited = False

    def change_visited(self, bool):
        if bool == True:
            self.visited = True
        return False
