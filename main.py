import os
import sys
directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "code", "classes"))
sys.path.append(os.path.join(directory, "data"))
sys.path.append(os.path.join(directory, "code", "algoritmes"))

# importeer het spel, de algoritmes en een visualisatie
from rushhour.py import Rushhour
from willekeurig.py import Willekeurig

def main():
    game = Rushhour(gamename)

    # implementeer willekeurig algoritme
    A = Willekeurig(game)


if __name__ == '__main__':
    main()
