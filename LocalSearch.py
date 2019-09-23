from time import time

def search(problem, algorithm):
    n = 0
    start = time()
    s = []
    while True:
        n += 1 
        result = algorithm(problem)
        if problem.heuristic(result) is 0:
            s.append(result)
            break
    t = time() - start
    print("\nTentativas Totais: {}\nTempo de execução: {}".format(n, t))
    return s, n, t