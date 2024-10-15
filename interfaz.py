import pygame
from arbol import Arbol
from producto import Producto
import time
from auxiliar import dibujar_nodo
from auxiliar import dibujar_animacion_buscar_id
from auxiliar import dibujar_animacion_filtrar    
from auxiliar import dibujar_animacion_filtrar_combinada    
from auxiliar import pintar_rectangulo_bordeado
from auxiliar import dibujar_nodo_main
from auxiliar import cargar_arbol_archivo
from auxiliar import guardar_arbol_archivo

# import botones

pygame.init()
screen_info = pygame.display.Info()
screen_width, screen_height = screen_info.current_w, screen_info.current_h
ventana = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
pygame.display.set_caption("Árbol AVL")

font = pygame.font.Font(None, 32)

#inputs
input_boxes_producto = [
    {"rect": pygame.Rect(250, 50, 200, 30), "color": (230,230,230), "active": False, "text": "gelatina"},
    {"rect": pygame.Rect(250, 100, 200, 30), "color": (230,230,230), "active": False, "text": "1"},
    {"rect": pygame.Rect(250, 150, 200, 30), "color": (230,230,230), "active": False, "text": "1200"},
    {"rect": pygame.Rect(250, 200, 200, 30), "color": (230,230,230), "active": False, "text": "comida"}
]
input_boxes_combinada = [
    {"rect": pygame.Rect(300, 50, 200, 30), "color": (230,230,230), "active": False, "text": "1200"},
    {"rect": pygame.Rect(300, 100, 200, 30), "color": (230,230,230), "active": False, "text": "1300"},
    {"rect": pygame.Rect(300, 150, 200, 30), "color": (230,230,230), "active": False, "text": ""},
    {"rect": pygame.Rect(300, 200, 200, 30), "color": (230,230,230), "active": False, "text": ""}
]

input_boxes_filtrar_precio =[
    {"rect": pygame.Rect(300, 50, 200, 30), "color": (230, 230, 230), "active": False, "text": ""},
    {"rect": pygame.Rect(300, 100, 200, 30), "color": (230, 230, 230), "active": False, "text": ""}
]
input_boxes_actualizar =[
    {"rect": pygame.Rect(743, 290 ,150, 25), "color": (215, 215, 215), "active": False, "text": ""},
    {"rect": pygame.Rect(715, 333, 150, 25), "color": (215, 215, 215), "active": False, "text": ""}
]
input_box_eliminar ={"rect": pygame.Rect(190, 50, 200, 30), "color": (230, 230, 230), "active": False, "text": ""}
input_box_buscar_id = {"rect": pygame.Rect(190, 50, 200, 30), "color": (230, 230, 230), "active": False, "text": ""}
input_box_categoria = {"rect": pygame.Rect(250, 50, 200, 30), "color": (230, 230, 230), "active": False, "text": ""}
input_box_nombre = {"rect": pygame.Rect(250, 50, 200, 30), "color": (230, 230, 230), "active": False, "text": ""}

# texto de los inputs
input_labels_producto = [ "Nombre producto:","Cantidad:", "Precio:", "Categoría Producto:"]
input_labels_combinada = ["Ingrese el precio minimo:","Ingrese el precio maximo:","Filtrar por cantidad:", "Filtrar por categoria:"]
input_labels_filtrar_precio = ["Ingrese el precio minimo:","Ingrese el precio maximo:"]

#diccionario para la informacion de los atributos
atributos_productos = { "Nombre producto" : "" ,"Cantidad": "","Precio":"","Categoria":""}



#Botones de guardar
insertar_boton = pygame.Rect(250, 250, 100, 40)
eliminar_boton = pygame.Rect(190, 90, 110, 40)
buscar_id_boton = pygame.Rect(190, 90, 110, 40)
filtrar_precio_boton = pygame.Rect(300, 140, 110, 40)
filtrar_categoria_boton = pygame.Rect(250, 90, 110, 40)
filtrar_combinada_boton = pygame.Rect(250, 240, 110, 40)
filtrar_buscar_nombre = pygame.Rect(250, 90, 110, 40)
actualizar_atributos_boton = pygame.Rect(481, 440, 140, 40)



#botones formularios
#mostrar fomulario de insertar producto
mostrar_formulario_boton = pygame.Rect(50, 50, 240, 40)
mostrar_eliminar_boton = pygame.Rect(50, 110 , 240, 40)
mostrar_buscar_id_boton = pygame.Rect(50, 170 , 240, 40)
mostrar_filtrar_precio_boton = pygame.Rect(50, 230 , 240, 40)
mostrar_filtrar_categoria_boton = pygame.Rect(50, 290 , 240, 40)
mostrar_filtrar_combinada_boton = pygame.Rect(50, 350 , 240, 40)
mostrar_actualizar_datos = pygame.Rect(50, 410, 240, 40)
guardar_arbol_boton=pygame.Rect(50,470, 240, 40)
cargar_arbol_boton=pygame.Rect(50,530, 240, 40)
volver_menu_boton = pygame.Rect(screen_width - 240, 20, 150, 40)

formulario_visible_producto = False
formulario_visible_eliminar = False
formulario_visible_buscar_id = False
formulario_visible_categoria = False
formulario_visible_combinada = False
formulario_visible_filtrar_precio = False
formulario_visible_actualizar_datos = False
actualizar_atributos = False
cargar_arbol=False
guardar_arbol=False

nodo_a_actualizar=None



arbol = Arbol()
raiz = arbol.raiz
def manejar_eventos(event):
    global guardar_arbol,cargar_arbol,raiz, formulario_visible_producto,formulario_visible_eliminar,formulario_visible_buscar_id,atributos_productos,formulario_visible_filtrar_precio,formulario_visible_categoria,productos_visibles,formulario_visible_combinada,formulario_visible_actualizar_datos,nodo_a_actualizar,actualizar_atributos                 
    #este es el manejadoor de insertar
    for box in input_boxes_producto:
        if event.type == pygame.MOUSEBUTTONDOWN:
            if formulario_visible_producto:
                box["active"] = box["rect"].collidepoint(event.pos)
                if insertar_boton.collidepoint(event.pos):
                    nombre = input_boxes_producto[0]["text"]
                    cantidad_text = input_boxes_producto[1]["text"]
                    precio_text = input_boxes_producto[2]["text"]
                    categoria = input_boxes_producto[3]["text"]

                    if cantidad_text and nombre and precio_text and categoria:
                     
                        formulario_visible_producto = False
                        cantidad = int(cantidad_text)
                        precio = int(precio_text)
                        nuevo_producto = Producto(cantidad, nombre, precio, categoria)
                        arbol.insertar(nuevo_producto,ventana,screen_info )
                        raiz = arbol.raiz
                        for box in input_boxes_producto:
                            box["text"] = "1"
                    else:
                        print("Todos los campos deben estar llenos")
            if mostrar_formulario_boton.collidepoint(event.pos)  and not formulario_visible_eliminar and not formulario_visible_buscar_id and not formulario_visible_categoria and not formulario_visible_combinada and not formulario_visible_filtrar_precio and not formulario_visible_actualizar_datos and not actualizar_atributos:

                formulario_visible_producto = True

            if volver_menu_boton.collidepoint(event.pos):
                formulario_visible_producto = False

        if box["active"] and formulario_visible_producto and event.type == pygame.KEYDOWN :
            if event.key == pygame.K_RETURN:
                box["active"] = False
            elif event.key == pygame.K_BACKSPACE:
                box["text"] = box["text"][:-1]
            else:   
                box["text"] += event.unicode
    # manejo de eventos de eliminar            
    if event.type == pygame.MOUSEBUTTONDOWN:
        if formulario_visible_eliminar:
            input_box_eliminar["active"] = input_box_eliminar["rect"].collidepoint(event.pos)
            if eliminar_boton.collidepoint(event.pos):
                id = input_box_eliminar["text"]
                if id:
                    formulario_visible_eliminar=False
                    arbol.eliminar_nodo(int(id),1,ventana,screen_info)
                    raiz=arbol.raiz

        if mostrar_eliminar_boton.collidepoint(event.pos) and not formulario_visible_producto  and not formulario_visible_buscar_id and not formulario_visible_categoria and not formulario_visible_combinada and not formulario_visible_filtrar_precio and not formulario_visible_actualizar_datos and not actualizar_atributos:
            formulario_visible_eliminar = True
        if volver_menu_boton.collidepoint(event.pos) :
            formulario_visible_eliminar = False

    if input_box_eliminar["active"] and formulario_visible_eliminar and event.type == pygame.KEYDOWN :
        if event.key == pygame.K_RETURN:
            input_box_eliminar["active"] = False
        elif event.key == pygame.K_BACKSPACE:
            input_box_eliminar["text"] = input_box_eliminar["text"][:-1]
        else:
            input_box_eliminar["text"] += event.unicode
    #manejo de eventos de buscar por id 
    if event.type == pygame.MOUSEBUTTONDOWN:
        if formulario_visible_buscar_id:
            input_box_buscar_id["active"] = input_box_buscar_id["rect"].collidepoint(event.pos)
            if buscar_id_boton.collidepoint(event.pos):
                id = input_box_buscar_id["text"]
                if id:
                    
                    if raiz:
                        nodo=arbol.buscar_nodo_por_id(int(id))
                        producto=nodo.producto
                        if producto:
                            atributos_productos["Nombre producto"]=producto.nombre_producto
                            atributos_productos["Categoria"]=producto.categoria_producto
                            atributos_productos["Precio"]=str(producto.precio)
                            atributos_productos["Cantidad"]=str(producto.cantidad)
                            input_box_buscar_id["text"]=""
                            ventana.fill((255,255,255))
                            dibujar_nodo_main(ventana, raiz, (screen_width // 2), 150, 120,font)
                            animacion=dibujar_animacion_buscar_id(ventana,raiz,(screen_width // 2), 150, 120,font,int(id))
                        else:
                            print("El nodo no existe")    
                    print("No hay ningun arbol guardado")
                
        if mostrar_buscar_id_boton.collidepoint(event.pos) and not formulario_visible_producto and not formulario_visible_eliminar and not formulario_visible_categoria and not formulario_visible_combinada and not formulario_visible_filtrar_precio and not formulario_visible_actualizar_datos and not actualizar_atributos  :
            formulario_visible_buscar_id = True
        if volver_menu_boton.collidepoint(event.pos) :
            formulario_visible_buscar_id = False
            atributos_productos["Nombre producto"]=""
            atributos_productos["Categoria"]=""
            atributos_productos["Precio"]=""
            atributos_productos["Cantidad"]=""

            input_box_buscar_id["text"]=""

    if input_box_buscar_id["active"] and formulario_visible_buscar_id and event.type == pygame.KEYDOWN :

        if event.key == pygame.K_RETURN:
            input_box_buscar_id["active"] = False
        elif event.key == pygame.K_BACKSPACE:
            input_box_buscar_id["text"] = input_box_buscar_id["text"][:-1]
        else:
            input_box_buscar_id["text"] += event.unicode
            
    #filtrar precio
    for box in input_boxes_filtrar_precio:
        if event.type == pygame.MOUSEBUTTONDOWN:
            if formulario_visible_filtrar_precio:
                box["active"] = box["rect"].collidepoint(event.pos)
                if filtrar_precio_boton.collidepoint(event.pos):
                    precio_min = input_boxes_filtrar_precio[0]["text"]
                    precio_max = input_boxes_filtrar_precio[1]["text"]

                    if precio_min and precio_max and precio_min < precio_max:
                        try:
                            formulario_visible_filtrar_precio = False
                            precio_min=int(precio_min)
                            precio_max=int(precio_max)
                            ventana.fill((255,255,255))
                            dibujar_nodo_main(ventana, raiz, (screen_width // 2), 150, 120,font)
                            animacion=dibujar_animacion_filtrar(ventana,raiz,(screen_width // 2), 150, 120,font,raiz,precio_min,precio_max,None)
                            for box in input_boxes_filtrar_precio:
                                box["text"] = ""
                        except ValueError:
                            print("Error")
                    else:   
                        print("Todos los campos deben estar llenos")
            if mostrar_filtrar_precio_boton.collidepoint(event.pos) and not formulario_visible_producto and not formulario_visible_eliminar and not formulario_visible_buscar_id and not formulario_visible_categoria and not formulario_visible_combinada  and not formulario_visible_actualizar_datos and not actualizar_atributos :

                formulario_visible_filtrar_precio = True

            if volver_menu_boton.collidepoint(event.pos):
                formulario_visible_filtrar_precio = False

        if box["active"] and formulario_visible_filtrar_precio and event.type == pygame.KEYDOWN :
            if event.key == pygame.K_RETURN:
                box["active"] = False
            elif event.key == pygame.K_BACKSPACE:
                box["text"] = box["text"][:-1]
            else:   
                box["text"] += event.unicode
   
    #Filtrar por categoria
    if event.type == pygame.MOUSEBUTTONDOWN:
        if formulario_visible_categoria:
            input_box_categoria["active"] = input_box_categoria["rect"].collidepoint(event.pos)
            if filtrar_categoria_boton.collidepoint(event.pos):
                categoria = input_box_categoria["text"]
                if categoria:
                    # productos=arbol.filtrar_categoria(categoria)
                    ventana.fill((255,255,255))
                    dibujar_nodo_main(ventana, raiz, (screen_width // 2), 150, 120,font)
                    animacion=dibujar_animacion_filtrar(ventana,raiz,(screen_width // 2), 150, 120,font,raiz,None,None,categoria)

                    

        if mostrar_filtrar_categoria_boton.collidepoint(event.pos) and not formulario_visible_producto and not formulario_visible_eliminar and not formulario_visible_buscar_id  and not formulario_visible_combinada and not formulario_visible_filtrar_precio and not formulario_visible_actualizar_datos and not actualizar_atributos:
            formulario_visible_categoria = True
        if volver_menu_boton.collidepoint(event.pos) :
            formulario_visible_categoria = False

    if input_box_categoria["active"] and formulario_visible_categoria and event.type == pygame.KEYDOWN :
        if event.key == pygame.K_RETURN:
            input_box_categoria["active"] = False
        elif event.key == pygame.K_BACKSPACE:
            input_box_categoria["text"] = input_box_categoria["text"][:-1]
        else:
            input_box_categoria["text"] += event.unicode
    #Filtrar combinada  
    for box in input_boxes_combinada:
        if event.type == pygame.MOUSEBUTTONDOWN:
            if formulario_visible_combinada:
                box["active"]=box["rect"].collidepoint(event.pos)
                if filtrar_combinada_boton.collidepoint(event.pos):
                    precio_min = (input_boxes_combinada[0]["text"])
                    precio_max= (input_boxes_combinada[1]["text"])
                    cantidad= (input_boxes_combinada[2]["text"])
                    categoria = input_boxes_combinada[3]["text"]
                    ventana.fill((255,255,255))

                    dibujar_nodo_main(ventana, raiz, (screen_width // 2), 150, 120,font)
                    dibujar_animacion_filtrar_combinada(ventana,arbol.raiz,(screen_width // 2), 150, 120,font,categoria,cantidad,precio_min,precio_max,arbol.raiz)
                    formulario_visible_combinada=False
                    for box in input_boxes_combinada:
                        box["text"] = ""
            if mostrar_filtrar_combinada_boton.collidepoint(event.pos) and not formulario_visible_producto and not formulario_visible_eliminar and not formulario_visible_buscar_id and not formulario_visible_categoria  and not formulario_visible_filtrar_precio and not formulario_visible_actualizar_datos and not actualizar_atributos:
                formulario_visible_combinada=True

            if volver_menu_boton.collidepoint(event.pos):
                formulario_visible_combinada = False
        if box["active"] and formulario_visible_combinada and event.type == pygame.KEYDOWN :
            if event.key == pygame.K_RETURN:
                box["active"] = False
            elif event.key == pygame.K_BACKSPACE:
                box["text"] = box["text"][:-1]
            else:   
                box["text"] += event.unicode

    #modifucando primera parte de actualizar            
    if event.type == pygame.MOUSEBUTTONDOWN:
        if formulario_visible_actualizar_datos:
            input_box_nombre["active"] = input_box_nombre["rect"].collidepoint(event.pos)
            if filtrar_categoria_boton.collidepoint(event.pos):
                nombre = input_box_nombre["text"]
                if nombre:
                    if arbol.buscar_nodo_nombre(nombre):
                        nodo_a_actualizar=arbol.buscar_nodo_nombre(nombre)
                        input_boxes_actualizar[0]["text"]=str(nodo_a_actualizar.producto.cantidad)
                        input_boxes_actualizar[1]["text"]=str(nodo_a_actualizar.producto.precio)
                        actualizar_atributos=True
                        formulario_visible_actualizar_datos=False
                        input_box_nombre["text"]=""
                    

        if mostrar_actualizar_datos.collidepoint(event.pos) and not formulario_visible_producto and not formulario_visible_eliminar and not formulario_visible_buscar_id and not formulario_visible_categoria and not formulario_visible_combinada and not formulario_visible_filtrar_precio  and not actualizar_atributos:
            formulario_visible_actualizar_datos = True
        if volver_menu_boton.collidepoint(event.pos) :
            formulario_visible_actualizar_datos = False

    if input_box_nombre["active"] and formulario_visible_actualizar_datos and event.type == pygame.KEYDOWN and not formulario_visible_buscar_id :
        if event.key == pygame.K_RETURN:
            input_box_nombre["active"] = False
        elif event.key == pygame.K_BACKSPACE:
            input_box_nombre["text"] = input_box_nombre["text"][:-1]
        else:
            input_box_nombre["text"] += event.unicode
    #modificando segunda parte actualizar
    for box in input_boxes_actualizar:
        if event.type == pygame.MOUSEBUTTONDOWN:
            if actualizar_atributos:
                
              box["active"]=box["rect"].collidepoint(event.pos) 
              if actualizar_atributos_boton.collidepoint(event.pos):
                cantidad =input_boxes_actualizar[0]["text"]
                precio =input_boxes_actualizar[1]["text"]
                arbol.actualizar_atributos(nodo_a_actualizar,cantidad,precio)
                actualizar_atributos = False
                
            if volver_menu_boton.collidepoint(event.pos) and not formulario_visible_producto and not formulario_visible_eliminar and not formulario_visible_buscar_id and not formulario_visible_categoria and not formulario_visible_combinada and not formulario_visible_filtrar_precio and not formulario_visible_actualizar_datos :
                actualizar_atributos = False

        if box["active"] and actualizar_atributos and event.type == pygame.KEYDOWN :
            if event.key == pygame.K_RETURN:
               box["active"] = False
            elif event.key == pygame.K_BACKSPACE:
                box["text"] = box["text"][:-1]
            else:   
                box["text"] += event.unicode    

    if event.type == pygame.MOUSEBUTTONDOWN:
        if cargar_arbol_boton.collidepoint(event.pos):
            cargar_arbol = True
        if cargar_arbol:
            cargar_arbol_archivo(ventana,screen_info ,arbol, "arboles/arbol2.json")
            raiz=arbol.raiz
            cargar_arbol=False

        # if volver_menu_boton.collidepoint(event.pos) :
        #     cargar_arbol = False
    if event.type == pygame.MOUSEBUTTONDOWN:
        if guardar_arbol_boton.collidepoint(event.pos):
            guardar_arbol = True
        if guardar_arbol:
            nombre = "arbol2"
            guardar_arbol_archivo(arbol,nombre)
            raiz=arbol.raiz
            guardar_arbol=False

        # if volver_menu_boton.collidepoint(event.pos) :
        #     guardar_arbol = False

    
    
    
running = True  

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        manejar_eventos(event)
    ventana.fill((255, 255, 255))

    if formulario_visible_producto:
        for i, box in enumerate(input_boxes_producto):
            pintar_rectangulo_bordeado(ventana, box["rect"], box["color"], 10)
            text_surface = font.render(box["text"], True, (0, 0, 0))
            ventana.blit(text_surface, (box["rect"].x + 5, box["rect"].y + 5))
            ventana.blit(font.render(input_labels_producto[i], True, (0, 0, 0)), (box["rect"].x - 230, box["rect"].y + 5))
        pintar_rectangulo_bordeado(ventana, insertar_boton, (0, 255, 0), 10)
        ventana.blit(font.render("Insertar", True, (0, 0, 0)), (insertar_boton.x + 10, insertar_boton.y + 5))
        pintar_rectangulo_bordeado(ventana, volver_menu_boton, (255, 0, 0), 10)
        ventana.blit(font.render("Volver", True, (255, 255, 255)), (volver_menu_boton.x + 10, volver_menu_boton.y + 5))

    elif formulario_visible_eliminar:
        pintar_rectangulo_bordeado(ventana, input_box_eliminar["rect"], input_box_eliminar["color"], 10)
        text_surface = font.render(input_box_eliminar["text"], True, (0, 0, 0))
        ventana.blit(text_surface, (input_box_eliminar["rect"].x + 5, input_box_eliminar["rect"].y + 5))
        ventana.blit(font.render("Ingrese el id", True, (0, 0, 0)), (input_box_eliminar["rect"].x - 150, input_box_eliminar["rect"].y + 5))
        pintar_rectangulo_bordeado(ventana, eliminar_boton, (0, 255, 0), 10)
        ventana.blit(font.render("Eliminar", True, (0, 0, 0)), (eliminar_boton.x + 10, eliminar_boton.y + 9))
        pintar_rectangulo_bordeado(ventana, volver_menu_boton, (255, 0, 0), 10)
        ventana.blit(font.render("Volver", True, (255, 255, 255)), (volver_menu_boton.x + 10, volver_menu_boton.y + 5))

    elif formulario_visible_buscar_id:
        pintar_rectangulo_bordeado(ventana, input_box_buscar_id["rect"], input_box_buscar_id["color"], 10)
        text_surface = font.render(input_box_buscar_id["text"], True, (0, 0, 0))
        ventana.blit(text_surface,(input_box_buscar_id["rect"].x + 5, input_box_buscar_id["rect"].y + 5))
        ventana.blit(font.render("Ingrese el id", True, (0, 0, 0)), (input_box_buscar_id["rect"].x - 150, input_box_buscar_id["rect"].y + 5))
        pintar_rectangulo_bordeado(ventana, buscar_id_boton, (0, 255, 0), 10)
        ventana.blit(font.render("Buscar", True, (0, 0, 0)), (buscar_id_boton.x + 10, buscar_id_boton.y + 9))
        pintar_rectangulo_bordeado(ventana, volver_menu_boton, (255, 0, 0), 10)
        ventana.blit(font.render("Volver", True, (255, 255, 255)), (volver_menu_boton.x + 10, volver_menu_boton.y + 5))

      
        pintar_rectangulo_bordeado(ventana,(screen_width//2-200,180,500,250),(250,250,250),10)  
        ventana.blit(font.render("Informacion del producto",True,(255,0,0)),(483+120,210)) 
        
        ventana.blit(font.render("Nombre del producto:",True,(0,0,0)),(495,250)) 
        ventana.blit(font.render(atributos_productos["Nombre producto"],True,(0,0,0)),(727,250)) 

        ventana.blit(font.render("Cantidad del producto:",True,(0,0,0)),(495,290))
        ventana.blit(font.render(atributos_productos["Cantidad"],True,(0,0,0)),(748 ,290)) 

        ventana.blit(font.render("Precio del producto:",True,(0,0,0)),(495,330)) 
        ventana.blit(font.render(atributos_productos["Precio"],True,(0,0,0)),(715,330)) 

        ventana.blit(font.render("Categoria del producto:",True,(0,0,0)),(495,370)) 
        ventana.blit(font.render(atributos_productos["Categoria"],True,(0,0,0)),(750,370)) 
    elif actualizar_atributos:
        pintar_rectangulo_bordeado(ventana, actualizar_atributos_boton, (0, 255, 0), 10)
        ventana.blit(font.render("Actualizar", True, (0, 0, 0)), (actualizar_atributos_boton.x + 10, actualizar_atributos_boton.y + 9))
        pintar_rectangulo_bordeado(ventana, volver_menu_boton, (255, 0, 0), 10)
        ventana.blit(font.render("Volver", True, (255, 255, 255)), (volver_menu_boton.x + 10, volver_menu_boton.y + 5))


        pintar_rectangulo_bordeado(ventana,(screen_width//2-200,180,500,250),(250,250,250),10)  
        ventana.blit(font.render("Informacion del producto",True,(255,0,0)),(483+120,210)) 
        
        ventana.blit(font.render("Nombre del producto:",True,(0,0,0)),(495,250)) 
        ventana.blit(font.render(nodo_a_actualizar.producto.nombre_producto,True,(0,0,0)),(727,250)) 

        for box in input_boxes_actualizar:
            pygame.draw.rect(ventana,box["color"],box["rect"])
        ventana.blit(font.render("Cantidad del producto:",True,(0,0,0)),(495,290))
        ventana.blit(font.render(input_boxes_actualizar[0]["text"],True,(0,0,0)),(input_boxes_actualizar[0]["rect"].x+3 ,input_boxes_actualizar[0]["rect"].y)) 
        

        ventana.blit(font.render("Precio del producto:",True,(0,0,0)),(495,330)) 
        ventana.blit(font.render(input_boxes_actualizar[1]["text"],True,(0,0,0)),(input_boxes_actualizar[1]["rect"].x+3 ,input_boxes_actualizar[1]["rect"].y) )

        ventana.blit(font.render("Categoria del producto:",True,(0,0,0)),(495,370)) 
        ventana.blit(font.render(nodo_a_actualizar.producto.categoria_producto,True,(0,0,0)),(750,370))

  
        
        
    elif formulario_visible_filtrar_precio:
        for i, box in enumerate(input_boxes_filtrar_precio):
            pintar_rectangulo_bordeado(ventana, box["rect"], box["color"], 10)
            text_surface = font.render(box["text"], True, (0, 0, 0))
            ventana.blit(text_surface, (box["rect"].x + 5, box["rect"].y + 5))
            ventana.blit(font.render(input_labels_filtrar_precio[i], True, (0, 0, 0)), (box["rect"].x - 280, box["rect"].y + 5))
        
        pintar_rectangulo_bordeado(ventana, filtrar_precio_boton, (0, 255, 0), 10)
        ventana.blit(font.render("Buscar", True, (0, 0, 0)), (filtrar_precio_boton.x + 10, filtrar_precio_boton.y + 9))
        
        pintar_rectangulo_bordeado(ventana, volver_menu_boton, (255, 0, 0), 10)
        ventana.blit(font.render("Volver", True, (255, 255, 255)), (volver_menu_boton.x + 10, volver_menu_boton.y + 5))   

    elif formulario_visible_categoria:
        pintar_rectangulo_bordeado(ventana, input_box_categoria["rect"], input_box_categoria["color"], 10)
        text_surface = font.render(input_box_categoria["text"], True, (0, 0, 0))
        ventana.blit(text_surface,(input_box_categoria["rect"].x + 5, input_box_categoria["rect"].y + 5))
        ventana.blit(font.render("Ingrese la categoria", True, (0, 0, 0)), (input_box_categoria["rect"].x - 225, input_box_categoria["rect"].y + 5))
        pintar_rectangulo_bordeado(ventana, filtrar_categoria_boton, (0, 255, 0), 10)
        ventana.blit(font.render("Buscar", True, (0, 0, 0)), (filtrar_categoria_boton.x + 10, filtrar_categoria_boton.y + 9))
        pintar_rectangulo_bordeado(ventana, volver_menu_boton, (255, 0, 0), 10)
        ventana.blit(font.render("Volver", True, (255, 255, 255)), (volver_menu_boton.x + 10, volver_menu_boton.y + 5))
        
    elif formulario_visible_actualizar_datos:
        pintar_rectangulo_bordeado(ventana, input_box_nombre["rect"], input_box_nombre["color"], 10)
        text_surface = font.render(input_box_nombre["text"], True, (0, 0, 0))
        ventana.blit(text_surface,(input_box_nombre["rect"].x + 5, input_box_nombre["rect"].y + 5))
        ventana.blit(font.render("Ingrese el nombre", True, (0, 0, 0)), (input_box_nombre["rect"].x - 225, input_box_nombre["rect"].y + 5))
        pintar_rectangulo_bordeado(ventana, filtrar_buscar_nombre, (0, 255, 0), 10)
        ventana.blit(font.render("Buscar", True, (0, 0, 0)), (filtrar_buscar_nombre.x + 10, filtrar_buscar_nombre.y + 9))
        pintar_rectangulo_bordeado(ventana, volver_menu_boton, (255, 0, 0), 10)
        ventana.blit(font.render("Volver", True, (255, 255, 255)), (volver_menu_boton.x + 10, volver_menu_boton.y + 5))
        
    elif formulario_visible_combinada:
        for i,box in enumerate(input_boxes_combinada):
            pintar_rectangulo_bordeado(ventana, box["rect"], box["color"], 10)
            text_surface = font.render(box["text"], True, (0, 0, 0))
            ventana.blit(text_surface, (box["rect"].x + 5, box["rect"].y + 5))
            ventana.blit(font.render(input_labels_combinada[i], True, (0, 0, 0)), (box["rect"].x - 290, box["rect"].y + 5))
        pintar_rectangulo_bordeado(ventana, filtrar_combinada_boton, (0, 255, 0), 10)
        ventana.blit(font.render("Buscar", True, (0, 0, 0)), (filtrar_combinada_boton.x + 10, filtrar_combinada_boton.y + 9))
        
        pintar_rectangulo_bordeado(ventana, volver_menu_boton, (255, 0, 0), 10)
        ventana.blit(font.render("Volver", True, (255, 255, 255)), (volver_menu_boton.x + 10, volver_menu_boton.y + 5))   



    else:
        #Muestra el boton de agregar producto producto
        pintar_rectangulo_bordeado(ventana, mostrar_formulario_boton, (0, 128, 0), 10)
        ventana.blit(font.render("Agregar producto", True, (255, 255, 255)), (mostrar_formulario_boton.x +5, mostrar_formulario_boton.y + 8))
        #Muestra el boton de eliminar producto
        pintar_rectangulo_bordeado(ventana, mostrar_eliminar_boton, (0, 128, 0), 10)
        ventana.blit(font.render("Eliminar producto", True, (255, 255, 255)), (mostrar_eliminar_boton.x +5, mostrar_eliminar_boton.y + 8))
        
        pintar_rectangulo_bordeado(ventana, mostrar_buscar_id_boton, (0, 128, 0), 10)
        ventana.blit(font.render("Buscar por id", True, (255, 255, 255)), (mostrar_buscar_id_boton.x +5, mostrar_buscar_id_boton.y + 8))

        pintar_rectangulo_bordeado(ventana, mostrar_filtrar_precio_boton, (0, 128, 0), 10)
        ventana.blit(font.render("Filtrar por precio", True, (255, 255, 255)), (mostrar_filtrar_precio_boton.x +5, mostrar_filtrar_precio_boton.y + 8))
        
        pintar_rectangulo_bordeado(ventana, mostrar_filtrar_categoria_boton, (0, 128, 0), 10)
        ventana.blit(font.render("Filtrar categoria", True, (255, 255, 255)), (mostrar_filtrar_categoria_boton.x +5, mostrar_filtrar_categoria_boton.y + 8))
        
        pintar_rectangulo_bordeado(ventana, mostrar_filtrar_combinada_boton, (0, 128, 0), 10)
        ventana.blit(font.render("Filtrar varios criterios", True, (255, 255, 255)), (mostrar_filtrar_combinada_boton.x +5, mostrar_filtrar_combinada_boton.y + 8))
        
        pintar_rectangulo_bordeado(ventana, mostrar_actualizar_datos, (0, 128, 0), 10)
        ventana.blit(font.render("Actualizar datos", True, (255, 255, 255)), (mostrar_actualizar_datos.x +5, mostrar_actualizar_datos.y + 8))

        pintar_rectangulo_bordeado(ventana, guardar_arbol_boton, (0, 128, 0), 10)
        ventana.blit(font.render("Guardar el arbol", True, (255, 255, 255)), (guardar_arbol_boton.x +5, guardar_arbol_boton.y + 8))
    
        pintar_rectangulo_bordeado(ventana, cargar_arbol_boton, (0, 128, 0), 10)
        ventana.blit(font.render("Cargar arbol", True, (255, 255, 255)), (cargar_arbol_boton.x +5, cargar_arbol_boton.y + 8))
    
    if not formulario_visible_buscar_id and not actualizar_atributos:
        dibujar_nodo_main(ventana, arbol.raiz, (screen_width // 2)+100, 150, 120,font)
    pygame.display.update() 
           
    
pygame.quit()