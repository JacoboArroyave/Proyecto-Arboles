import pygame, time
def dibujar_nodo(ventana, nodo, x, y, espacio, color=(0, 128, 255)):
    if nodo:
        # Dibujar líneas entre nodos
        if nodo.izquierda:
            pygame.draw.line(ventana, (0,0,0), (x, y), (x - espacio, y + 50), 2)
        if nodo.derecha:
            pygame.draw.line(ventana, (0,0,0), (x, y), (x + espacio, y + 50), 2)

        # Dibujar nodo
        dibujar(ventana,nodo,x,y,espacio)
        pygame.display.update()
        dibujar_nodo(ventana, nodo.izquierda, x - espacio, y + 50, espacio // 2, color)
        dibujar_nodo(ventana, nodo.derecha, x + espacio, y + 50, espacio // 2, color)
        dibujar(ventana,nodo,x,y,espacio)

    
def dibujar(ventana, nodo, x, y, espacio, color= (0, 128, 255), borde=(0,0,0)):
    font = pygame.font.Font(None, 32)
    pygame.draw.circle(ventana,color, (x, y), 20)
    pygame.draw.circle(ventana, borde, (x, y), 20, 2)
    texto = font.render(str(nodo.producto.id), True, (255, 255, 255))
    ventana.blit(texto, (x -6 , y - 10))
    pygame.display.update()
    pygame.draw.circle(ventana, borde, (x, y), 20, 2)
    time.sleep(0.2)
    pygame.display.update()

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
            return dibujar_animacion_buscar_id(ventana,nodo.derecha,x - espacio, y+50, espacio//2,font,id)
    return False

def dibujar_animacion_filtrar(ventana,nodo,x,y,espacio,font,raiz,precio_min,precio_max,categoria):
    
    pygame.draw.circle(ventana,(255,0,0),(x,y),20,2)
    pygame.display.update()
    time.sleep(1)
    if precio_min and precio_max:
        if (precio_min <= nodo.producto.precio <= precio_max):
                ventana.fill((255,255,255))
                ventana.blit(font.render(f'Nodo encontrado con un precio mayor que {precio_min} y un precio menor que {precio_max}' ,True,(0,0,0)),(30,30))
                pintar_cuadro_informacion(ventana,font,nodo)
                pygame.display.update()
                time.sleep(5)
                ventana.fill((255,255,255))
                dibujar_nodo_main(ventana, raiz, (683), 150, 120,font)
                pygame.display.update()
    elif categoria:
        if (nodo.producto.categoria_producto == categoria):
                ventana.fill((255,255,255))
                ventana.blit(font.render(f'Nodo encontrado con una categoria {categoria} con un id {nodo.producto.id}' ,True,(0,0,0)),(30,30))
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
    pygame.draw.rect(ventana, (0, 0, 0), rect, 2, border_radius=corner_radius)


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
        pygame.draw.circle(ventana, (0, 128, 255), (x, y), 20)
        pygame.draw.circle(ventana, (0, 0, 0), (x, y), 20, 2)
        texto = font.render(str(nodo.producto.id), True, (255, 255, 255))
        ventana.blit(texto, (x -6 , y - 10))
        
        dibujar_nodo_main(ventana, nodo.izquierda, x - espacio, y + 50, espacio // 2,font)
        dibujar_nodo_main(ventana, nodo.derecha, x + espacio, y + 50, espacio // 2,font)