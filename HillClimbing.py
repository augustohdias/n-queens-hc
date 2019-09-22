def algorithm(problem):
    current = problem.initial()
    while True:
        neighbours = problem.near_states(current)
        if not neighbours:
            break
        
        neighbour = max(neighbours, key=lambda state: problem.heuristic(state))

        if problem.heuristic(neighbour) <= problem.heuristic(current):
            break
        current = neighbour
    return current
