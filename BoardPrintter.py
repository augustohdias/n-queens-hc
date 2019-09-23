from random import choice

def print_board(result):
    print("Estado:")
    if not result:
        print([None])
        return

    for r in result:
        board = []
        for c in r:
            line = ['#'] * len(r)
            line[c] = 'Q'
            board.append(str().join(line))
        charlist = map(list, board)
        for e in charlist:
            print(" ".join(e))