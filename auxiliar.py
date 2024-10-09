import pygame, time
def dibujar_nodo(ventana, nodo, x, y, espacio, color=(0, 128, 255)):
   
    if nodo:
        # Dibujar líneas entre nodos
        if nodo.izquierda:
            pygame.draw.line(ventana, (0,0,0), (x, y), (x - espacio, y + 50), 2)
        if nodo.derecha:
            pygame.draw.line(ventana, (0,0,0), (x, y), (x + espacio, y + 50), 2)

        # Dibujar nodo
        dibujar(ventana,nodo,x,y,espacio, borde=(255, 0, 0))
        pygame.display.update()
        # dibujar(ventana,nodo,x,y,espacio,color)
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


