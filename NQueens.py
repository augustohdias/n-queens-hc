from random import choice
from collections import Counter
from random import randrange
from BoardPrintter import print_board

class NQueens():
    def __init__(self, N):
        self.N = N

    # Estado inicial:
    #   Retorna o estado inicial a partir do size
    def initial(self):
        return list(randrange(self.N) for i in range(self.N))

    # Heuristica: h
    #   Número de pares de rainhas se atacando
    def heuristic(self, state):

        # Define a, b, c como contadores
        a, b, c = [Counter() for i in range(3)]
        
        for row, col in enumerate(state):
            a[col] += 1
            b[row - col] += 1
            c[abs(row + col)] += 1
        
        # Percorre as os mapas (a, b, c) incrementando o valor de ataques
        # Divide para retirar contagens dobradas
        h = 0
        for counter in [a, b, c]:
            for key in counter:
                h += int(counter[key] * (counter[key] - 1) / 2)
        
        # print("\nNúmero de ataques: {}".format(h))
        # print_board([state])
        
        return h

    # Retorna todos os estados acessiveis a partir do estado atual. 
    # As peças movem-se apenas entre colunas, logo nunca haverá duas peças na mesma linha.
    def neighbours(self, state):
        neighborhood = []
        # Para cada state[row] verfica se as colunas vizinhas estão vazias.
        for row in range(self.N):
            for col in range(self.N):
                # Se for diferente:
                #   A coluna atual está disponivel para movimentar-se.
                if col != state[row]:
                    aux = list(state)
                    aux[row] = col  # Troca a coluna para a vazia.
                    neighborhood.append(list(aux))  # Inclui na lista neighborhood.
        return neighborhood
