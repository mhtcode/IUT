import copy
import math
import random
from datetime import datetime

import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator


def print_board(board):
    for row in board:
        for col in row:
            print(col, end=' ')
        print()

def create_initial_board():
    board = [['N' for _ in range(9)] for _ in range(9)]
    for i in range(9):
        j = random.randint(0, 8)
        board[j][i] = 'Q'
    return board

def count_conflicts(board):
    conflicts = 0
    seen_conflicts = set()

    for i in range(9):
        for j in range(9):
            if board[i][j] == 'Q':
                for k in range(j + 1, 9):
                    if board[i][k] == 'Q':
                        conflict = (i, j, i, k)
                        if conflict not in seen_conflicts:
                            conflicts += 1
                            seen_conflicts.add(conflict)

                    if 0 <= i - (k - j) < 9 and board[i - (k - j)][k] == 'Q':
                        conflict = (i, j, i - (k - j), k)
                        if conflict not in seen_conflicts:
                            conflicts += 1
                            seen_conflicts.add(conflict)

                    if 0 <= i + (k - j) < 9 and board[i + (k - j)][k] == 'Q':
                        conflict = (i, j, i + (k - j), k)
                        if conflict not in seen_conflicts:
                            conflicts += 1
                            seen_conflicts.add(conflict)

    return conflicts

def get_neighbors(board):
    neighbors = []

    for i in range(9):
        for j in range(9):
            if board[i][j] == 'Q':
                for k in range(9):
                    if k != j:
                        neighbor = copy.deepcopy(board)
                        neighbor[i][j] = 'N'
                        neighbor[k][j] = 'Q'
                        neighbors.append(neighbor)

    return neighbors


def simulated_annealing(initial_temperature, cooling_rate, max_iterations):
    current_board = create_initial_board()
    current_temperature = initial_temperature

    for iteration in range(max_iterations):
        neighbors = get_neighbors(current_board)
        random_neighbor = random.choice(neighbors)
        delta_e = count_conflicts(random_neighbor) - count_conflicts(current_board)

        if delta_e < 0 or random.uniform(0, 1) < math.exp(-delta_e / current_temperature):
            current_board = random_neighbor

        current_temperature *= cooling_rate

    return (current_board, count_conflicts(current_board))


initial_temperature = 100.0
cooling_rate = 0.999
max_iterations = 10000

num_trials = 20
conflicts_list = []
iterations_list = []
execution_times = []
zero_conflicts_count = 0
for i in range(num_trials):
    print("\n\nRound {}\n------------------------".format(i + 1))
    start_time = datetime.now()
    solution_board, conflicts = simulated_annealing(initial_temperature, cooling_rate, max_iterations)
    print_board(solution_board)
    print(f"Conflicts: {conflicts}\n")
    conflicts_list.append(conflicts)
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
plt.annotate(f'Initial Temperature: {initial_temperature}', xy=(0.5, 0.6), xycoords='axes fraction', ha='center', va='center', fontweight='bold')
plt.annotate(f'Temperature Rate: {cooling_rate}', xy=(0.5, 0.5), xycoords='axes fraction', ha='center', va='center', fontweight='bold')
plt.annotate(f'Max Iterations: {max_iterations}', xy=(0.5, 0.4), xycoords='axes fraction', ha='center', va='center', fontweight='bold')
plt.axis('off')

plt.subplot(2, 3, 5)
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.2f%%', shadow=True, startangle=140)
plt.title('Zero Conflicts Count')




plt.subplot(2, 3, 4)
average_execution_time = round(average_execution_time, 4)
plt.annotate(f'Average Execution Time(per round): {average_execution_time}s',  xy=(0.5, 0.5), xycoords='axes fraction', ha='center', va='center', fontweight='bold')
plt.axis('off')


plt.subplot(2, 3, 6)
total_execution_time = round(sum(execution_times), 4)
plt.annotate(f'Total Execution Time: {total_execution_time}s',  xy=(0.5, 0.5), xycoords='axes fraction', ha='center', va='center', fontweight='bold')
plt.axis('off')

plt.tight_layout()
now = datetime.now()
current_time = now.strftime("%H_%M_%S")
plt.savefig(r'q3\images\Q3_{}.png'.format(current_time))
plt.show()
