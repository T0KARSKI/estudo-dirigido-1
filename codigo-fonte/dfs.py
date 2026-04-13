from utils import toggle, is_goal, state_to_tuple

def dfs(initial):
    stack = [(initial, 0)]
    visited = set()

    while stack:
        state, steps = stack.pop()

        if is_goal(state):
            return steps

        key = state_to_tuple(state)
        if key in visited:
            continue
        visited.add(key)

        n = len(state)
        for i in range(n):
            for j in range(n):
                new_state = toggle(state, i, j)
                stack.append((new_state, steps + 1))

    return -1
