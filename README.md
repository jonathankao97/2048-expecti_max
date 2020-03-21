# 2048 Expectimax AI Implementation
The aim of this project is to create an AI to score as well as possible on the popular [2048](https://play2048.co/) game. 

## Design Choice: Expectimax vs Minimax
Similar to the Minimax algorithm, Expectimax runs a complete search of all possible game states after a given number of moves. Given all possible states, Expectimax returns an optimal solution. The implementation is similar to that of [DFS](https://en.wikipedia.org/wiki/Depth-first_search) and is recursive in nature. Read more about expectimax and minimax [here](https://en.wikipedia.org/wiki/Expectiminimax)

Expectimax was chosen as a better AI algorithm for the 2048 game since the "opponent" squares are randomly generated, not optimally selected. While expectimax may preform worse on the worst-case random square, it will preform better on average as compared to Minimax

## Heuristic
The heuristic was designed based on personal playing experience. Each square is given a "heuristic multiplier" and the total score of a given board is determined by multiplying the values of blocks with the heuristic multiplier of the square they occupy.

## Future Things
As of right now, the program can only run within a reasonable time 5/6 layers deep. Unlike minimax, pruning is more difficult. May also look to create a nice GUI to better visualize what is happening in the game and notice patterns
