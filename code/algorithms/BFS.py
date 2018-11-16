from collections import defaultdict, deque
from classes.archive import Archive

class Graph(object):

    def __init__(self, game):
        """Initialization method that creates a dictionary to store graph."""
        self.archive_list = []
        game = game
        game.bfs(game)

    def make_queue(self, game, distance):
        """Function that adds edge archive to the graph."""
        # iterate over all possible moves and add them to a queue and archive_list
        self.queue = []
        car_list_parent = self.game.car_list
        for move in game.possible_move():
            archive = Archive(move, car_list_parent, distance)
            self.archive_list.append(archive)
            self.queue.append(archive)

    def bfs(self, game):
        """Function that print the Breadth First Traversal from the given source"""
        # define the first board that will be played from
        source = game.return_car_list()
        distance = 0
        source_board = Archive("None", source, distance)
        self.archive_list.append(source_board)

        # do find new moves while the game has not been won
        while not game.won():
            distance += 1
            command_list = game.make_possible_move()

            for input in command_list:
                car_id = input[0]
                command = input[1]
                child_car_list = game.move(command, car_id)



        while not game.won():
            distance += 1

            # add all possible moves to the queue and add to archive
            self.make_queue(game, distance)

            while self.queue:
                d = self.queue.popleft()
                # print(d, end=" ")

                for i in self.graph[d]:
                    if not self.visited[i]:
                        # check the move and if won
                        # break --> a solution has been found within [distance] steps
                        queue.append(i)
                        visited[i] = True
                        distance[i] = distance[d] + 1


#
#
# BFS (G, s)                   #/Where G is the graph and s is the source node
#       let Q be queue.
#       Q.enqueue( s ) #//Inserting s in queue until all its neighbour vertices are marked.
#
#       mark s as visited.
#       while ( Q is not empty)
#            #//Removing that vertex from queue,whose neighbour will be visited now
#            v  =  Q.dequeue( )
#
#           #//processing all the neighbours of v
#           for all neighbours w of v in Graph G
#                if w is not visited
#                         Q.enqueue( w )             #//Stores w in Q to further visit its neighbour
#                         mark w as visited.
