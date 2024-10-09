
import random
# En esta clase definimos los atributos de producto donde producto sera un atributo de la clase nodo
class Producto:
    contador_id=1
    def __init__(self,cantidad,nombre_producto,precio,categoria_producto):
        self.id=Producto.contador_id
        Producto.contador_id+=1
        self.cantidad = cantidad
        self.nombre_producto = nombre_producto
        self.precio = precio
        self.categoria_producto = categoria_producto

    def generar_id():
        return int(uuid.uuid4()) 
    
    def mostrar_productos(self):
        return (self.id)    
 
    
