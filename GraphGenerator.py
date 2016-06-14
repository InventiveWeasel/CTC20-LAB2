import random


def generateGraph(n,m):
    graph = [[random.randint(1,10) for i in range(0,n)] for j in range(0,n)]
    #  Selecionamos os de maior valor
    return graph



print generateGraph(5)