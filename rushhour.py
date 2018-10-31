class Rushhour(object):
    """docstring for Rushhour."""
    def __init__(self, arg):
        self.arg = arg

    def load_board(length):
        """Function for loading the board"""
        bord = Bord()
        # open file in read mode
        with open(filename, "r") as file:
            # itterate over text and strip line
            for text_line in file:
                text_line = text_line.strip()
                # check if line is information on board length
                if text_line.startswith(board):
                    text_line = text_line.rsplit()
                    for x in range(text_line[1]):
                        for y in range(text_line[1]):
                            # use bord.load function to append coordinates to the board
                                bord.load(Coordinate(x,y))
                # the order of cars: id, length, colour, location
                if text_line.isdigit():
                    id = text_line
                if text_line.startswith(length):
                    text_line = text_line.rsplit()
                    length = text_line[1]
                if text_line.startswith(color):
                    text_line = text_line.rsplit()
                    color = text_line[1]
                if text_line.startswith(location):
                    while file.readline() is not "":
                        coordinate = file.readline().split(",")
                        coordinate[0] = x
                        coordinate[1] = y
                    # make cars
                    





    def load_cars():
        """Function for loading the cars on the board"""
        pass

    def move():
        """Function for moving the cars on the board"""
        pass

    def won():
        """Win condition for the game"""
        pass


    def play():
        """Lets play a game"""
        pass
