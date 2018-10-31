from block.py import Block 

class Rushhour(object):
    """docstring for Rushhour."""
    def __init__(self, arg):
        self.arg = arg

    def load_board(length):
        """Function for loading the board"""
        bord = Bord()
        for x in range(length):
            for y in range(length):
                # use bord.load function to append coordinates to the board
                bord.load(Block(x,y))

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
