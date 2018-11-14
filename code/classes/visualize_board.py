# Class that visualizes a certain board from RushHour

import tkinter as tk


class BoardVisualization:
    def __init__(self, board, cars, counter):
        """
        Visualizes a RushHour board with cars

        board = (Board object with .entrance, .grid, .length)
        cars = (list of cars with .id, .length, .color, .coordinate, .direction)
        """

        self.board = board
        self.cars = cars
        self.block = 40
        self.board_length = self.board.length
        self.width = self.board.length*self.block
        self.height = self.board.length*self.block
        self.max_dim = self.width
        self.counter = counter

        # Initialize a drawing surface
        self.master = tk.Tk()
        self.w = tk.Canvas(self.master, width=500, height=500)
        self.w.pack()
        self.master.update()

        # Initialize text
        self.text = self.w.create_text(25, 0, anchor='nw',
                                       text="Let's see the solution")

        self.draw_board(self.cars)

        self.master.update()

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
                x1, y1 = self.map_coords(i*40, self.width - j*40)
                x2, y2 = self.map_coords(i*40 + 40, self.width - j*40 - 40)
                self.blocks[(i, j)] = self.w.create_rectangle(x1, y1, x2, y2,
                                                              fill=color)

    def status_string(self, counter):
        """Returns a status string to print with the board"""
        return (f"This is board {counter}")

    def draw_board(self, cars):
        """Draws the board"""

        # Draw white blocks
        self.blocks = {}
        for i in range(self.board_length):
            for j in range(self.board_length):
                x1, y1 = self.map_coords(i*40, j*40)
                x2, y2 = self.map_coords(i*40 + 40, j*40 + 40)
                self.blocks[(i, j)] = self.w.create_rectangle(x1, y1, x2, y2,
                                                              fill="white")
        # Color in the car blocks
        self.cars = cars
        self.load_cars()
        self.master.update()

    def update(self, cars, counter):
        """Updates the board visualization"""

        # Draw the board
        self.draw_board(cars)

        # Update text
        self.w.delete(self.text)
        self.text = self.w.create_text(25, 0, anchor='nw',
                                       text=self.status_string(counter))

    def done(self):
        """Goes into the main loop"""
        self.master.mainloop()


if __name__ == '__main__':
    visual = BoardVisualization()
