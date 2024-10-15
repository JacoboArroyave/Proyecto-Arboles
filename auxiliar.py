import pygame, time, json
from producto import Producto

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
def dibujar_animacion_filtrar_combinada(ventana,nodo,x,y,espacio,font,categoria,cantidad,precio_min,precio_max,raiz):
        pygame.draw.circle(ventana,(255,0,0),(x,y),20,2)
        pygame.display.update()
        time.sleep(1)
        y_texto=30
        font_texto = pygame.font.Font(None, 25)
        if validar_precio(nodo,precio_min,precio_max) and validar_categoria(nodo,categoria) and validar_cantidad(nodo,cantidad):
            if validar_precio(nodo,precio_min,precio_max):
                ventana.blit(font_texto.render(f'Nodo encontrado con un precio mayor que {precio_min} y un precio menor que {precio_max}' ,True,(0,0,0)),(30,y_texto))
                y_texto+=30
            if validar_categoria(nodo,categoria):
                ventana.blit(font_texto.render(f'Nodo encontrado con una categoria {categoria}' ,True,(0,0,0)),(30,y_texto))
                y_texto+=30
            if validar_cantidad(nodo,cantidad):
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
    

def validar_precio(nodo,precio_min,precio_max):
    if precio_min != "" and precio_max !="":
        return int(precio_min) <= nodo.producto.precio <= int(precio_max)   
    return True   
def validar_categoria(nodo,categoria):
    if categoria !="":
        return categoria == nodo.producto.categoria_producto   
    return True   
def validar_cantidad(nodo,cantidad):
    if cantidad !="":
        return int(cantidad) == nodo.producto.cantidad   
    return True   



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


def pintar_rectangulo_bordeado(ventana, rect, color, corner_radius):
    pygame.draw.rect(ventana, color, rect, border_radius=corner_radius)
    pygame.draw.rect(ventana, (0, 0, 0), rect, 2, border_radius= corner_radius)


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

def guardar_arbol_archivo(arbol, nombre):

    print(arbol)
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



def cargar_arbol_archivo(ventana,screen_info, arbol, ruta_archivo):
    arbol.raiz = None
    with open(ruta_archivo, 'r') as f:
        datos = json.load(f)
        id_root= datos["root"]
        cola = [id_root]

        _cargar_arbol(ventana,screen_info, arbol,cola, datos)

def _cargar_arbol(ventana,screen_info, arbol,cola, datos):

    while cola:
        actual = cola.pop(0)

        datos_nodo = datos[actual]["producto"]
        altura=datos[actual]["altura"]

        nuevo_producto = Producto(cantidad=int(datos_nodo["cantidad"]), nombre_producto=datos_nodo["nombre"], precio=int(datos_nodo["precio"]), categoria_producto=datos_nodo["categoria"],id=int(actual))
        arbol.insertar(nuevo_producto,ventana,screen_info)
        print(actual,datos[actual])
        if datos[actual]["hijo_izquierdo"]:
            cola.append(datos[actual]["hijo_izquierdo"])
        if datos[actual]["hijo_derecho"]:
            cola.append(datos[actual]["hijo_derecho"])

    
