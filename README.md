# 2048 Expectimax AI Implementation
The aim of this project is to create an AI to score as well as possible on the popular [2048](https://play2048.co/) game. 

## Design Choice: Expectimax vs Minimax
Similar to the Minimax algorithm, Expectimax runs a complete search of all possible game states after a certain number of moves. Given all possible stats, Expectimax returns an optimal solution.

Expectimax was implemented for the 2048 game since the "opponent" squares are randomly generated and doesn't play optimally. Thus, it makes more sense to take an average of all scenarios.

## Heuristic
The heuristic was designed based on personal playing experience. Each square is given a "heuristic multiplier" and the total score of a given board is determined by multiplying the values of blocks with the heuristic multiplier of the square they occupy.


