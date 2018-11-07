# Willekeurig algoritme om het spel 'rushhour' mee te spelen

from random import randint


def Willekeurig(game):
    """
    Genereert willekeurige commands voor de auto's in het spel
    """
    # while not self.won
    counter = 0
    while not game.won():
        # pick a random car (in case of 3 cars)
        amount_cars = len(game.car_list)
        rand_id = randint(1, amount_cars)

        # give a random command
        random = randint(1, 2)
        if random == 1:
            command = '+'
        else:
            command = '-'

        game.move(command, rand_id)
        counter += 1
        game.update_board()
        game.print_board()
    return counter
