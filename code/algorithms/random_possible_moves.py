from random import randint


class Randomize(object):
    """The randomize class contains an algorith which chooses random numbers
    from a list of possible moves"""
    def __init__(self, game):
        game = game
        self.randomize(game)

    def randomize(self, game):
        """Chooses a random move from the move_list. The move_list contains
        all possible moves, formatted in
        [car.id, [coordinate[1], coordinate[2]]]"""
        while not game.won():
            command_list = game.make_possible_move()
            rand_int = randint(0, len(command_list) - 1)
            input = command_list[rand_int]
            car_id = input[0]
            command = input[1]
            game.move(command, car_id)
