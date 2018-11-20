from collections import deque
from code.classes.archive import Archive

class Graph(object):

    def __init__(self, game):
        """Initialization method that creates a dictionary to store graph."""
        self.queue = deque()
        self.archive_list = []
        game = game
        game.bfs(game)

    def make_queue(self, game, distance, car_list_parent):
        """Function that adds edge archive to the graph."""
        # iterate over all possible moves and add them to a queue and archive_list
        for move in self.game.make_possible_move():
            archive = Archive(move, car_list_parent, distance)
            self.archive_list.append(archive)
            self.queue.append(archive)

    def bfs(self, game):
        """Function that print the Breadth First Traversal from the given source"""
        # define the first board that will be played from
        source = game.return_car_list()
        distance = 0
        source_board = Archive("None", source, distance)
        self.archive_list.append(source_board)

        # put the first possible moves into the queue
        self.make_queue(game, distance)

        # play all possible moves from queue while the game has not been won
        while self.queue:
            d = self.queue.popleft()
            move = self.archive_list[d].move
            car_list_parent = self.archive_list[d].parent
            car_id = move.split()[2]
            command = move.split()[1]
            move(car_id, command, car_list_parent)
            child_car_list = self.game.return_car_list()

            # if the game has been won by performing the last move return the
            # amount of steps that were performed and break, else put the options
            # that are made in the queue
            if self.game.won():
                print(f"the solution was found in {self.archive_list[d].distance} steps")
                return print(f"the solution was found in {self.archive_list[d].distance} steps")
            else:
                self.make_queue(game, self.archive_list[d].distance + 1, child_car_list)

            # hash the parent board to save space
            self.archive_list[d].parent = hash(self.archive_list[d].parent)
