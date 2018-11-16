from code.rushhour import Rushhour
# from code.algorithms.random_things import Randomize
from code.algorithms.random_possible_moves import Randomize
from code.classes.load_cars import LoadCars


def main():
    things = LoadCars("3")
    car_list = things.car_list
    board = things.board
    # how to import willekeurig
    rushhour = Rushhour(car_list, board)
    Randomize(rushhour)

if __name__ == "__main__":
    main()
