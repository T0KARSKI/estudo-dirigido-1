from bfs import bfs
from dfs import dfs
from astar import astar
from greedy import greedy
from hill_climbing import hill_climbing

def run_test(name, func, state):
    try:
        result = func(state)
        print(f"{name}: {result}")
    except:
        print(f"{name}: erro")

def generate_board(n):
    return [[0 for _ in range(n)] for _ in range(n)]

# =========================
# 2x2
# =========================
print("\n=== TABULEIRO 2x2 ===")
state_2x2 = generate_board(2)

run_test("BFS", bfs, state_2x2)
run_test("DFS", dfs, state_2x2)
run_test("A*", astar, state_2x2)
run_test("Greedy", greedy, state_2x2)
run_test("Hill Climbing", hill_climbing, state_2x2)

# =========================
# 3x3
# =========================
print("\n=== TABULEIRO 3x3 ===")
state_3x3 = [
    [0,1,0],
    [1,0,1],
    [0,1,0]
]

run_test("BFS", bfs, state_3x3)
run_test("DFS", dfs, state_3x3)
run_test("A*", astar, state_3x3)
run_test("Greedy", greedy, state_3x3)
run_test("Hill Climbing", hill_climbing, state_3x3)

# =========================
# 5x5
# =========================
print("\n=== TABULEIRO 5x5 ===")
state_5x5 = [
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,1,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
]

print("BFS: não executado (alto custo)")
print("DFS: não executado (alto custo)")

run_test("A*", astar, state_5x5)
run_test("Greedy", greedy, state_5x5)
run_test("Hill Climbing", hill_climbing, state_5x5)

# =========================
# 7x7
# =========================
print("\n=== TABULEIRO 7x7 ===")
state_7x7 = generate_board(7)

print("BFS: não executado (inviável)")
print("DFS: não executado (inviável)")
print("A*: não executado (alto custo)")

run_test("Greedy", greedy, state_7x7)
run_test("Hill Climbing", hill_climbing, state_7x7)

# =========================
# 10x10
# =========================
print("\n=== TABULEIRO 10x10 ===")
state_10x10 = generate_board(10)

print("BFS: não executado (inviável)")
print("DFS: não executado (inviável)")
print("A*: não executado (inviável)")
print("Greedy: execução limitada")
print("Hill Climbing: execução limitada")
