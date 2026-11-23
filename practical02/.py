from collections import deque
import heapq

# Graph with edge costs
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 1)],
    'D': [('G', 3)],
    'E': [('G', 1)],
    'F': [('G', 2)],
    'G': []
}

# Breadth-First Search (BFS)
def bfs(start, goal):
    queue = deque([(start, [start])])
    visited = set()

    while queue:
        node, path = queue.popleft()

        if node == goal:
            return path

        if node not in visited:
            visited.add(node)
            for neighbor, cost in graph[node]:
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))
    return None


# Depth-First Search (DFS)
def dfs(start, goal):
    stack = [(start, [start])]
    visited = set()

    while stack:
        node, path = stack.pop()

        if node == goal:
            return path

        if node not in visited:
            visited.add(node)
            for neighbor, cost in graph[node]:
                if neighbor not in visited:
                    stack.append((neighbor, path + [neighbor]))
    return None


# Uniform-Cost Search (UCS)
def ucs(start, goal):
    priority_queue = [(0, start, [start])]
    visited = set()

    while priority_queue:
        cost, node, path = heapq.heappop(priority_queue)

        if node == goal:
            return path, cost

        if node not in visited:
            visited.add(node)

            for neighbor, edge_cost in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(
                        priority_queue,
                        (cost + edge_cost, neighbor, path + [neighbor])
                    )
    return None, float('inf')


start, goal = 'A', 'G'

bfs_path = bfs(start, goal)
dfs_path = dfs(start, goal)
ucs_path, ucs_cost = ucs(start, goal)

def path_cost(path):
    total = 0
    for i in range(len(path) - 1):
        for neighbor, cost in graph[path[i]]:
            if neighbor == path[i + 1]:
                total += cost
                break
    return total

print("BFS Path:", bfs_path, "Cost:", path_cost(bfs_path))
print("DFS Path:", dfs_path, "Cost:", path_cost(dfs_path))
print("UCS Path:", ucs_path, "Cost:", ucs_cost)
