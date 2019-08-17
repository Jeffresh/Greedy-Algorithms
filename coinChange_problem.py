class Monedas:

    def __init__(self, cantidad=0, valor=0):
        self.cantidad = cantidad
        self.valor = valor

def select(candidate_set):
    # TODO: Implement this method
    pass

def coinChange(conjunto_monedas, cambio):
    candidates_set = conjunto_monedas
    candidates_selected = []
    c = cambio
    candidate_selected = None

    while c!=0 and candidates_set:
        candidate = select(candidate_selected)

        # TODO: keep going




