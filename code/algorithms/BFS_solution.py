from collections import deque
from code.classes.archive import Archive
from copy import deepcopy
from code.classes.rushhour import Rushhour
from code.classes.constructive_algoritm import Constructive

class Graph(Constructive):

    def __init__(self, game):
        """Initialization method that creates a dictionary to store graph, a
        queue to iterate over the graph and initialize the game.
        game = rushhour object"""
        self.queue = deque()
        self.archive_dict = {}
        self.game = game
        self.board = game.board
        self.solution = None
        self.won = False

    def run(self):
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

    def add_to_archive(self, move, parent, child_car_list, distance):
        """Creates archive object and adds it to the archive.
        move = [car_id, command], contains info on the move which has been made
        parent = list of car objects of parent board
        child_car_list = list of car objects of current board
        distance = int, distance from starting board """
        archive = Archive(move, self.hashh(parent), deepcopy(child_car_list), distance)
        self.archive_dict[self.hashh(child_car_list)] = archive
        self.put(archive)

    def check_child(self, child_car_list, distance):
        """Checks if the child is in the archive
        Returns bolean"""
        return not self.hashh(child_car_list) in self.archive_dict

    def put(self, archive):
        """Adds archive object to queue
        archive = archive object"""
        self.queue.append(archive)
