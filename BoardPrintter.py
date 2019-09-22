from random import choice

def print_board(result):
    print("Resultados:\n")
    if not result:
        print([None])
        return

    for r in result:
        board = []
        for c in r:
            line = ['.'] * len(r)
            line[c] = 'Q'
            board.append(str().join(line))
        charlist = map(list, board)
        for a, b in zip(range(0, 8), charlist):
            if a % len(b) == 0:
                print("\n")
            print(" ".join(b))