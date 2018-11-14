# Class that visualizes a certain board from RushHour

import tkinter as tk
from car_visual import Car

# class SequenceVisualization:


class BoardVisualization:
    def __init__(self):
        """Visualizes a RushHour board with cars

           board = (Board object with .entrance, .grid, .length)
           cars = (list of cars with .id, .length, .color, .coordinate,\
            .direction)
        """
        # self.board = board
        # self.cars = cars
        # self.board_length = self.board.length
        # self.width = self.board.length
        # self.height = self.board.length

        # 40 is the width of one block
        self.board_length = 6
        self.block = 40
        self.width = self.board_length*self.block
        self.height = self.board_length*self.block
        self.max_dim = self.width

        # Initialize a drawing surface
        self.master = tk.Tk()
        self.w = tk.Canvas(self.master, width=500, height=500)
        self.w.pack()
        self.master.update()

        # Draw white squares
        self.blocks = {}
        for i in range(self.board_length):
            for j in range(self.board_length):
                x1, y1 = self.map_coords(i*40, j*40)
                x2, y2 = self.map_coords(i*40 + 40, j*40 + 40)
                self.blocks[(i, j)] = self.w.create_rectangle(x1, y1, x2, y2,
                                                              fill="white")

        self.load_cars()
        self.text = self.w.create_text(25, 0, anchor='nw', text="This is the\
         solution")
        self.master.update()

        self.master.mainloop()

    def map_coords(self, x, y):
        """Maps grid positions to window positions (in pixels)."""
        return (250 + 450 * ((x - self.width / 2.0) / self.max_dim),
                250 + 450 * ((self.height / 2.0 - y) / self.max_dim))

    def load_cars(self):
        """Loads in the cars"""
        for car in self.cars:
            coordinates = car.coordinate
            color = car.color
            for coordinate in coordinates:
                i = coordinate[0]
                j = coordinate[1]
                x1, y1 = self.map_coords(i*40, j*40)
                x2, y2 = self.map_coords(i*40 + 40, j*40 + 40)
                self.blocks[(i, j)] = self.w.create_rectangle(x1, y1, x2, y2, fill=color)



    def status_string(self):
        """Returns a status string to print with the board"""





if __name__ == '__main__':
    visual = BoardVisualization()
