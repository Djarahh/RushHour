from random import randint


class Randomize(object):
    """The randomize class contains an algorith which chooses random numbers
    from a list of possible moves"""
    def __init__(self, game, initial_car_list):
        """Initialization of Randomize function
        game = string, only one number"""
        self.game = game
        self.initial_car_list = initial_car_list

    def randomize(self):
        """Chooses a random move from the move_list. The move_list contains
        all possible moves, formatted in
        [car.id, [coordinate[1], coordinate[2]]]"""
        sequence = []
        while not self.game.won():
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
        return sequence
