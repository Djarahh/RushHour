# Willekeurig algoritme om het spel 'rushhour' mee te spelen

from random import randint

def willekeurig():
    """
    Genereert willekeurige commands voor de auto's in het spel
    """
    # while not self.won
    while not self.won():
        # pick a random car (in case of 3 cars)
        amount_cars = len(self.car_list)
        rand_id = randint(1, amount_cars)

        # give a random command
        random = randint(1,2)
        if random == 1:
            command = '+'
        else:
            command = '-'

        self.move(command, rand_id)
        self.update_board()
        self.print_board()


if __name__ == '__main__':
    willekeurig()
