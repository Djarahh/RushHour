from collections import deque
from code.classes.archive import Archive
from copy import deepcopy
from code.rushhour import Rushhour

class Graph(object):

    def __init__(self, game):
        """Initialization method that creates a dictionary to store graph."""
        self.queue = deque()
        self.archive_dict = {}
        self.game = game
        self.board = game.board
        self.archive = None
        self.solution = None
        self.won = False

    def bfs(self):

        source = self.game.return_car_list()
        distance = 0
        source_board = Archive(None, None, deepcopy(source), distance)
        self.archive_dict[self.hashh(source)] = source_board

        self.make_possible_babies(source, distance + 1)

        while self.queue:
            current = self.queue.popleft()
            if self.won:
                print(f"The solution was found in {self.archive.distance + 1} steps.")
                return self.solution
            else:
                self.make_possible_babies(current.current, current.distance + 1)
        print("No solution was found")

    def make_possible_babies(self, parent, distance):
        self.game = Rushhour(parent, self.board)
        command_list = self.game.make_possible_move()
        for move in command_list:
            car_id = move[0]
            command = move[1]
            self.game.move(command, car_id, deepcopy(parent))
            child_car_list = self.game.return_car_list()
            if self.game.won():
                self.won = True
                self.archive = Archive(move, deepcopy(parent), deepcopy(child_car_list), distance)
                self.solution = self.make_solution()

            if not self.hashh(child_car_list) in self.archive_dict:
                archive = Archive(move, deepcopy(parent), deepcopy(child_car_list), distance)
                self.queue.append(archive)
                self.archive_dict[self.hashh(child_car_list)] = archive

    def hashh(self, car_list):
        coordinates = []
        for item in car_list:
            coordinates.append(item.coordinate)
        hash_code = hash(str(coordinates))
        return hash_code

    def make_solution(self):
        solution = deque()
        cursor = self.archive
        while True:
            # while not end of solution
            solution.appendleft(cursor.move)
            cursor = self.archive_dict[self.hashh(cursor.parent)]
            if cursor.parent == None:
                solution.append([1, [4,5]])
                break
        return solution
