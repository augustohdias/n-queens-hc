def algorithm(problem):
    current = problem.initial()
    while True:
        neighbours = problem.neighbours(current)
        
        if not neighbours:
            break
        
        neighbour = min(neighbours, key=lambda state: problem.heuristic(state))

        if problem.heuristic(neighbour) >= problem.heuristic(current):
            break
        current = neighbour
    return current
