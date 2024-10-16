import pygame, time, json
from producto import Producto
#dibujar_nodo
#Descripcion:Esta funcion es la funcion recursiva de dibiujar el arbol, se diferencia de la otra que se muestra "paso por paso"
#Parametros:
# ventana(es la ventana donde se esta mostrando todo la parte visual) 
#x,y(Las poscicion donde se dibujara el circulo y hace referencia a el centro del circulo)
#espacio(Es el espacio que se dejarfa entre el nodo padre y los hijos)
#color(es por defecto un especie de azul y indicara el color del nodo, cuando el producrto tenga stock 0 se pintara de otro color)
def dibujar_nodo(ventana, nodo, x, y, espacio, color=(0, 128, 255)):
    if nodo:
        # Dibujar líneas entre nodos
        if nodo.izquierda:
            pygame.draw.line(ventana, (0,0,0), (x, y), (x - espacio, y + 50), 2)
        if nodo.derecha:
            pygame.draw.line(ventana, (0,0,0), (x, y), (x + espacio, y + 50), 2)

        # Dibujar nodo
        dibujar(ventana,nodo,x,y,espacio,color)
        pygame.display.update()
        dibujar_nodo(ventana, nodo.izquierda, x - espacio, y + 50, espacio // 2, color)
        dibujar_nodo(ventana, nodo.derecha, x + espacio, y + 50, espacio // 2, color)
        dibujar(ventana,nodo,x,y,espacio,color)
        pygame.display.update()
#dibuja
#decripcion:Este es el encargado de pintar la apariencia del nodo
#Parametros:
# ventana(es la ventana donde se esta mostrando todo la parte visual) 
#nodo(el nodo que se pintara)
#x,y(Las poscicion donde se dibujara el circulo y hace referencia a el centro del circulo)
#espacio(Es el espacio que se dejarfa entre el nodo padre y los hijos)
#color(es por defecto un especie de azul y indicara el color del nodo, cuando el producrto tenga stock 0 se pintara de otro color)
#borde(es por defecto un especie de rojo y indicara el borde del nodo)
    
def dibujar(ventana, nodo, x, y, espacio, color, borde=(0,0,0)):
    font = pygame.font.Font(None, 32)
    if nodo.producto.cantidad == 0:
        pygame.draw.circle(ventana, (70, 75, 57), (x, y), 20)
    else:   
        pygame.draw.circle(ventana, (0, 128, 255), (x, y), 20)
    pygame.draw.circle(ventana, borde, (x, y), 20, 2)
    texto = font.render(str(nodo.producto.id), True, (255, 255, 255))
    ventana.blit(texto, (x -6 , y - 10))
    pygame.display.update()
    time.sleep(0.2)
        
#dijar_animacion_buscar_id
#Descripcion:Esta funcion busca un solo id
# ventana(es la ventana donde se esta mostrando todo la parte visual) 
#nodo(el nodo que se pintara)
#x,y(Las poscicion donde se dibujara el circulo y hace referencia a el centro del circulo)
#espacio(Es el espacio que se dejarfa entre el nodo padre y los hijos)
#font(hace referencia a la fuente)
#id(El id el cual sera buscado)
def dibujar_animacion_buscar_id(ventana,nodo,x,y,espacio,font,id):
    if nodo:
        pygame.draw.circle(ventana,(255,0,0),(x,y),20,2)
        pygame.display.update()
        time.sleep(1)
        

        if nodo.producto.id == id :
            ventana.blit(font.render(f'Nodo encontrado con el id {id}' ,True,(0,0,0)),(30,30))
            pygame.display.update()
            time.sleep(1)
            return
            
        pygame.draw.circle(ventana,(0,0,0),(x,y),20,2)
        pygame.display.update()

        if id > nodo.producto.id:
           return dibujar_animacion_buscar_id(ventana,nodo.derecha,x + espacio, y+50 ,espacio//2,font,id)
        else:
            return dibujar_animacion_buscar_id(ventana,nodo.izquierda,x - espacio, y+50, espacio//2,font,id)
    return False

#dibujar_animacion_filtrar_combinada
#Descripcion:esta funcion buscara los productos que cumplan con ciertos criterios
# Parametros:
# ventana(es la ventana donde se esta mostrando todo la parte visual) 
#nodo(el nodo que se pintara)
#x,y(Las poscicion donde se dibujara el circulo y hace referencia a el centro del circulo)
#espacio(Es el espacio que se dejarfa entre el nodo padre y los hijos)
#font(hace referencia a la fuente)
#categoria,cantidad,precio_min,precio_max(Estos son los criterios por los que filtrara)
#raiz(Es la raiz del arbol y empazara e indica pro donde empezara el recorrido)

def dibujar_animacion_filtrar_combinada(ventana,nodo,x,y,espacio,font,categoria,cantidad,precio_min,precio_max,raiz):
        pygame.draw.circle(ventana,(255,0,0),(x,y),20,2)
        pygame.display.update()
        time.sleep(1)
        y_texto=30
        font_texto = pygame.font.Font(None, 25)
        if validar_precio(nodo,precio_min,precio_max) and validar_categoria(nodo,categoria) and validar_cantidad(nodo,cantidad):
            if validar_precio(nodo,precio_min,precio_max):
                if precio_min != "":
                    ventana.blit(font_texto.render(f'Nodo encontrado con un precio mayor que {precio_min} y un precio menor que {precio_max}' ,True,(0,0,0)),(30,y_texto))
                y_texto+=30
            if validar_categoria(nodo,categoria):
                if categoria !=:
                    ventana.blit(font_texto.render(f'Nodo encontrado con una categoria {categoria}' ,True,(0,0,0)),(30,y_texto))
                y_texto+=30
            if validar_cantidad(nodo,cantidad):
                if cantidad != ""
                    ventana.blit(font_texto.render(f'Nodo encontrado con una cantidad {cantidad}' ,True,(0,0,0)),(30,y_texto))
                y_texto+=30
            pygame.display.update()
            time.sleep(3)
            ventana.fill((255,255,255))
            pintar_cuadro_informacion(ventana,font,nodo)
            pygame.display.update()
            time.sleep(5)
            ventana.fill((255,255,255))
            dibujar_nodo_main(ventana, raiz, (683), 150, 120,font)
            pygame.display.update()
            
        pygame.draw.circle(ventana,(0,0,0),(x,y),20,2)
        pygame.display.update()

        if  nodo.izquierda:
            dibujar_animacion_filtrar_combinada(ventana,nodo.izquierda,x - espacio, y+50 ,espacio//2,font,categoria,cantidad,precio_min,precio_max,raiz)
        if nodo.derecha:
            dibujar_animacion_filtrar_combinada(ventana,nodo.derecha,x + espacio, y+50, espacio//2,font,categoria,cantidad,precio_min,precio_max,raiz)
    
#validar_precio
#desciprcion:Este metodo validara que validar precio sea uno de los criterios 
# para filtrar por varios atributos y tambien validara que se cumpla la condicion
#Parametros:
#nodo(Es aquel que se le verificara la condicion)
#precio_min,precio_max(son las condiciones a validar)

def validar_precio(nodo,precio_min,precio_max):
    if precio_min != "" and precio_max !="":
        return int(precio_min) <= nodo.producto.precio <= int(precio_max)   
    return True   
#validar_categoria
#desciprcion:Este metodo validara que validar categoria sea uno de los criterios 
# para filtrar por varios atributos y tambien validara que se cumpla la condicion
#Parametros:
#nodo(Es aquel que se le verificara la condicion)
#categoria(son las condiciones a validar)

def validar_categoria(nodo,categoria):
    if categoria !="":
        return categoria == nodo.producto.categoria_producto   
    return True

#validar_cantidad
#desciprcion:Este metodo validara que validar cantidad sea uno de los criterios 
# para filtrar por varios atributos y tambien validara que se cumpla la condicion
#Parametros:
#nodo(Es aquel que se le verificara la condicion)
#cantidad(son las condiciones a validar)
   
def validar_cantidad(nodo,cantidad):
    if cantidad !="":
        return int(cantidad) == nodo.producto.cantidad   
    return True   


#dibujar_animacion_filtrar
#Descripcion:esta funcion buscara los productos que cumplan con ciertos criterios,filtrara popr precio o por categoria
# Parametros:
# ventana(es la ventana donde se esta mostrando todo la parte visual) 
#nodo(el nodo que se pintara)
#x,y(Las poscicion donde se dibujara el circulo y hace referencia a el centro del circulo)
#espacio(Es el espacio que se dejarfa entre el nodo padre y los hijos)
#font(hace referencia a la fuente)
#raiz(Es la raiz del arbol y empazara e indica pro donde empezara el recorrido)
#categoria,precio_min,precio_max(Estos son los criterios por los que filtrara)

def dibujar_animacion_filtrar(ventana,nodo,x,y,espacio,font,raiz,precio_min,precio_max,categoria):
    
    pygame.draw.circle(ventana,(255,0,0),(x,y),20,2)
    pygame.display.update()
    time.sleep(1)
    if precio_min and precio_max:
        if (precio_min <= nodo.producto.precio <= precio_max):
                ventana.blit(font.render(f'Nodo encontrado con un precio mayor que {precio_min} y un precio menor que {precio_max}' ,True,(0,0,0)),(30,30))
                pygame.display.update()
                time.sleep(2)
                ventana.fill((255,255,255))
                pintar_cuadro_informacion(ventana,font,nodo)
                pygame.display.update()
                time.sleep(5)
                ventana.fill((255,255,255))
                dibujar_nodo_main(ventana, raiz, (683), 150, 120,font)
                pygame.display.update()
    elif categoria:
        if (nodo.producto.categoria_producto == categoria):
                ventana.blit(font.render(f'Nodo encontrado con una categoria {categoria} con un id {nodo.producto.id}' ,True,(0,0,0)),(30,30))
                pygame.display.update()
                time.sleep(2)
                ventana.fill((255,255,255))
                pintar_cuadro_informacion(ventana,font,nodo)
                pygame.display.update()
                time.sleep(5)
                ventana.fill((255,255,255))
                dibujar_nodo_main(ventana, raiz, (683), 150, 120,font)
                pygame.display.update()

    pygame.draw.circle(ventana,(0,0,0),(x,y),20,2)
    pygame.display.update()
    
    if nodo.izquierda:
        dibujar_animacion_filtrar(ventana,nodo.izquierda,x - espacio, y+50 ,espacio//2,font,raiz,precio_min,precio_max,categoria)
    if nodo.derecha:
        dibujar_animacion_filtrar(ventana,nodo.derecha,x + espacio, y+50 ,espacio//2,font,raiz,precio_min,precio_max,categoria)

#pintar_rectangulo_bordeado
#descripcion:es el encargado de que las cajas de texto o lo botones tengan una apariencia bordeada
# ventana(es la ventana donde se esta mostrando todo la parte visual) 
#rect(son las dimensiones de la caja o los botones)
#color(represntara de que color sewera pintado la caja)

def pintar_rectangulo_bordeado(ventana, rect, color, corner_radius):
    pygame.draw.rect(ventana, color, rect, border_radius=corner_radius)
    pygame.draw.rect(ventana, (0, 0, 0), rect, 2, border_radius= corner_radius)

#pintar_cuadro_informativo
#descripcion:pinta uin cuiadron grande con los atributos de el producto
#parametros:
# ventana(es la ventana donde se esta mostrando todo la parte visual) 
#font(representa la fuente delk texto)
#nodo(es que aque nodo que se le obtendram los atributos de el producto)


def pintar_cuadro_informacion(ventana,font,nodo):
    pintar_rectangulo_bordeado(ventana,(483,180,500,250),(250,250,250),10)  
    ventana.blit(font.render("Informacion del producto",True,(255,0,0)),(483+120,210)) 
    
    ventana.blit(font.render("Nombre del producto:",True,(0,0,0)),(495,250)) 
    ventana.blit(font.render(nodo.producto.nombre_producto,True,(0,0,0)),(727,250)) 

    ventana.blit(font.render("Cantidad del producto:",True,(0,0,0)),(495,290)) 
    ventana.blit(font.render(str(nodo.producto.cantidad),True,(0,0,0)),(748 ,290)) 

    ventana.blit(font.render("Precio del producto:",True,(0,0,0)),(495,330)) 
    ventana.blit(font.render(str(nodo.producto.precio),True,(0,0,0)),(715,330)) 

    ventana.blit(font.render("Categoria del producto:",True,(0,0,0)),(495,370)) 
    ventana.blit(font.render(nodo.producto.categoria_producto,True,(0,0,0)),(750,370)) 

#dibujar_nodo_main
#descriopcio:este metodo dibuja el arbol sin animaciones
#parametros:
# ventana(es la ventana donde se esta mostrando todo la parte visual) 
#nodo(el nodo que se dibujara)
#x,y(Las poscicion donde se dibujara el circulo y hace referencia a el centro del circulo)
#espacio(Es el espacio que se dejara entre el nodo padre y los hijos)
#font(hace referencia a la fuente)

def dibujar_nodo_main(ventana, nodo, x, y, espacio,font):
    if nodo:
        # Dibujar líneas entre nodos
        if nodo.izquierda:
            pygame.draw.line(ventana, (0, 0, 0), (x, y), (x - espacio, y + 50), 2)
            
        if nodo.derecha:
            pygame.draw.line(ventana, (0, 0, 0), (x, y), (x + espacio, y + 50), 2)

        # Dibujar nodo
        if nodo.producto.cantidad == 0:
            pygame.draw.circle(ventana, (70, 75, 57), (x, y), 20)
        else:
            pygame.draw.circle(ventana, (0, 128, 255), (x, y), 20)
        pygame.draw.circle(ventana, (0, 0, 0), (x, y), 20, 2)
        texto = font.render(str(nodo.producto.id), True, (255, 255, 255))
        ventana.blit(texto, (x -6 , y - 10))
        
        dibujar_nodo_main(ventana, nodo.izquierda, x - espacio, y + 50, espacio // 2,font)
        dibujar_nodo_main(ventana, nodo.derecha, x + espacio, y + 50, espacio // 2,font)


#guardar_arbol
#descripcion:este metodo guardara los arboles que el usuario quiera en formato json
#parametros:
#arbol(es el arbol avl)
#nombre(nombre del arcchivo que el usaurio le puso)
def guardar_arbol_archivo(arbol, nombre):
    if not arbol:
        pass
    ruta_archivo = "arboles/"+nombre+".json"
    datos= {}
    datos["root"] = str(arbol.raiz.producto.id)

    cola = [arbol.raiz.producto.id]

    while cola:
        actual = cola.pop(0)

        nodo = arbol.buscar_nodo_por_id(actual)
        producto = {
            "cantidad": nodo.producto.cantidad,
            "precio": nodo.producto.precio,
            "categoria": nodo.producto.categoria_producto,
            "nombre": nodo.producto.nombre_producto
        }
        datos[str(actual)]= {}
        datos[str(actual)]["producto"] = producto
        datos[str(actual)]["altura"] = nodo.altura
        datos[str(actual)]["hijo_izquierdo"] = None
        datos[str(actual)]["hijo_derecho"] = None
        if nodo.izquierda:
            datos[str(actual)]["hijo_izquierdo"] = str(nodo.izquierda.producto.id) 
            cola.append(nodo.izquierda.producto.id)
        if nodo.derecha:
            datos[str(actual)]["hijo_derecho"] = str(nodo.derecha.producto.id) 
            cola.append(nodo.derecha.producto.id)
     
    with open(ruta_archivo, 'w') as f:
        json.dump(datos, f) 

#cargar_arbol_archivo
#parametros:
# ventana(es la ventana donde se esta mostrando todo la parte visual) 
#arbol(es el arbol avl)
#nombre(nombre del arcchivo que el usaurio le puso)


def cargar_arbol_archivo(ventana,screen_info, arbol, nombre):
    arbol.raiz = None
    ruta_archivo = "arboles/"+nombre+".json"
    font = pygame.font.Font(None, 32)
    try:
        with open(ruta_archivo, 'r') as f:
            datos = json.load(f)
            id_root= datos["root"]
            cola = [id_root]
            _cargar_arbol(ventana,screen_info, arbol,cola, datos)

    except FileNotFoundError:
        ventana.blit(font.render(f'El archivo no esxistente' ,True,(0,0,0)),(screen_info.current_w//2,screen_info.current_h//2))
        pygame.display.update()
        time.sleep(1)
def _cargar_arbol(ventana,screen_info, arbol,cola, datos):

    while cola:
        actual = cola.pop(0)

        datos_nodo = datos[actual]["producto"]
        altura=datos[actual]["altura"]

        nuevo_producto = Producto(cantidad=int(datos_nodo["cantidad"]), nombre_producto=datos_nodo["nombre"], precio=int(datos_nodo["precio"]), categoria_producto=datos_nodo["categoria"],id=int(actual))
        arbol.insertar(nuevo_producto,ventana,screen_info)
        if datos[actual]["hijo_izquierdo"]:
            cola.append(datos[actual]["hijo_izquierdo"])
        if datos[actual]["hijo_derecho"]:
            cola.append(datos[actual]["hijo_derecho"])

    
