from time import time

def search(problem, algorithm, i):
    n_iterations = i
    cnt = 0
    start = time()
    s = []
    for i in range(n_iterations):
        result = algorithm(problem)
        if problem.heuristic(result) is 0:
            cnt += 1
            s.append(result)
    print("Soluções/Tentativas: %2d/%d\nTempo de execução: %f" % (cnt, n_iterations, time() - start))
    return s 