import math


class Monedas:

    def __init__(self, valor=0, cantidad=0):
        self.cantidad = cantidad
        self.valor = valor

    def __str__(self):
        return '{} Monedas de {} euro\n'.format(self.cantidad, self.valor)


def objetivo(monedas):
    suma = 0
    for moneda in monedas:
        suma += moneda.cantidad

    return suma


def select(candidate_set):
    candidate_selected = None
    limit = -math.inf

    for candidate in candidate_set:
        if limit < candidate.valor:
            candidate_selected = candidate
            limit = candidate.valor

    return candidate_selected


def coinChange(conjunto_monedas, cambio):
    candidates_set = conjunto_monedas[:]
    candidates_selected = []
    c = cambio
    candidate_selected = None

    while c != 0 and candidates_set:

        candidate = select(candidates_set)
        candidates_set.remove(candidate)
        candidate.cantidad = min(candidate.cantidad, c // candidate.valor)
        if candidate.cantidad > 0:
            candidates_selected.append(candidate)
            c = c - candidate.valor * candidate.cantidad

    return candidates_selected


if __name__ == "__main__":
    monedas = [Monedas(1,100), Monedas(5,100), Monedas(10,100), Monedas(15,100), Monedas(25,100), Monedas(50,100),
               Monedas(100,100), Monedas(200,100), Monedas(500,100)]


    cambio = coinChange(monedas, 467)

    for monedas in cambio:
        print(monedas)

    print("El número de monedas es: ", objetivo(cambio) )