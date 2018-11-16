from random import randint


class Randomize(object):
    """docstring for Willekeurig."""
    def __init__(self, game):
        game = game
        self.randomize(game)

    def randomize(self, game):
        """
        Generates random commands for RushHour
        """
        counter = 0
        # while not self.won
        while not game.won():
            # pick a random car (in case of 3 cars)
            amount_cars = len(game.car_list)
            rand_id = randint(1, amount_cars)
            # find length of this car (2 or 3)
            for car in game.car_list:
                if rand_id == car.id:
                    length = car.length
            # pick a random coordinate this car should go to
            # inside the borders of the board: 6x6
            command = []
            # give three coordinates if car is length 3
            if length > 2:
                coordinate = randint(0, 3)
                command.append(coordinate)
                command.append(coordinate + 1)
                command.append(coordinate + 2)
            # give two coordinates if car is length 2
            else:
                coordinate = randint(0, 4)
                command.append(coordinate)
                command.append(coordinate + 1)
            game.move(command, rand_id)
            game.update_board()
            game.print_board()
            print(counter)
            counter += 1
