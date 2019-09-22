import HillClimbing 
import LocalSearch
import BoardPrintter
from NQueens import NQueens


if __name__ == "__main__":
    # Inicia o problema passando o tamanho do tabuleiro
    problem = NQueens(8)
    board = LocalSearch.search(problem, HillClimbing.algorithm, 100)
    # BoardPrintter.print_board(board)
    BoardPrintter.print_board(board)