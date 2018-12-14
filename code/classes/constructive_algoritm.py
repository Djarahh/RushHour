from .rushhour import Rushhour
from copy import deepcopy
from .archive import Archive
from collections import deque

class Constructive(object):
    """Class that contains functions that are used in all constructive
    algoritms. """

    def hashh(self, car_list):
        """Hashes a car list (configuration of a board).
        car_list = list, contains car object of the current board"""
        coordinates = []
        for item in car_list:
            coordinates.append(item.coordinate)
        hash_code = hash(str(coordinates))
        return hash_code

    def make_solution(self, solution):
        """Traces the solution back and returns the solution
        solution = deque(), a queue that is empty"""
        cursor = self.archive
        while cursor.parent:
            # while not end of solution
            solution.appendleft(cursor.move)
            cursor = self.archive_dict[cursor.parent]
        solution.append([1, [(self.game.board.entrance[0] - 1),
                        self.game.board.entrance[0]]])
        return solution

    def make_possible_children(self, parent, distance):
        """Creates a queue and puts all board states that have not yet been
        visited in the archive. Parent = list of car objects, distance = integer """
        self.game = Rushhour(parent, self.board)
        command_list = self.game.make_possible_move()
        for move in command_list:
            car_id = move[0]
            command = move[1]
            self.game.move(command, car_id, deepcopy(parent))
            child_car_list = self.game.return_car_list()
            if self.game.won():
                if self.winning(move, parent, child_car_list, distance):
                    break
            elif self.check_child(child_car_list, distance):
                self.add_to_archive(move, parent, child_car_list, distance)
                # archive = Archive(move, self.hashh(parent), deepcopy(child_car_list), distance)
                # self.archive_dict[self.hashh(child_car_list)] = archive
                # self.put(archive)

    def winning(self, move, parent, child_car_list, distance):
        self.won = True
        self.archive = Archive(move, self.hashh(parent), deepcopy(child_car_list), distance)
        solution = deque()
        self.solution = self.make_solution(solution)
        self.final_board = child_car_list
        return True
