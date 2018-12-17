# Project RushHour

RushHour is a fun game with an amount of colourful cars on a game board. The goal of this game is to move
the red car to the exit of the game board. For this project we have tried to solve seven different game boards
of sizes 6x6, 9x9 and 12x12.

## Getting Started

### Requirements

There are no requirements for our code.

### Structure

Here is a short summary of the structure of our program:
+ code (here you can find all python scripts)
  + algorithms (here you can find all of our algorithms)
  + classes (here you can find all classes used)
  + visualisation (here you can find the files for the visualisation)
+ data (here you can find all data necessary for implementing the game boards)
+ exploration (here you can find our exploration of the problem)
+ results (here you can find the results of the algorithms)

### Testing

To run the code with the default configuration(algorithm: random, game: 1, visualisation: on) use:

*python main.py*

To choose your own algorithm, game and other parameters use this format:

*python main.py [-h] [-b board] [-be [width]] [-a algorithm] [-vis [visualize]]
               [-bou [bound]] [-d [deltabound]]*

+ -h shows a help message and exits
+ -b board, choose a board with the following choices [1, 2, 3, 4, 5, 6, 12] (default = board 1)
+ -be [width], the width of the beam search (default = 100)
+ -a algorithm, choose an algorithm from the following choices ["bfs", "best", "dfs", "bnb", "random", "beam"]
+ -vis [visualize], turns visualisation on or off by choosing from [yes (y) or no (n)] (default = yes)
+ -bou [bound], the starting bound of the branch and bound algorithm (default = 80)
+ -d [deltabound], decrease of the updated bound of the branch and bound algorithm (default = 10)

### Output

While the algorithms are run you can see different output per algorithm,
here a short explanation of the output:

BFS: deepest point reached so far
Best: deepest point reached so far
Branch and Bound: the updated bound
Beam: deepest point reached so far

### Warning

The BFS algorithm takes up a lot of memory, so we would advise users to not run this algorithm with 
boards that are larger than 6x6.

## Authors

Team: Gargamel and the Smurfs

+ Yara Djaidoen
+ Stan Helsloot
+ Tula Kaptein

## Acknowledgments

We would like to thank:

+ Quinten van der Post for being our tech assistant and helping us through all of our struggles
+ Minor Programmeren for making it possible to learn so much of programming in such a short time
+ The world wide web for providing us with code, how to's and error solutions
