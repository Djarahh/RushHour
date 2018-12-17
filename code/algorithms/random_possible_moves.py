from random import randint
import sys


class Randomize(object):
    """The randomize class contains an algorith which chooses random numbers
    from a list of possible moves"""
    def __init__(self, game, initial_car_list):
        """Initialization of Randomize function
        game = string, only one number"""
        self.game = game
        self.initial_car_list = initial_car_list

    def run(self):
        """Chooses a random move from the move_list. The move_list contains
        all possible moves, formatted in
        [car.id, [coordinate[1], coordinate[2]]]"""
        sequence = []
        counter_spinner = 0
        print("running...")
        while not self.game.won():
            counter_spinner += 1
            self.runner(counter_spinner % 4)
            command_list = self.game.make_possible_move()
            rand_int = randint(0, len(command_list) - 1)
            input = command_list[rand_int]
            car_id = input[0]
            command = input[1]
            self.game.move(command, car_id, self.game.car_list)
            if self.initial_car_list == self.game.car_list:
                sequence = []
            move = [car_id, command]
            sequence.append(move)
            if self.game.car_list == self.initial_car_list:
                sequence = []
        print("Congratulations, you have found a random solution!")
        return sequence

    def runner(self, counter):
        """Progress spinner cause its awesome"""
        # turning tables
        syms = ['\\', '|', '/', '-']
        bs = "\b"
        sym = syms[counter]
        sys.stdout.write("\b%s" % sym)
        sys.stdout.flush()
