from collections import deque
from code.classes.archive import Archive
from copy import deepcopy

class Graph(object):

    def __init__(self, game):
        """Initialization method that creates a dictionary to store graph."""
        self.queue = deque()
        self.archive_dict = {}
        self.game = game

    def bfs(self):

        source = self.game.return_car_list()
        distance = 0
        source_board = Archive(None, None, deepcopy(source), distance)
        self.archive_dict[self.hashh(source)] = source_board

        self.make_possible_babies(source, distance + 1)

        while self.queue:
            print(f"Queue: {len(self.queue)}")
            current = self.queue.popleft()
            if self.game.won():
                return print(f"the solution was found in {current.distance}steps.")
            else:
                self.make_possible_babies(current.parent, current.distance + 1)
        print("No soltion was found")

    def make_possible_babies(self, parent, distance):
        command_list = self.game.make_possible_move()
        for move in command_list:
            car_id = move[0]
            command = move[1]
            self.game.move(command, car_id, parent)
            child_car_list = self.game.return_car_list()

            if self.hashh(child_car_list) in self.archive_dict:
                print("YAY")
            else:
                print("NAY")
                archive = Archive(move, deepcopy(parent), deepcopy(child_car_list), distance)
                self.queue.append(archive)
                self.archive_dict[self.hashh(child_car_list)] = archive
            print(f"Length: {len(self.archive_dict)}")


    def hashh(self, car_list):
        coordinates = []
        for item in car_list:
            coordinates.append(item.coordinate)
        hash_code = hash(str(coordinates))
        return hash_code
