from collections import deque
from code.classes.archive import Archive
from copy import deepcopy


class Graph(object):

    def __init__(self, game):
        """Initialization method that creates a dictionary to store graph."""
        self.queue = deque()
        self.archive_list = []
        self.game = game
        self.bfs(game)

    def make_queue(self, distance, car_list_parent):
        """Function that adds edge archive to the graph."""
        # iterate over all possible moves and add them to a queue and archive_list
        command_list = self.game.make_possible_move()
        for move in command_list:
            archive = Archive(move, deepcopy(car_list_parent), distance)
            self.archive_list.append(archive)
            self.queue.append(archive)

    def bfs(self, game):
        """Function that print the Breadth First Traversal from the given source"""
        # define the first board that will be played from
        source = self.game.return_car_list()
        distance = 0
        source_board = Archive("None", deepcopy(source), distance)
        self.archive_list.append(source_board)

        # put the first possible moves into the queue
        self.make_queue(distance + 1, source)

        # play all possible moves from queue while the game has not been won
        while self.queue:
            d = self.queue.popleft()
            move = d.move
            car_list_parent = d.parent
            car_id = move[0]
            command = move[1]
            self.game.move(command, car_id, car_list_parent)
            child_car_list = self.game.return_car_list()
            # if the game has been won by performing the last move return the
            # amount of steps that were performed and break, else put the options
            # that are made in the queue
            if self.game.won():
                print(f"the solution was found in {d.distance} steps")
                return print(f"the solution was found in {d.distance} steps")
            else:
                self.make_queue(d.distance + 1, child_car_list)

            # hash the parent board to save space
            d.children_made(True)
