def algorithm(problem):
    current = problem.initial()
    while True:
        neighbours = problem.neighbours(current)
        
        if not neighbours:
            break
        
        neighbour = min(neighbours, key=lambda state: problem.heuristic(state))

        print("\n\nEstado vizinho:")
        n = problem.heuristic(neighbour)
        print("\n\nEstado corrente:")
        c = problem.heuristic(current)
        if n >= c:
            break
        current = neighbour
    return current
