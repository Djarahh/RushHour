from collections import deque
from code.classes.archive_dfs import Archive
from copy import deepcopy


class Tree(object):
    def __init__(self, game):
        """
        Initializes a tree object to use for depth first search
        """
        self.stack = deque()
        self.game = game
        self.archive_dict = {}

    def make_stack(self, distance, car_list_parent):
        """Function that adds to the stack"""
        command_list = self.game.make_possible_move()
        for move in command_list:
            archive = Archive(move, deepcopy(car_list_parent), distance)
            if not archive.hash_parent(move) in self.archive_dict.keys():
                print("YAY")
            self.stack.appendleft(archive)

    def check_child(self):
        """Function to check child for stack"""
        pass

    def dfs(self):
        """Function """
        # define the first board
        source = self.game.return_car_list()
        distance = 0
        # source_board = Archive(None, deepcopy(source), distance)
        # self.archive_dict[source_board.hash_parent()] = source_board
        # put first possible moves in the stack
        self.make_stack(distance + 1, source)
        # go deep!
        for i in range(5):
        # while self.stack:
            next = self.stack.popleft()
            move = next.move
            car_list_parent = next.parent
            car_id = move[0]
            command = move[1]
            # print(car_id)
            # print(command)
            self.game.move(command, car_id, car_list_parent)
            child_car_list = self.game.return_car_list()

            if self.game.won():
                return print(f"the solution was found in {next.distance} steps")
            else:
                # print(next.hash_parent())
                self.archive_dict[next.hash_parent(move)] = next
                self.make_stack(next.distance + 1, child_car_list)
        print("Solution not found")
        print(self.archive_dict.keys())
