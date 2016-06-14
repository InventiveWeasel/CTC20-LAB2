import random
import itertools

def generateGraph(n,m):
    pairs = []
    #  Inicializamos o grafo com -1
    graph = [[-1 for i in range(0,n)] for j in range(0,n)]

    #Pesos aleatorios em ordem decrescente
    weights = [random.randint(1,10) for i in range(0,n*n)]
    weights.sort(reverse = True)
    print weights
    indexes = [i for i in range(0,n)]
    aux = itertools.permutations(indexes,2)
    for i in aux:
        pairs.append(i)
    random.shuffle(pairs)
    i = 0
    while i < m:
        if graph[pairs[i][0]][pairs[i][1]] == -1:
            graph[pairs[i][0]][pairs[i][1]] = weights[i]
            #  Adiciona-se tambem o simetrico
            graph[pairs[i][1]][pairs[i][0]] = weights[i]
            i = i+1
    for i in range(0,n):
        print graph[i]
    return graph
