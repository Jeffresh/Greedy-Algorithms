import math

class Artista:
    def __init__(self, i, j):
        self.i = i
        self.j = j

def select(candidates_set):
    #TODO implement
    pass

def objetivo(candidates_selected):
    #TODO implement
    pass

def prim(matrix, number_of_vertices):

    path = [1 for i in range(1, number_of_vertices)].insert(0,0)
    cost = [matrix[1, j] for j in range(1, number_of_vertices)].insert(0,math.inf)
    candidates_set = [i for i in range(1, number_of_vertices)]

    candidates_selected = []

    while candidates_selected.count() != 0:
        vertice = select(candidates_set)
        candidates_selected.remove(vertice)
        candidates_selected.append(path[vertice], vertice)

        for j in candidates_set:
            if matrix[vertice, j] < cost[j]:
                cost[j] = matrix=[vertice, j]
                path[j] = vertice

    return candidates_selected





