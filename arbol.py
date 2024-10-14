from nodo import * 
import copy
from producto import Producto
from auxiliar import dibujar_nodo
import time
import pygame

class Arbol:    
    #Se inicializa el arbol vacio
    def __init__(self): 
        self.raiz=None
        self.balanceo = False

    # insertar
    # Descripcion:
    # Este metodo sera utilizado para insertar cada nodo el cual se ira balanceando cuando sea necesario
    # en caso de que el producto ya existe no se creara un nuevo nodo sino que se aumentara la cantidad
    # de productos en el nodo existente (tener en cuenta que este es el metodo publico)
    # Atributos:
    # producto(Producto):es un objeto de tipo ojeto el cual sera insertado como nodo en el arbol
    def insertar(self,producto,ventana,screen_info ):
        # Se hace la verificacion que el producto no exista y si existe lo que se vera afectado sera la cantidad del producto
        n=self.buscar_nodo_nombre(producto.nombre_producto)
        # if (n):
        #     print("hola")
        #     n.producto.cantidad+=producto.cantidad
        if self.raiz == None:
            self.raiz=Nodo(producto)
        else:
            self.raiz=self._insertar(producto,self.raiz,ventana,screen_info )
            if self.balanceo:
                ventana.fill((255, 255, 255))
                dibujar_nodo(ventana,self.raiz,screen_info.current_w//2,150,120)      
                time.sleep(0.2)
                self.balanceo = False

    # _insertar
    # Descripcion:       
    # Este sera el metodo privado de insertar,el funcionamiento de este metodo fue explicado en el metodo publico
    # Parametros: 
    # producto(Producto):Es un objeto de tipo ojeto el cual sera insertado como nodo en el arbol
    # nodo(Nodo):Representaran los nodos ascendentes del nuevo nodo(gracias a la recursion)        

    def _insertar(self,producto,n,ventana,screen_info ):
        if n is None :
            temp1 = Nodo(producto) 
            return temp1 

        elif producto.id < n.producto.id:
            n.izquierda=self._insertar(producto,n.izquierda,ventana,screen_info )  
        elif  producto.id > n.producto.id: 
            n.derecha=self._insertar(producto,n.derecha,ventana,screen_info )
        if self.obtener_altura(n.derecha) == 1 : 
            ventana.fill((255, 255, 255))
            dibujar_nodo(ventana,self.raiz,screen_info.current_w//2,150,120)      
            time.sleep(1)
        # pintar
        return self.hacer_rotacion(producto,n,ventana,screen_info)

    def hacer_rotacion(self,producto,n,ventana,screen_info ) : 
        # Se actualiza la altura del nodo
        n.altura = 1 + max(self.obtener_altura(n.izquierda) , self.obtener_altura(n.derecha))
        #Se obtiene el balance del nodo
        balance=self.obtener_altura(n.izquierda) - self.obtener_altura(n.derecha)
        if balance < -1 and producto.id >= n.derecha.producto.id:  
            self.balanceo = True
            return self.rotacion_izquierda(n, ventana,screen_info)
        if balance > 1 and producto.id <= n.izquierda.producto.id: 
            self.balanceo = True
            return self.rotacion_derecha(n,ventana,screen_info)
        
        if balance > 1 and producto.id > n.izquierda.producto.id:
            n.izquierda=self.rotacion_izquierda(n.izquierda,ventana,screen_info)
            self.balanceo = True
            return self.rotacion_derecha(n)

        if balance < -1 and producto.id < n.derecha.producto.id:
            n.derecha=self.rotacion_derecha(n.derecha)
            self.balanceo = True
            return self.rotacion_izquierda(n, ventana,screen_info)  
        return n

    # Rotacion_izquierda
    # Descripcion: 
    # Hace la rotacion a la izquierda
    # Parametros:
    # n(Nodo):Representa la raiz del arbol o subarbol al cual se le aplicara la rotacion
    # Return:Retorna una rotacion simple a la izquierda al arbol o subarbol correspondiente       

    def rotacion_izquierda(self,n, ventana, screen_info):

        if n is not self.raiz:
            ventana.fill((255, 255, 255))
            dibujar_nodo(ventana,n,screen_info.current_w//2,150,120)      
            time.sleep(1)   
        z=n.derecha
        t=z.izquierda
        #Aqui se hacen la rotaciones 
        z.izquierda=n
        n.derecha=t
        #Actualizamos las alturas de n y z porque con esta rotacion son las que se ven afectadas
        n.altura=1 + max(self.obtener_altura(n.izquierda),self.obtener_altura(n.derecha))
        z.altura=1 + max(self.obtener_altura(z.izquierda),self.obtener_altura(z.derecha))
        if n is not self.raiz:
            ventana.fill((255, 255, 255))
            dibujar_nodo(ventana,z,screen_info.current_w//2,150,120)      
            time.sleep(1)
        return z

    # Rotacion_derecha
    # Descripcion: 
    # Hace la rotacion a la derecha
    # Parametros:
    # n(Nodo):Representa la raiz del arbol o subarbol al cual se le aplicara la rotacion
    # Return:Retorna una rotacion simple a la derecha al arbol o subarbol correspondiente        

    def rotacion_derecha(self,n):
        z=n.izquierda
        t=z.derecha
        #Aqui se hacen la rotaciones 
        z.derecha=n
        n.izquierda=t
        #Actualizamos las alturas de n y z porque con esta rotacion son las que se ven afectadas
        n.altura=1 + max(self.obtener_altura(n.izquierda),self.obtener_altura(n.derecha))
        z.altura=1 + max(self.obtener_altura(z.izquierda),self.obtener_altura(z.derecha))
        if n is not self.raiz:
            ventana.fill((255, 255, 255))
            dibujar_nodo(ventana,z,screen_info.current_w//2,150,120)      
            time.sleep(1)
        return z
        
    # obtener_altura()
    # Descripcion:    
    # Este metodo devuelve la altura del arbol o subarbol en caso de que no exista retornara 0 ya que si no se hace esto despues puede generar error
    # Parametros:
    # n(Nodo o none):Representara el nodo el cual queremos calcular su altura o en dado caso sera None porque no existe el nodo
    # Return: Retornara la altura del arbol o subarbol cuya raiz es n          
    def obtener_altura(self,n):
        if n is None:
            return 0
        return n.altura    

    # buscar_nodo_nombre
    # Descripcion    
    # Se utiliza esta funcion para buscar un nodo en especifico por el nombre

    def buscar_nodo_nombre(self,nombre_nodo):
        nodos=[]
        self._buscar_nodo_nombre(nombre_nodo,self.raiz,nodos)
        if len(nodos)==1:
            return nodos[0]
        return None   

    def _buscar_nodo_nombre(self,nombre_producto,n,nodos):
        if n is None:
            return
        if nombre_producto == n.producto.nombre_producto:
            return nodos.append(n)
        self._buscar_nodo_nombre(nombre_producto,n.izquierda,nodos)
        self._buscar_nodo_nombre(nombre_producto,n.derecha,nodos)


    # Descripcion:Esta funcion recorrera el arbol en un algoritmo de busqueda en profundidad,
    # pero tiene la particularidad de que puede recorrer en inorder los subarboles del mismo.
    # Parametros:
    # n(Nodo):La raiz del arbol que recorera
    # Return:Devuelve una lista de Nodos 

    def inorder(self,n):
        nodos=[]
        self._inorder(n,nodos)
        return nodos

    #_inorder
    # Descripcion: Es el algoritmo privado de inoder y es el encargardo de guardar en la lista los nodos correspondientes
    # Parametros:
    # n(Nodo):La raiz del arbol que recorera
    # nodos([]):La lista donde se almacenaran los nodos
    # return:No retornara nada en especifico

    def _inorder(self,n,nodos):
        if n is None :
            return 
        self._inorder(n.izquierda,nodos)
        nodos.append(n)
        self._inorder(n.derecha,nodos)
        
    # buscar_nodo_padre
    # Descripcion:Es el metodo privado de buscar_nodo_padre el cual nos sirve para buscar el nodo padre de un nodo,
    # en caso de que sea la raiz devolvera la raiz.abs
    # Parametros:
    # id(int):el id del nodo al cual le buscaremos el padre

    def buscar_nodo_por_id(self,id):
        nodo = self._buscar_nodo_por_id(self.raiz,id)
        if nodo:
            return nodo
        return None
        
    # _buscar_nodo_por_id
    # Descripcion:Este el metodo privado de buscar_nodo_padre y es el encargado de hacer la recursion de este metodo
    # Parametros:
    # n(nodo):La raiz del arbol
    # id(int):id del nodo que buscaremos       

    def _buscar_nodo_por_id(self,n,id):
        if n is None:
            return None
        if  n.producto.id == id:
            return n
        if  n.producto.id < id:
            return self._buscar_nodo_por_id(n.derecha,id)
        if  n.producto.id > id:
            return self._buscar_nodo_por_id(n.izquierda,id)  


    def aux(self,n,ventana,screen_info):
        altura_n=self.obtener_altura(n)
        if altura_n == 1:
            return None
        if altura_n == 2:
            if n.izquierda is None:
                z= n.derecha
            else:
                z=n.izquierda
                z.derecha=n.derecha
        else:
            sub_arbol_ni=self.inorder(n.izquierda)
            z=sub_arbol_ni[len(sub_arbol_ni)-1]
            self.eliminar_nodo(z.producto.id,0,ventana,screen_info)
            z.izquierda=n.izquierda 
            z.derecha=n.derecha
           
           
        z.altura= 1 + max(self.obtener_altura(z.izquierda),self.obtener_altura(z.derecha))
        return z
    def eliminar_nodo(self,id,boolean,ventana,screen_info):
        if boolean:
            ventana.fill((255, 255, 255))
            dibujar_nodo(ventana,self.raiz,screen_info.current_w//2,150,120)      
            time.sleep(1) 
        self.raiz=self._eliminar_nodo(self.raiz,id,boolean,ventana,screen_info)
        #and self.balanceo   modificacion pero se mostrara en dos veces el mismo arbol
        if boolean :
            ventana.fill((255, 255, 255))
            dibujar_nodo(ventana,self.raiz,screen_info.current_w//2,150,120)      
            time.sleep(1.5)
            arbol.balanceo=False
        

    def _eliminar_nodo(self,n,id,boolean,ventana,screen_info):
        if n is None:
            return
        if n.producto.id == id:
            n=self.aux(n,ventana,screen_info)
            
        elif id > n.producto.id:
            n.derecha=self._eliminar_nodo(n.derecha,id,boolean,ventana,screen_info)              
        elif id < n.producto.id:
            n.izquierda=self._eliminar_nodo(n.izquierda,id,boolean,ventana,screen_info)  
           
        if n:
            n.altura= 1 + max(self.obtener_altura(n.izquierda),self.obtener_altura(n.derecha))
            if boolean:
                if n.derecha and n.izquierda:
                    if id == n.derecha.producto.id or id == n.izquierda.producto.id:
                        ventana.fill((255, 255, 255))
                        dibujar_nodo(ventana,n,screen_info.current_w//2,150,120)      
                        time.sleep(1.5)
                elif n.izquierda:
                    if id == n.izquierda.producto.id:
                        
                        ventana.fill((255, 255, 255))
                        dibujar_nodo(ventana,n,screen_info.current_w//2,150,120)      
                        time.sleep(1.5)
                elif n.derecha:
                    if id == n.derecha.producto.id:
                        ventana.fill((255, 255, 255))
                        dibujar_nodo(ventana,n,screen_info.current_w//2,150,120)      
                        time.sleep(1.5)
                return self.aux2(n,ventana,screen_info) 
            
        return n       
    def aux2 (self,n,ventana,screen_info):
        if self.obtener_altura(n)==1:
            return n
        if self.obtener_altura(n.izquierda) >= self.obtener_altura(n.derecha):
            nodos_izquierda=self.inorder(n.izquierda)
            nodo=nodos_izquierda[len(nodos_izquierda)-1]
        elif self.obtener_altura(n.izquierda) < self.obtener_altura(n.derecha):
            nodos_derecha=self.inorder(n.derecha)
            nodo=nodos_derecha[len(nodos_derecha)-1]
        return self.hacer_rotacion(nodo.producto,n,ventana,screen_info)

    def  actualizar_atributos(self,nodo,cantidad,precio):
        nodo.producto.cantidad=cantidad           
        nodo.producto.precio=precio     


    
arbol=Arbol()

# producto1=Producto(1,"gelatina",1200,"comida")
# producto2=Producto(1,"gelatina",1200,"comida")
# producto3=Producto(1,"gelatina",1200,"comida")
# producto4=Producto(1,"gelatina",1200,"comida")
# producto5=Producto(1,"gelatina",1200,"comida")
# producto6=Producto(1,"gelatina",1200,"comida")
# producto7=Producto(1,"gelatina",1200,"comida")

# arbol.insertar(producto1)   
# arbol.insertar(producto2)   
# arbol.insertar(producto3)   
# arbol.insertar(producto4)   
# arbol.insertar(producto5)   
# arbol.insertar(producto6)   
# arbol.insertar(producto7) 

# print(arbol.raiz.producto.id,"soy raiz ")
# arbol.eliminar_nodo(2,1)
# print(arbol.raiz.producto.id,"soy raiz ")
# arbol.inorder(arbol.raiz)
# nodos=arbol.filtrar_precio(1000,1300)
# for m in nodos:
#     print(m)
# n=arbol.buscar_nodo_nombre("gelatina")[0]
# arbol.raiz=Nodo(producto6)
# print(arbol.buscar_nodo_padre(5).producto.nombre_producto)



