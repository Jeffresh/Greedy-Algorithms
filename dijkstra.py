import math


def select(candidates_set, cost):
    r = math.inf
    vertex_selected = None

    for vertex in candidates_set:
        if cost[vertex] < r:
            r = cost[vertex]
            vertex_selected = vertex

    return vertex_selected


def dijkstra(cost_matrix, number_of_vertices, initial_vertex):
    candidate_set = []
    cost = [0]*number_of_vertices-1
    path = [0]*number_of_vertices-1

    for i in range(0,number_of_vertices):
        candidate_set.append(i)
        cost[i] = cost_matrix[initial_vertex, i]
        path[i] = initial_vertex

    candidate_set.remove(initial_vertex)

    while candidate_set.count() != 0:

        k = select(candidate_set, cost)
        candidate_set.remove(k)

        for vertex in candidate_set:
            if cost[k] + cost_matrix[k, vertex] < cost[vertex]:
                cost[vertex] = cost[k] + cost_matrix[k, vertex]
                path[vertex] = k


