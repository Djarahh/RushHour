from collections import deque
from code.classes.archive import Archive
from copy import deepcopy
from code.classes.rushhour import Rushhour
from code.classes.constructive_algoritm import Constructive
import heapq


class BestFirst(Constructive):

    def __init__(self, game, final_board):
        """Initialization method that creates a dictionary to store graph, a
        heap as queue
        game = rushhour
        final_board = list, from a previous algorthm."""
        self.heap = []
        self.archive_dict = {}
        self.game = game
        self.board = game.board
        self.archive = None
        self.solution = None
        self.won = False
        self.final_car_list = final_board
        self.counter = 0

    def bfs(self):
        """Function that iterates over the graph of parent boards and children
        It pops an archive object from the queue (heap) has the lowest value"""
        source = self.game.return_car_list()
        distance = 0
        source_board = Archive(None, None, deepcopy(source), distance)
        self.archive_dict[self.hashh(source)] = source_board

        self.make_possible_babies(source, distance + 1)

        while self.heap:
            queueobject = heapq.heappop(self.heap)
            current = self.archive_dict[queueobject[1]]
            if self.won:
                print(f"The solution was found in {self.archive.distance + 1} steps.")
                print(f"Calls to possible_babies: {self.counter}")
                return self.solution
            else:
                self.make_possible_babies(current.current, current.distance + 1)
                current.current = self.hashh(current.current)
        print("No solution was found")

    def make_possible_babies(self, parent, distance):
        """Puts archive object on the heap and checks and checks if the game
        is won.
        parent =  list, contains car objects of the parent
        distance = a single number
        """
        self.counter += 1
        if self.counter % 1000 == 0:
            print(self.counter)
        self.game = Rushhour(parent, self.board)
        command_list = self.game.make_possible_move()
        for move in command_list:
            car_id = move[0]
            command = move[1]
            self.game.move(command, car_id, deepcopy(parent))
            child_car_list = self.game.return_car_list()
            if self.game.won():
                self.won = True
                self.archive = Archive(move, self.hashh(parent), deepcopy(child_car_list), distance)
                solution = deque()
                self.solution = self.make_solution(solution)
                self.car_list = child_car_list

            if not self.hashh(child_car_list) in self.archive_dict:
                archive = Archive(move, self.hashh(parent), deepcopy(child_car_list), distance)
                value = self.value_giver(self.final_car_list, child_car_list)
                # free = self.freeing_cars(parent, child_car_list)
                # value = value - free
                heapq.heappush(self.heap, (value, self.hashh(child_car_list)))
                self.archive_dict[self.hashh(child_car_list)] = archive


    def value_giver(self, final_car_list, inital_car_list):
        """Calculates the difference between xi and xf"""
        board_value = 0
        if final_car_list:
            for car in inital_car_list:
                if car.direction == "x":
                    difference = abs(car.coordinate[0][0] - final_car_list[int(car.id) - 1].coordinate[0][0])
                    board_value += difference
                else:
                    difference = abs(car.coordinate[0][1] - final_car_list[int(car.id) - 1].coordinate[0][1])
                    board_value += difference
        return board_value

    def freeing_cars(self, current_car_list, child_car_list):
        """Heuristic for freeing other cars"""
        heur_value = 0
        current_command_list = self.game.make_possible_move_with_input(current_car_list)
        child_command_list = self.game.make_possible_move_with_input(child_car_list)
        # if len(child_command_list) > len(current_command_list):
        #     heur_value = -(len(child_command_list) - len(current_command_list
        car_id_list = []
        for move in current_command_list:
            car_id_list.append(move[0])
        for move in child_command_list:
            if move[0] in car_id_list:
                heur_value += 1
        # print(heur_value)
        return(heur_value)

    def return_car_list(self):
        return self.car_list
