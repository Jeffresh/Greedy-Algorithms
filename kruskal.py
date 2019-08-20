class Aristas:
    def __init__(self, i=0, j=0):
        self.i = i
        self.j = j

def partition(number_of_vertices):
    #TODO implement
    pass

def sort(candidates_set):
    #TODO implement
    pass

def select(candidates_set):
    #TODO implement
    pass

def search(p, number_of_vertices, vertex):
    #TODO implement
    pass

def fusion(candidates_selected):
    #TODO implement
    pass

def objetivo(candidates_selected):
    #TODO implement
    pass

def Kruskal(vertices,aristas):
    candidates_set = aristas
    candidates_selected=[]
    number_of_vertices = vertices.count()
    p = partition(number_of_vertices)
    sort(candidates_selected)

    while candidates_selected.count() != number_of_vertices - 1:
        arista_seleccionada = select(candidates_set)
        candidates_set.remove(arista_seleccionada)
        p1 = search(p,number_of_vertices, arista_seleccionada.i)
        p2 = search(p , number_of_vertices, arista_seleccionada.j)

        if p1 != p2:
            fusion(p,number_of_vertices,p1,p2)
            candidates_selected.append(arista_seleccionada)
