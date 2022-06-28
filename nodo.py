class Nodo:
    def __init__(self, producto, id):
        self.producto = producto
        self.id = id
        self.next = None

    def getId(self):
        return self.id
