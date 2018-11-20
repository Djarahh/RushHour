# Class that visualizes a certain board from RushHour

import tkinter as tk


class BoardVisualization:
    def __init__(self, game):
        """
        Visualizes a RushHour board with cars

        board = Board object (with .entrance, .grid, .length)
        cars = list (cars with .id, .length, .color, .coordinate, .direction)
        counter = integer
        """

        self.board = game.board
        self.cars = game.cars
        self.block = 40
        self.board_length = self.board.length
        self.width = self.board.length*self.block
        self.height = self.board.length*self.block
        self.max_dim = self.width
        self.counter = game.counter

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
        """
        Maps grid positions to window positions (in pixels).

        x = integer (x position on the game board)
        y = integer (y position on the game board)

        """
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
        """
        Returns a status string to print with the board

        counter = integer (counts the moves)
        """
        return (f"This is board {counter}")

    def draw_board(self, cars):
        """
        Draws the board

        cars = list (of cars)

        """
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
        """
        Updates the board visualization

        cars = list (of cars)
        counter = integer (counts the moves)
        """
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
