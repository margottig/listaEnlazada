from nodo import Nodo

class ListaEnlazada:
    def __init__(self):
        self.head = None

    def agregarNodo(self, nuevoNodo):
        if self.head == None:
            self.head = nuevoNodo
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = nuevoNodo

    def desplegarInformacion(self):
        temp = self.head
        while temp != None:
            print("ESTO REALMENTE VINO POR ACA",temp.producto, temp.id)
            temp = temp.next
        return 'holaninjas'


