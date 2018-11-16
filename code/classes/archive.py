class Archive(object):
    """docstring for Archive."""
<<<<<<< HEAD
    def __init__(self, move, car_list_parent, distance):
        self.move = move
        self.parent = car_list_parent
        self.child = car_list_self
        self.distance = 0

    def children_made(self, bool):
        if bool:
            self.parent = hash(self.parent)
=======
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
>>>>>>> e161c06683e519ebae0ef545ca2a4c5a7d4a2856
