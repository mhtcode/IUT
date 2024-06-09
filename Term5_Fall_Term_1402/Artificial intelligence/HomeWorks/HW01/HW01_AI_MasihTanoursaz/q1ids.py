from collections import deque


def depth_first_search(root, a_capacity, b_capacity, a_desired, b_desired, max_depth):
    visited = list()
    stack = deque([(root, [], 0)])

    while stack:
        state, actions, depth = stack.pop()

        if state == (a_desired, b_desired):
            return  actions

        if state not in visited and depth <= max_depth:
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
                    else:
                        continue
                elif action == "2->1":
                    if y > 0 and x < a_capacity:
                        amount = min(y, a_capacity - x)
                        new_state = (x + amount, y - amount)
                    else:
                        continue

                if new_state:
                    stack.append((new_state, actions + [action], depth + 1))

    return None

def IDS(root, a_capacity, b_capacity, a_desired, b_desired):
    max_depth = 0

    while True:
        actions = depth_first_search(root, a_capacity, b_capacity, a_desired, b_desired, max_depth)
        if actions:
            return actions
        max_depth += 1

a_capacity = int(input("Enter a capacity: "))
b_capacity = int(input("Enter b capacity: "))
a_desired = int(input("Enter a desired: "))
b_desired = int(input("Enter b desired: "))

root = (0, 0)
actions = IDS(
    root, a_capacity, b_capacity, a_desired, b_desired)
if actions:

    i = 0
    print("\nResult:\n-----------------------------")
    for action in actions:
        i = i+1
        print("Step: {}.\t".format(i), action)
else:
    print("Faild.")
