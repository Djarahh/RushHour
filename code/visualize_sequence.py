# Class that visualizes a sequence of RushHour Boards

import os
import sys

directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "classes"))

import tkinter as tk
from visualize_board import BoardVisualization
import time
from rushhour import Rushhour


class SequenceVisualization:
    def __init__(self, sequence, game_id):
        """
        Visualizes a sequence of RushHour boards

        sequence = (a list of moves)
        start_board = (starting board)
        """

        self.sequence = sequence
        self.game_id = game_id
        self.counter = 0

        game = Rushhour(game_id)
        visual = BoardVisualization(game.board, game.car_list, game.counter)
        for move in self.sequence:
            # wait a few seconds
            time.sleep(0.5)
            # do the move
            command = move.split()
            id = command[0]
            command = game.clean_input(command[1])
            game.move(command, id)

            # update the visualization
            visual.update(game.car_list, game.counter)

        # enter the main loop
        visual.done()


if __name__ == '__main__':
    sequence = ["2 0,1", "4 0,1", "3 2,3", "5 2,3", "7 0,1", "6 0,1,2", "1 0,1", "9 4,5", "11 2,3", "12 1,2", "13 1,2", "11 4,5", "9 2,3", "6 3,4,5", "1 4,5"]
    visual = SequenceVisualization(sequence, "3")
