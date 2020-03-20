import random


def p_board():
    for i in range(0, len(board)):
        print(board[i])


def random_square():
    locations = []
    for i in range(0, len(board)):
        for j in range(0, len(board[i])):
            if board[i][j] == 0:
                loc = [i, j]
                locations.append(loc)
    chosen_coord = locations[random.randint(0, len(locations)-1)]
    chosen_value = random.randint(0, 9)
    if chosen_value == 9:
        board[chosen_coord[0]][chosen_coord[1]] = 4
    else:
        board[chosen_coord[0]][chosen_coord[1]] = 2


#         make everything move
def moveright():
    for i in range(3,0,-1):
        pass



board = [[0 for i in range(4)] for j in range(4)]

# TODO: Move Function, Hueristic, MiniMax, Alpha-Beta Pruning

def heuristic():
    return 1

def generate_possible_user_moves():
    pass

def generate_possible_computer_moves():
    pass

# up, down, left, right
def expecti_max(board, depth, is_user_turn):
    if depth == 5:
        return heuristic()

    if is_user_turn:
        max_score = 0
        index = 0

        possible_moves = generate_possible_user_moves()
        # we want to know max score
        for x in range(0, len(possible_moves)):
            depth += 1
            if expecti_max(possible_moves[x],depth, False) > max_score:
                max_score = possible_moves[x]
                index = x
        return max_score
    else:
        depth += 1
        possible_moves = generate_possible_computer_moves()
#         we want to know average score
        average = 0
        for x in range(0,len(possible_moves)):
            expecti_max(possible_moves[x], depth, True)
            average += 0
        return average
