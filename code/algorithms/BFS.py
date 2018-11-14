from collections import defaultdict, deque
from archive import Archive

class Graph(object):

    def __init__(self, game):
        """Initialization method that creates a dictionary to store graph."""
        self.graph = []
        game = game
        game.bfs(game)

    def add_edge(self, game, distance, visited):
        """Function that adds edge archive to the graph."""
        # iterate over all possible moves in the game and add them to the tree
        for move in game.possible_move():
            board_hashed = hash(game.board)
            parent_hashed = hash(game.update_board())
            archive = Archive(move, board_hashed, parent_hashed, distance, visited)
            self.graph.append(archive)

    def bfs(self, game):
        """Function that print the Breadth First Traversal from the given source"""
        # define the first board that will be played from
        source = hash(game.board)
        self.distance = 0
        # do find new moves while the game has not been won
        while not game.won():
            self.distance += 1
            visited = defaultdict(bool)
            self.add_edge(game, self.distance, visited)

            queue = deque()
            queue.append(source)
            visited[source] = True
            distance[source] = 0

            while queue:
                d = queue.popleft()
                print(d, end=" ")

                for i in self.graph[d]:
                    if not visited[i]:
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
