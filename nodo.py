from producto import Producto

#Se crea el nodo el cual tiene un atributo Producto
class Nodo:
    def __init__(self,producto):
        self.producto=producto
        self.izquierda=None
        self.derecha=None
        self.altura=1
 