import itertools
import GraphGenerator

n = 6
m = 10
graph = GraphGenerator.generateGraph(n,m)

#  O vertice de partida sera sempre o numero 1 (indice 0)
indexes = [i for i in range(1,n)]
auxPaths = itertools.permutations(indexes, n-1)

#  Gerando todos os caminhos possiveis
paths = []
for i in auxPaths:
    paths.append([0] + list(i) + [0])

#  Percorrendo todos os caminhos possiveis
minCost = 0
minCostPath = 0
existeCaminho = False
for p in paths:
    auxCost = 0
    for step in range(0,n):
        i = p[step]
        j = p[step+1]
        if graph[i][j] == -1:
            break
        auxCost = auxCost + graph[i][j]
        #  Quando encontramos um caminho valido, o armazenamos e calculamos o seu custo
        if p[j] == p[0]:
            existeCaminho = True
            if (minCost == 0 or minCost > auxCost):
                minCost = auxCost
                minCostPath = p

#  Printando o resultado
if existeCaminho:
    print "O caminho desejado eh:"
    print minCostPath
    print "O custo minimo associado eh:"
    print minCost
else:
    print "Nao existe caminho minimo"


