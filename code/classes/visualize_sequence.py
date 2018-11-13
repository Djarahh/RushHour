# Class that visualizes a sequence of RushHour Boards

import tkinter as tk


class SequenceVisualization:
    def __init__(self, sequence):
        """
        Visualizes a sequence of RushHour boards

        sequence = (a list of boards, that are lists of cars)
        """

        self.sequence = sequence

        for board in self.sequence:
            self.visualize(board)

    def visualize(self, board):
        """
        Visualizes a board
        """
        self.board = board
