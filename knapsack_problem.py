import math


class Objeto:

    def __init__(self, nombre='diamante', valor=0.0, peso=0.0):
        self.nombre = nombre
        self.valor = valor
        self.peso = peso

    def __str__(self):
        return 'Nombre: {}\nValor: {} $ \nPeso: {} kg\n'.format(self.nombre, self.valor, self.peso)


def select(candidates_set):
    limit = -math.inf
    best_candidate = None

    for candidate in candidates_set:
        if candidate.valor/candidate.peso > limit:
            best_candidate = candidate
            limit = candidate.valor/candidate.peso

    return best_candidate

def objetivo(mochila):

    valor_total = 0

    for objeto in mochila:
        valor_total +=  objeto.valor

    return valor_total


def knapsack_problem(objetos, capacidad):
    candidates_set = objetos[:]
    candidates_selected = []

    while capacidad != 0 and candidates_set:
        candidato = select(candidates_set)
        candidates_set.remove(candidato)

        if candidato.peso <= capacidad:
            capacidad = capacidad-candidato.peso
            candidates_selected.append(candidato)
        else:
            candidato.peso = capacidad
            candidato.valor = candidato.valor * capacidad / candidato.peso
            candidates_selected.append(candidato)
            capacidad = 0

    return candidates_selected

if __name__ == "__main__":

    capacidad = 10.0
    lapiz = Objeto('lapiz', 0.3, 0.1)
    reloj = Objeto('Reloj', 1000000, 0.02)
    radio = Objeto('radio', 150.0, 3.0)
    joyas = Objeto('joyas', 20000.0, 13)
    diamantes = Objeto('Diamantes', 200000.0, 10.4)
    cartas = Objeto ('Cartas', 100000.0, 0.50)
    ordenador = Objeto('PC', 2000.0, 15.0)
    laptop = Objeto('laptop', 3000.0, 5.0)
    escritorio = Objeto('Escritorio', 1000.0, 20.0)

    objetos = [diamantes,lapiz,radio,joyas,ordenador,laptop,escritorio, cartas, reloj]

    mochila = knapsack_problem(objetos, capacidad)

    for objetos in mochila:
        print(objetos)

    print("Valor total: ", objetivo(mochila),"$")

