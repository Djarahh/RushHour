# test program for main

# voeg de huidige structuur toe aan path
import os
import sys

directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "code", "classes"))
sys.path.append(os.path.join(directory, "data"))
sys.path.append(os.path.join(directory, "code", "algoritmes"))

from car import Car
from board import Board
from random import randint
from willekeurig import Willekeurig
from rushhour import Rushhour

def main():
    # how to import willekeurig
    rushhour = Rushhour("1")
    willekeurig = Willekeurig(rushhour)



if __name__ == "__main__":
    main()
