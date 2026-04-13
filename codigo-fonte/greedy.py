from utils import toggle, is_goal

def heuristic(state):
    return sum(cell == 0 for row in state for cell in row)

def greedy(initial):
    state = initial
    steps = 0

    for _ in range(100):  # limite
        if is_goal(state):
            return steps

        best_state = None
        best_h = float('inf')

        n = len(state)
        for i in range(n):
            for j in range(n):
                new_state = toggle(state, i, j)
                h = heuristic(new_state)

                if h < best_h:
                    best_h = h
                    best_state = new_state

        if best_state is None:
            break

        state = best_state
        steps += 1

    return -1
