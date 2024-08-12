from collections import deque


def breadth_first_search(root, a_capacity, b_capacity, a_desired, b_desired):
    visited = list()
    queue = deque([(root, [])])

    while queue:
        state, actions = queue.popleft()

        if state == (a_desired, b_desired):
            visited.append(state)
            return visited, actions

        if state not in visited:
            visited.append(state)
            x, y = state
            for action in ["fill_1", "fill_2", "empty_1", "empty_2", "1->2", "2->1"]:
                if action == "fill_1":
                    new_state = (a_capacity, y)
                elif action == "fill_2":
                    new_state = (x, b_capacity)
                elif action == "empty_1":
                    new_state = (0, y)
                elif action == "empty_2":
                    new_state = (x, 0)
                elif action == "1->2":
                    if x > 0 and y < b_capacity:
                        amount = min(x, b_capacity - y)
                        new_state = (x - amount, y + amount)
                elif action == "2->1":
                    x, y = state
                    if y > 0 and x < a_capacity:
                        amount = min(y, a_capacity - x)
                        new_state = (x + amount, y - amount)

                if new_state:
                    queue.append((new_state, actions + [action]))

    return None



a_capacity = int(input("Enter a capacity: "))
b_capacity = int(input("Enter b capacitu: "))
a_desired = int(input("Enter a desired: "))
b_desired = int(input("Enter b disired: "))

root = (0, 0)
visited, actions = breadth_first_search(
    root, a_capacity, b_capacity, a_desired, b_desired)
if actions:
    print("\nGraph: {} states visited\n-----------------------------".format(len(visited)))
    for state in visited:
        print(state)
    i = 0
    print("-----------------------------")
    for action in actions:
        i = i+1
        print("Step: {}.\t".format(i), action)
else:
    print("Faild.")
