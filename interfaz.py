import pygame
from arbol import Arbol
from producto import Producto

pygame.init()
screen_info = pygame.display.Info()
screen_width, screen_height = screen_info.current_w, screen_info.current_h
ventana = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
pygame.display.set_caption("Árbol AVL")

font = pygame.font.Font(None, 32)
input_boxes = [
    {"rect": pygame.Rect(250, 50, 200, 30), "color": (0, 0, 0), "active": False, "text": "1"},
    {"rect": pygame.Rect(250, 100, 200, 30), "color": (0, 0, 0), "active": False, "text": "1"},
    {"rect": pygame.Rect(250, 150, 200, 30), "color": (0, 0, 0), "active": False, "text": "1"},
    {"rect": pygame.Rect(250, 200, 200, 30), "color": (0, 0, 0), "active": False, "text": "1"}
]
input_labels = ["Cantidad:", "Nombre Producto:", "Precio:", "Categoría Producto:"]
insertar_boton = pygame.Rect(250, 250, 100, 40)
mostrar_formulario_boton = pygame.Rect(50, 50, 200, 40)
volver_menu_boton = pygame.Rect(screen_width - 200, 20, 150, 40)
formulario_visible = Fals = False

arbol = Arbol()
root = arbol.raiz

def dibujar_nodo(ventana, nodo, x, y, espacio):
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
        
        dibujar_nodo(ventana, nodo.izquierda, x - espacio, y + 50, espacio // 2)
        dibujar_nodo(ventana, nodo.derecha, x + espacio, y + 50, espacio // 2)

def manejar_eventos(event):
    global root, formulario_visible
    for box in input_boxes:
        if event.type == pygame.MOUSEBUTTONDOWN:
            if formulario_visible:
                box["active"] = box["rect"].collidepoint(event.pos)
                if insertar_boton.collidepoint(event.pos):
                    cantidad_text = input_boxes[0]["text"]
                    nombre = input_boxes[1]["text"]
                    precio_text = input_boxes[2]["text"]
                    categoria = input_boxes[3]["text"]

                    if cantidad_text and nombre and precio_text and categoria:
                        try:
                     
                            formulario_visible = False
                            cantidad = int(cantidad_text)
                            precio = float(precio_text)
                            nuevo_producto = Producto(cantidad, nombre, precio, categoria)
                            arbol.insertar(nuevo_producto,ventana,screen_info )
                            root = arbol.raiz
                       
                            for box in input_boxes:
                                box["text"] = "1"
                            print("Producto insertado")
                        except ValueError:
                            print("Cantidad y precio deben ser números válidos.")
                    else:
                        print("Todos los campos deben estar llenos")
            if mostrar_formulario_boton.collidepoint(event.pos) :
                formulario_visible = True
            
            if volver_menu_boton.collidepoint(event.pos):
                formulario_visible = False

        if box["active"] and formulario_visible and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                box["active"] = False
            elif event.key == pygame.K_BACKSPACE:
                box["text"] = box["text"][:-1]
            else:
                box["text"] += event.unicode

def draw_rounded_rect(surface, rect, color, corner_radius):
    pygame.draw.rect(surface, color, rect, border_radius=corner_radius)
    pygame.draw.rect(surface, (0, 0, 0), rect, 2, border_radius=corner_radius)

running = True  

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        manejar_eventos(event)
    
    ventana.fill((255, 255, 255))

    if formulario_visible:
        for i, box in enumerate(input_boxes):
            draw_rounded_rect(ventana, box["rect"], (230, 230, 230), 10)
            text_surface = font.render(box["text"], True, (0, 0, 0))
            ventana.blit(text_surface, (box["rect"].x + 5, box["rect"].y + 5))
            ventana.blit(font.render(input_labels[i], True, (0, 0, 0)), (box["rect"].x - 230, box["rect"].y + 5))
        draw_rounded_rect(ventana, insertar_boton, (0, 255, 0), 10)
        ventana.blit(font.render("Insertar", True, (0, 0, 0)), (insertar_boton.x + 10, insertar_boton.y + 5))
        draw_rounded_rect(ventana, volver_menu_boton, (255, 0, 0), 10)
        ventana.blit(font.render("Volver", True, (255, 255, 255)), (volver_menu_boton.x + 10, volver_menu_boton.y + 5))
    else:
        draw_rounded_rect(ventana, mostrar_formulario_boton, (0, 128, 0), 10)
        ventana.blit(font.render("Agregar Producto", True, (255, 255, 255)), (mostrar_formulario_boton.x +5, mostrar_formulario_boton.y + 8))
    dibujar_nodo(ventana, root, screen_width // 2, 150, 120)
    pygame.display.update()
   
pygame.quit()
    