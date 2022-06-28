from tempfile import tempdir
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


    def buscarNodo(self, id):        
        temp = self.head
        while temp != None:
            if temp.getId() == id:
                return temp
            temp = temp.next
            print("BuscarNodo", temp)
        return None
    
    def longitudListaEnlazada(self):
        temp = self.head
        contador = 0
        while temp != None:
            contador += 1
            temp = temp.next
        return contador


