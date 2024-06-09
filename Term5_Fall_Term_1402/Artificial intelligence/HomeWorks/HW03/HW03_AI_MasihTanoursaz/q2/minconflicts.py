import copy
import random

global MAX_ITERATIONS 
MAX_ITERATIONS = 1000


def print_board(board):
    ''' Prints the chess board to the console '''

    for row in board:
        for col in row:
            print(col, end=' ')
        print('\t')

def create_initial_board():
    ''' Creates a 9x9 board with a random queen placement '''

    board = [['N' for i in range(9)] for j in range(9)]
    for i in range(9):
        j = random.randint(0, 8)
        board[j][i] = 'Q'
    return board

def count_conflicts(board):
    ''' Counts the number of conflicts between queens in a given configuration '''

    conflicts = 0
    seen_conflicts = set()

    for i in range(9):
        for j in range(9):
            if board[i][j] == 'Q':
                # Check conflicts in the same row
                for k in range(j + 1, 9):
                    if board[i][k] == 'Q':
                        conflict = (i, j, i, k)
                        if conflict not in seen_conflicts:
                            conflicts += 1
                            seen_conflicts.add(conflict)

                # Check conflicts in the upper-right diagonal
                for k in range(1, min(i + 1, 9 - j)):
                    if board[i - k][j + k] == 'Q':
                        conflict = (i, j, i - k, j + k)
                        if conflict not in seen_conflicts:
                            conflicts += 1
                            seen_conflicts.add(conflict)

                # Check conflicts in the lower-right diagonal
                for k in range(1, min(9 - i, 9 - j)):
                    if board[i + k][j + k] == 'Q':
                        conflict = (i, j, i + k, j + k)
                        if conflict not in seen_conflicts:
                            conflicts += 1
                            seen_conflicts.add(conflict)

    return conflicts


def get_neighbors(board):
    ''' Generates all possible neighbor configurations for a 9x9 board '''

    neighbors = []

    for row in range(9):
        for col in range(9):
            if board[row][col] == 'Q':
                for k in range(9):
                    if k != row:
                        neighbor = copy.deepcopy(board)
                        neighbor[row][col] = 'N'
                        neighbor[k][col] = 'Q'
                        neighbors.append(neighbor)

    # Include neighbors with the same number of conflicts
    current_conflicts = count_conflicts(board)
    for neighbor in neighbors.copy():
        if count_conflicts(neighbor) == current_conflicts:
            neighbors.append(neighbor)

    return neighbors


def local_search():
    ''' Performs hill climbing on the N-Queens problem '''

    board = create_initial_board()
    print("Initial Board:")
    print_board(board)
    counter = 0
    current_conflicts = count_conflicts(board)
    print(f"Initial Conflicts: {current_conflicts}\n")
    current_state = board
    while counter <= MAX_ITERATIONS :
        counter +=1
        neighbors = get_neighbors(current_state)
        random_neighbor = random.choice(neighbors)
        if(count_conflicts(random_neighbor) <= current_conflicts):
            current_state = random_neighbor
            current_conflicts = count_conflicts(current_state) 
            if(current_conflicts == 0):
                print("Result:")
                print_board(current_state)
                print(f"Conflicts: {current_conflicts}\n")
                return True

    return False



if(local_search()):
    print("""Solution found:)\n""")
else:
    print("Failed to find solution!!\n")
    