from collections import deque
from code.classes.archive import Archive
from copy import deepcopy
from code.classes.rushhour import Rushhour
from code.classes.constructive_algoritm import Constructive

class Graph(Constructive):

    def __init__(self, game):
        """Initialization method that creates a dictionary to store graph, a
        queue to iterate over the graph and initialize the game."""
        self.queue = deque()
        self.archive_dict = {}
        self.game = game
        self.board = game.board
        self.solution = None
        self.won = False

    def bfs(self):
        """Iterates over the graph and retuns solution when game is won"""
        source = self.game.return_car_list()
        distance = 0
        source_board = Archive(None, None, deepcopy(source), distance)
        self.archive_dict[self.hashh(source)] = source_board

        self.make_possible_children(source, distance + 1)

        while self.queue:
            current = self.queue.popleft()
            if self.won:
                print(f"The solution was found in {self.archive.distance + 1} steps.")
                return self.solution
            else:
                self.make_possible_children(current.current, current.distance + 1)
        print("No solution was found")

    def check_child(self, child_car_list, distance):
            return not self.hashh(child_car_list) in self.archive_dict

    def put(self, archive):
        self.queue.append(archive)


    def return_car_list(self):
        return self.final_board
