# test program for main

from code.classes.car import Car
from code.classes.board import Board
from random import randint
from code.algorithm.willekeurig import Willekeurig
from code.rushhour import Rushhour

def main():
    # how to import willekeurig
    rushhour = Rushhour("1")
    willekeurig = Willekeurig(rushhour)



if __name__ == "__main__":
    main()
