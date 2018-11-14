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
            visual.update(game.car_list)

        # enter the main loop
        visual.done()


if __name__ == '__main__':
    sequence = ["5 0,1", "6 0,1"]
    visual = SequenceVisualization(sequence, "1")
