global board_size
board_size = 15

def printBoard(board):
    for i in range(board_size):
        for j in range(board_size):
            print(board[i][j], end = " ")
        print()

def canplace(board, row, col):

    # Check this row on left side
    for i in range(col):
        if board[row][i] == "Q":
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1),
                    range(col, -1, -1)):
        if board[i][j] == "Q":
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, board_size, 1),
                    range(col, -1, -1)):
        if board[i][j] == "Q":
            return False

    return True

def count_conflicts(board):
    ''' Counts the number of conflicts between queens in a given configuration '''

    conflicts = 0
    seen_conflicts = set()

    for i in range(board_size):
        for j in range(board_size):
            if board[i][j] == 'Q':
                # Check conflicts in the same row
                for k in range(j + 1, board_size):
                    if board[i][k] == 'Q':
                        conflict = (i, j, i, k)
                        if conflict not in seen_conflicts:
                            conflicts += 1
                            seen_conflicts.add(conflict)

                # Check conflicts in the upper-right diagonal
                for k in range(1, min(i + 1, board_size - j)):
                    if board[i - k][j + k] == 'Q':
                        conflict = (i, j, i - k, j + k)
                        if conflict not in seen_conflicts:
                            conflicts += 1
                            seen_conflicts.add(conflict)

                # Check conflicts in the lower-right diagonal
                for k in range(1, min(board_size - i, board_size - j)):
                    if board[i + k][j + k] == 'Q':
                        conflict = (i, j, i + k, j + k)
                        if conflict not in seen_conflicts:
                            conflicts += 1
                            seen_conflicts.add(conflict)

    return conflicts

def backtracking(board, col):
    
    # base case
    if col >= board_size:
        return True
    for i in range(board_size):

        if canplace(board, i, col):
            board[i][col] = "Q"

            # recursively try to place queens
            if backtracking(board, col + 1) == True:
                return True
                
            board[i][col] = "N"

    return False

def run():
    board = [["N" for i in range(board_size)] for j in range(board_size)]

    if backtracking(board, 0) == False:
        print ("No Possible Solution exists")
        return False

    printBoard(board)
    print(f"Conflicts: {count_conflicts(board)}\n")
    return True

run()