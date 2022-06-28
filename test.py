# from listaEnlazada.nodo import Nodo
from nodo import Nodo
from lista_enlazada import ListaEnlazada

listaEnlazada = ListaEnlazada()

producto1 = Nodo("bicicleta", 123)
producto3 = Nodo("radio", 111)
producto4 = Nodo("consola", 131)


listaEnlazada.agregarNodo(producto1)
listaEnlazada.agregarNodo(producto3)
listaEnlazada.agregarNodo(producto4)

print(listaEnlazada.desplegarInformacion())

listaEnlazada.buscarNodo(1)
print(listaEnlazada.longitudListaEnlazada())