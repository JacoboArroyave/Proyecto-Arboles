import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configurar la ventana
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Checkbox con texto en Pygame")

# Definir colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Coordenadas y tamaño del checkbox
checkbox_rect = pygame.Rect(100, 100, 20, 20)
checkbox_checked = False

# Configurar la fuente y el texto
font = pygame.font.Font(None, 36)
text = font.render("Aceptar términos y condiciones", True, BLACK)


# Bucle principal del juego
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if checkbox_rect.collidepoint(event.pos):
                checkbox_checked = not checkbox_checked

    # Dibujar el checkbox y el texto
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLACK, checkbox_rect, 2)
    if checkbox_checked:
        pygame.draw.rect(screen, GREEN, checkbox_rect.inflate(-4, -4))
    screen.blit(text,(200,100))

    pygame.display.flip()

# Salir de Pygame
pygame.quit()
sys.exit()
