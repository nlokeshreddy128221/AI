import heapq

goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)

start = (1, 2, 3,
         4, 0, 6,
         7, 5, 8)

# Heuristic 1: Misplaced tiles
def misplaced(state):
    return sum(
        1 for i in range(9)
        if state[i] != 0 and state[i] != goal[i]
    )

# Heuristic 2: Manhattan distance
def manhattan(state):
    distance = 0
    for i, tile in enumerate(state):
        if tile != 0:
            target = goal.index(tile)
            distance += abs(i // 3 - target // 3)
            distance += abs(i % 3 - target % 3)
    return distance

# Generate possible next states
def neighbors(state):
    zero = state.index(0)
    row, col = zero // 3, zero % 3
    result = []

    for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        r, c = row + dr, col + dc

        if 0 <= r < 3 and 0 <= c < 3:
            j = r * 3 + c
            new_state = list(state)
            new_state[zero], new_state[j] = new_state[j], new_state[zero]
            result.append(tuple(new_state))

    return result

# A* search
def astar(start, heuristic):
    pq = [(heuristic(start), 0, start)]
    parent = {start: None}
    cost = {start: 0}
    expanded = 0

    while pq:
        f, g, state = heapq.heappop(pq)

        if g != cost[state]:
            continue

        expanded += 1

        if state == goal:
            path = []
            while state is not None:
                path.append(state)
                state = parent[state]
            return path[::-1], expanded

        for nxt in neighbors(state):
            new_g = g + 1

            if new_g < cost.get(nxt, float('inf')):
                cost[nxt] = new_g
                parent[nxt] = state
                heapq.heappush(
                    pq, (new_g + heuristic(nxt), new_g, nxt)
                )

    return None, expanded

# Compare heuristics
for name, heuristic in [
    ("Misplaced Tiles", misplaced),
    ("Manhattan Distance", manhattan)
]:
    path, expanded = astar(start, heuristic)

    print("\nHeuristic:", name)
    print("Moves required:", len(path) - 1)
    print("States expanded:", expanded)

    print("Solution:")
    for state in path:
        print(state[0:3])
        print(state[3:6])
        print(state[6:9])
        print()
