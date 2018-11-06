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

        # find length of this car (2 or 3)
        for car in self.car_list:
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
        self.move(command, rand_id)
        self.update_board()
        self.print_board()


if __name__ == '__main__':
    willekeurig()
