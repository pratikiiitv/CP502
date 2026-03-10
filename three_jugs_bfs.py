from collections import deque

def is_valid(state):
    jug1, jug2, jug3 = state
    if FIXME
        return False
    return True

def get_successors(state):
    successors = []
    jug1, jug2, jug3 = state
    
        moves = [FIXME]
        for move in moves:
            new_state = FIXME
            if is_valid(new_state):
                successors.append(new_state)
    else:
        moves = [FIXME]
        for move in moves:
            new_state = FIXME
            if is_valid(new_state):
                successors.append(new_state)
    return successors

def bfs(start_state, goal_state):
    queue = deque([(start_state, [])])
    visited = set()
    while queue:
        (state, path) = queue.pop()
        if state in visited:
            continue
        visited.add(state)
        path = path + [state]
        if check_goal_state(state):
            return path
        for successor in get_successors(state):
            queue.append((successor, path))
    return None

start_state = (8, 0, 0)
goal_state = FIXME

solution = bfs(start_state, goal_state)
if solution:
    print("Solution found:")
    for step in solution:
        print(step)
else:
    print("No solution found.")
