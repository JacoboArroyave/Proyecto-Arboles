
import random
# En esta clase definimos los atributos de producto donde producto sera un atributo de la clase nodo
class Producto:
    contador_id=1
    def __init__(self,cantidad,nombre_producto,precio,categoria_producto, id=-1):
        if id!=-1:
            Producto.contador_id=id
       
        self.id=Producto.contador_id
        self.cantidad = cantidad
        self.nombre_producto = nombre_producto
        self.precio = precio
        self.categoria_producto = categoria_producto
        Producto.contador_id+=1
