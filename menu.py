import pygame

class Menu:
    @staticmethod
    def mostrar(screen):
        pygame.font.init()
        
        # Configuración de colores
        WHITE = (255, 255, 255)
        LIGHT_BLUE = (135, 206, 235)
        BUTTON_COLOR = (50, 50, 255)
        BUTTON_HOVER_COLOR = (100, 100, 255)
        
        # Configuración de fuentes
        title_font = pygame.font.SysFont("Arial", 48)
        button_font = pygame.font.SysFont("Arial", 36)
        
        # Texto del menú
        title_text = title_font.render("Menu", True, WHITE)
        start_text = button_font.render("Presiona cualquier tecla para comenzar", True, WHITE)
        exit_text = button_font.render("Esc para salir", True, WHITE)

        # Fondo degradado
        screen.fill(LIGHT_BLUE)
        
        # Dibujar el título
        screen.blit(title_text, (screen.get_width() // 2 - title_text.get_width() // 2, 50))
        
        # Dibujar los botones con bordes redondeados
        start_button_rect = pygame.Rect(screen.get_width() // 2 - 250, 200, 500, 60)
        exit_button_rect = pygame.Rect(screen.get_width() // 2 - 250, 300, 500, 60)
        
        pygame.draw.rect(screen, BUTTON_COLOR, start_button_rect, border_radius=30)
        pygame.draw.rect(screen, BUTTON_COLOR, exit_button_rect, border_radius=30)
        
        # Agregar el texto dentro de los botones
        screen.blit(start_text, (screen.get_width() // 2 - start_text.get_width() // 2, 210))
        screen.blit(exit_text, (screen.get_width() // 2 - exit_text.get_width() // 2, 310))

        # Actualizar la pantalla
        pygame.display.update()

        espera = True
        while espera:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        # Creditos
                        screen.fill((0, 0, 0))  # Fondo negro
                        name_font = pygame.font.SysFont("Arial", 48)
                        name_text = name_font.render("Miguel Rojas", True, WHITE)
                        screen.blit(name_text, (screen.get_width() // 2 - name_text.get_width() // 2, screen.get_height() // 2 - 50))

                        pygame.display.update()
                        
                        pygame.time.wait(3000)  # Esperar 3 segundos antes de cerrar el juego
                        pygame.quit()
                        quit()
                    else:
                        return  # Continuar con el juego al presionar cualquier tecla
