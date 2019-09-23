import HillClimbing 
import LocalSearch
import BoardPrintter
from NQueens import NQueens


if __name__ == "__main__":
    problem = NQueens(12)
    iterations = 1000
    
    total_trials = []
    total_time = 0

    for i in range(iterations):
        s, n, t = LocalSearch.search(problem, HillClimbing.algorithm)
        BoardPrintter.print_board(s)
        total_trials.append(n)
        total_time += t
    
    print("\nMédia de tentativas: {}\nTempo médio: {}s".format(sum(total_trials)/iterations, total_time/iterations))