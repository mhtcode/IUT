import copy
import random
from datetime import datetime

import matplotlib.pyplot as plt


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


def find_best_neighbor(board):
    ''' Chooses the neighbor configuration with the fewest conflicts '''

    best_neighbor = None

    for neighbor in get_neighbors(board):
        if best_neighbor is None or count_conflicts(neighbor) < count_conflicts(best_neighbor):
            best_neighbor = neighbor

    return best_neighbor


def hill_climb():
    ''' Performs hill climbing on the N-Queens problem '''

    board = create_initial_board()
    print("Initial Board:")
    print_board(board)

    current_conflicts = count_conflicts(board)
    print(f"Initial Conflicts: {current_conflicts}\n")
    iteration = 1
    counter = 0
    while True:
        best_neighbor = find_best_neighbor(board)
        new_conflicts = count_conflicts(best_neighbor)  # Count conflicts for the best neighbor
        if new_conflicts > current_conflicts:
            break  # Stop if no better neighbor is found
        if new_conflicts == current_conflicts:
            counter+=1
        if counter == 20:
            break;
        board = best_neighbor
        current_conflicts = new_conflicts

        print(f"\nIteration {iteration}:")
        print_board(board)
        print(f"Conflicts: {current_conflicts}\n")
        iteration += 1

    return current_conflicts, iteration


num_trials = 20
conflicts_list = []
iterations_list = []
execution_times = []
zero_conflicts_count = 0
for i in range(num_trials):
    print("\n\nRound {}\n------------------------".format(i + 1))
    start_time = datetime.now()
    conflicts, iterations = hill_climb()
    conflicts_list.append(conflicts)
    iterations_list.append(iterations)
    end_time = datetime.now()
    execution_times.append((end_time - start_time).total_seconds())

    if conflicts == 0:
        zero_conflicts_count += 1


average_iterations = sum(iterations_list) / num_trials

percentage_zero_conflicts = (zero_conflicts_count / num_trials) * 100
percentage_non_zero_conflicts = 100 - percentage_zero_conflicts

average_execution_time = sum(execution_times) / len(execution_times)

labels = ['Zero Conflicts', 'Non-Zero Conflicts']
sizes = [percentage_zero_conflicts, percentage_non_zero_conflicts]
colors = ['#00FF00', '#ff1465']
explode = (0.1, 0)

plt.figure(figsize=(15, 8))

plt.subplot(2, 3, 2)
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.title('Zero Conflicts Count')

plt.subplot(2, 3, 4)
plt.bar(['Average Iterations'], [average_iterations])
plt.title('Average Number of Iterations')


plt.subplot(2, 3, 5)
plt.bar(['Average Execution Time'], [average_execution_time])
plt.title('Average Execution Time')

plt.subplot(2, 3, 6)
plt.bar(['Total Execution Time'], [sum(execution_times)])
plt.title('Total Execution Time')

plt.tight_layout()
now = datetime.now()
current_time = now.strftime("%H_%M_%S")
plt.savefig(r'q2\images\Q2_{}.png'.format(current_time))
plt.show()