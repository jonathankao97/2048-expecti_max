import random

def pp_board(board):
    print("------------")
    for row in range(0,4):
        ret = ""
        for col in range(0,4):
            if col != 0:
                ret += " "
            ret += str(board[row][col])
        print(ret)
    print("------------")

def equivalence_relation(board1, board2):
    for row in range(0,4):
        for col in range(0,4):
            if board1[row][col] != board2[row][col]:
                return False
    return True

def is_game_over(board):
    for row in range(0,4):
        for col in range(0,4):
            if board[row][col] == 0:
                return False
    if not equivalence_relation(board, move_up(board)):
        return False
    if not equivalence_relation(board, move_down(board)):
        return False
    if not equivalence_relation(board, move_left(board)):
        return False
    if not equivalence_relation(board, move_right(board)):
        return False
    return True

def random_square(board):
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
    return board

def matrix_direction_indices(direction):
    if direction == 1:
        left = 3
        right = -1
    else:
        left = 0
        right = 4
    return left, right

def merge_left_right(board, direction):
    left, right = matrix_direction_indices(direction)
    for row in range(0,4):
        pointer = -1
        for col in range(left, right, -1*direction):
            if board[row][col] != 0:
                if pointer == -1:
                    pointer = col
                else:
                    if board[row][col] == board[row][pointer]:
                        board[row][pointer] += board[row][col]
                        board[row][col] = 0
                        pointer = -1
                    else:
                        pointer = col
    return board

def merge_up_down(board, direction):
    left, right = matrix_direction_indices(-1*direction)
    for col in range(0,4):
        pointer = -1
        for row in range(left, right, direction):
            if board[row][col] != 0:
                if pointer == -1:
                    pointer = row
                else:
                    if board[row][col] == board[pointer][col]:
                        board[pointer][col] += board[row][col]
                        board[row][col] = 0
                        pointer = -1
                    else:
                        pointer = row
    return board

def shift_left_right(board, direction):
    left, right = matrix_direction_indices(direction)
    for row in range(0,4):
        pointer = -1
        for col in range(left, right, -1*direction):
            if board[row][col] == 0 and pointer == -1:
                pointer = col
            elif board[row][col] != 0 and pointer != -1:
                board[row][pointer] = board[row][col]
                board[row][col] = 0
                pointer -= direction
    return board

def shift_up_down(board, direction):
    left, right = matrix_direction_indices(-1*direction)
    for col in range(0,4):
        pointer = -1
        for row in range(left, right, direction):
            if board[row][col] == 0 and pointer == -1:
                pointer = row
            elif board[row][col] != 0 and pointer != -1:
                board[pointer][col] = board[row][col]
                board[row][col] = 0
                pointer += direction
    return board

def move_left(board):
    return_board = [[board[j][i] for i in range(4)] for j in range(4)]
    merge_left_right(return_board, -1)
    shift_left_right(return_board, -1)
    return return_board

def move_right(board):
    return_board = [[board[j][i] for i in range(4)] for j in range(4)]
    merge_left_right(return_board, 1)
    shift_left_right(return_board, 1)
    return return_board

def move_up(board):
    return_board = [[board[j][i] for i in range(4)] for j in range(4)]
    merge_up_down(return_board, 1)
    shift_up_down(return_board, 1)
    return return_board

def move_down(board):
    return_board = [[board[j][i] for i in range(4)] for j in range(4)]
    merge_up_down(return_board, -1)
    shift_up_down(return_board, -1)
    return return_board

heuristic_multiplier = [[2**3, 2**4, 2**5, 2**6],[2**2, 2**3, 2**4, 2**5],[2**1, 2**2, 2**3, 2**4],[2**0, 2**1, 2**2, 2**3]]
def heuristic(board):
    score = 0
    for row in range(0,4):
        for col in range(0,4):
            score += board[row][col]*heuristic_multiplier[row][col]
    return score

def generate_possible_user_moves(board):
    return [move_up(board), move_down(board), move_left(board), move_right(board)]

def generate_possible_computer_moves(board):
    two_list = []
    four_list = []
    for row in range(0,4):
        for col in range(0,4):
            if board[row][col] == 0:
                board[row][col] = 2
                two_list.append([[board[j][i] for i in range(4)] for j in range(4) ])
                board[row][col] = 4
                four_list.append([[board[j][i] for i in range(4)] for j in range(4)])
                board[row][col] = 0
    return two_list, four_list

def expecti_max(board, depth, is_user_turn):
    if depth == 5:
        return heuristic(board), 0
    if is_user_turn:
        max_score = -1
        index = 0
        possible_moves = generate_possible_user_moves(board)
        for x in range(0, len(possible_moves)):
            score = expecti_max(possible_moves[x], depth+1, False)[0]
            if score > max_score:
                max_score = score
                index = x
        return max_score, index
    else:
        two_list, four_list = generate_possible_computer_moves(board)
        if len(two_list) == 0 or len(four_list) == 0:
            return 0,0
        two_average = 0
        for x in range(0,len(two_list)):
            two_average += expecti_max(two_list[x], depth+1, True)[0]
        two_average /= len(two_list)

        four_average = 0
        for x in range(0,len(four_list)):
            four_average += expecti_max(four_list[x], depth+1, True)[0]
        four_average /= len(four_list)

        return .10*four_average + .90*two_average, 0

# run game
board = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
board = random_square(board)
for i in range(0,50000):
    pp_board(board)
    print("Round", i+1, "SCORE:", heuristic(board))
    direction = expecti_max(board, 0, True)[1]
    if direction == 0:
        board = move_up(board)
    elif direction == 1:
        board = move_down(board)
    elif direction == 2:
        board = move_left(board)
    else:
        board = move_right(board)
    board = random_square(board)
    if is_game_over(board):
        print("GAME IS OVER WITH SCORE", heuristic(board))
        pp_board(board)
        break
