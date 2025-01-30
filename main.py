import pygame
from enemigo import Enemigo
from torre import Torre
from menu import Menu
import time

pygame.init()

# Configuración de la pantalla
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tower Defense")

# Colores
GREEN = (34, 177, 76) # Color del area fuera del camino
BROWN = (139, 69, 19) # Color del camino
WHITE = (255, 255, 255) # Color de texto
RED = (255, 0, 0)  # Color del botón
BUTTON_COLOR = (200, 0, 0)  # Color de fondo del botón

# Definir el camino como una lista de puntos
path = [
    (100, 0), (100, 150), (200, 150), (200, 300), (400, 300), 
    (400, 450), (600, 450), (600, HEIGHT - 100), (WIDTH - 100, HEIGHT - 100), 
    (WIDTH - 100, HEIGHT)
]


# ------------------------------ CLASE JUEGO ------------------------------
class Juego:
    def __init__(self):
        self.enemigos = []
        self.torres = []
        self.dinero = 50  # Dinero inicial
        self.puntos = 0
        self.running = True
        self.clock = pygame.time.Clock()
        self.salario = 10  # Dinero ganado por cada enemigo destruido
        self.torre_precio = 50  # Precio por una torre básica
        self.max_enemigos = 10  # Número máximo de enemigos que aparecerán
        self.enemigos_destruidos = 0  # Contador de enemigos destruidos
        self.tiempo_ultimo_enemigo = time.time()  # Variable para el temporizador
        self.intervalo_entre_enemigos = 3  # Intervalo de tiempo entre la aparición de enemigos (en segundos)

    def ganar_dinero(self):
        # Cada vez que un enemigo es destruido, se gana dinero
        self.dinero += self.salario

    def crear_enemigos(self):
        if len(self.enemigos) < self.max_enemigos and time.time() - self.tiempo_ultimo_enemigo > self.intervalo_entre_enemigos:
            enemigo = Enemigo(path)
            self.enemigos.append(enemigo)
            self.tiempo_ultimo_enemigo = time.time()  # Actualizar el tiempo del último enemigo creado
            print(f"Enemigo creado: {enemigo}")  # Verificación

    def dibujar_torre(self):
        for torre in self.torres:
            torre.dibujar(screen)

    def actualizar_enemigos(self):
        for enemigo in self.enemigos[:]:
            if not enemigo.destruido:
                enemigo.mover()  # Mover al enemigo en el camino
                enemigo.dibujar(screen)  # Dibujar al enemigo en la pantalla

                for torre in self.torres:
                    for proyectil in torre.proyectiles[:]:
                        if proyectil.colision():  # Si hay colisión
                            enemigo.cambiar_color()  # Cambiar el color del enemigo
                            torre.proyectiles.remove(proyectil)  # Eliminar el proyectil de la lista
                            break  # Salir después de la colisión

            if enemigo.vida <= 0:  # Si la vida del enemigo es 0, se destruye
                enemigo.destruido = True
                self.enemigos.remove(enemigo)  # Eliminar al enemigo de la lista
                self.puntos += 10  # Sumar puntos por destruir al enemigo
                self.enemigos_destruidos += 1  # Incrementar el contador de enemigos destruidos
                self.ganar_dinero()
                self.verificar_fin_nivel()

    def verificar_fin_nivel(self):
        if self.enemigos_destruidos == self.max_enemigos:
            print("Nivel completado: Todos los enemigos han sido derrotados.")
            
            # Destruir todos los enemigos
            for enemigo in self.enemigos:
                enemigo.destruido = True
            self.enemigos = []  # Limpiar la lista de enemigos

            # Mostrar mensaje de nivel completado
            self.mostrar_mensaje_nivel_completado()

            # Terminar el juego
            self.running = False  # Esto seguirá cerrando el juego

    def mostrar_mensaje_costo_torre(self):
        font = pygame.font.SysFont("Arial", 24)
        mensaje = font.render("Colocar torres cuesta 50 monedas", True, WHITE)
        screen.blit(mensaje, (WIDTH // 2 - mensaje.get_width() // 2, HEIGHT - 40))



    def reiniciar_nivel(self):
        """Reinicia el nivel, eliminando enemigos y torres, y reseteando puntos y dinero"""
        self.enemigos = []
        self.torres = []
        self.dinero = 100  # Restablecer dinero
        self.puntos = 0
        self.enemigos_destruidos = 0  # Reiniciar contador de enemigos destruidos
        self.tiempo_ultimo_enemigo = time.time()  # Reiniciar el temporizador de enemigos

    def dibujar_boton_reiniciar(self):
        # Crear el rectángulo del botón de reiniciar, ubicado junto al de salir
        button_rect = pygame.Rect(WIDTH - 300, 10, 140, 40)
        pygame.draw.rect(screen, BUTTON_COLOR, button_rect)

        # Agregar texto al botón
        font = pygame.font.SysFont("Arial", 24)
        texto_boton = font.render("Reiniciar", True, WHITE)
        screen.blit(texto_boton, (WIDTH - 290, 15))

        return button_rect

    def verificar_click_reiniciar(self, mouse_pos):
        # Si el clic está dentro del área del botón de reiniciar
        button_rect = self.dibujar_boton_reiniciar()
        if button_rect.collidepoint(mouse_pos):
            return True
        return False        

    def mostrar_mensaje_nivel_completado(self):
        # Mostrar mensaje en la pantalla
        font = pygame.font.SysFont("Arial", 48)
        mensaje = font.render("Nivel Completado!", True, WHITE)
        screen.blit(mensaje, (WIDTH // 2 - mensaje.get_width() // 2, HEIGHT // 2 - mensaje.get_height() // 2))

        # Mostrar el mensaje por unos segundos
        pygame.display.update()
        pygame.time.wait(2000)  # Esperar 2 segundos

    def actualizar_torres(self):
        for torre in self.torres:
            torre.detectar_enemigos(self.enemigos)

    def actualizar_proyectiles(self):
        for torre in self.torres[0].proyectiles:
            if torre.colision():
                torre.enemigo.destruido = True
                self.torres[0].proyectiles.remove(torre)  # Eliminar proyectil después de la colisión
            else:
                torre.mover()
                torre.dibujar(screen)

    def mostrar_puntuacion(self):
        font = pygame.font.SysFont("Arial", 24)
        texto_puntuacion = font.render(f"Puntuación: {self.puntos}", True, WHITE)
        screen.blit(texto_puntuacion, (10, 10))

        # Mostrar el dinero
        texto_dinero = font.render(f"Dinero: {self.dinero}", True, WHITE)
        screen.blit(texto_dinero, (10, 40))

        # Mostrar los enemigos abatidos
        texto_enemigos_abatidos = font.render(f"Enemigos abatidos: {self.enemigos_destruidos}", True, WHITE)
        screen.blit(texto_enemigos_abatidos, (10, 70))

    def dibujar_boton_salir(self):
        # Crear el rectángulo del botón de salir
        button_rect = pygame.Rect(WIDTH - 150, 10, 140, 40)
        pygame.draw.rect(screen, BUTTON_COLOR, button_rect)

        # Agregar texto al botón
        font = pygame.font.SysFont("Arial", 24)
        texto_boton = font.render("Salir", True, WHITE)
        screen.blit(texto_boton, (WIDTH - 140, 15))

        return button_rect

    def verificar_click_salir(self, mouse_pos):
        # Si el clic está dentro del área del botón
        button_rect = self.dibujar_boton_salir()
        if button_rect.collidepoint(mouse_pos):
            return True
        return False

    def colocar_torre(self, pos):
        x, y = pos
        if self.dinero >= self.torre_precio:
            self.torres.append(Torre(x, y, 100))  # Agregar torre
            self.dinero -= self.torre_precio  # Descontar dinero por la torre
        else:
            print("No tienes suficiente dinero para colocar una torre.")

# ------------------------------ EJECUCIÓN DEL JUEGO ------------------------------

# Mostrar el menú
Menu.mostrar(screen)

# Crear el objeto del juego
juego = Juego()

# Bucle principal del juego
while juego.running:
    screen.fill(GREEN)  # Fondo del mapa

    # Crear enemigos
    juego.crear_enemigos()

    # Dibujar el camino
    for i in range(len(path) - 1):
        pygame.draw.line(screen, BROWN, path[i], path[i + 1], 40)

    juego.actualizar_enemigos()
    juego.dibujar_torre()
    juego.actualizar_torres()  
    juego.mostrar_puntuacion()
    juego.mostrar_mensaje_costo_torre()

    # Botones
    juego.dibujar_boton_salir()
    juego.dibujar_boton_reiniciar()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            juego.running = False
        # Verificar si el clic está sobre el botón de salir
        if event.type == pygame.MOUSEBUTTONDOWN:
            if juego.verificar_click_salir(event.pos):
                juego.running = False  # Terminar el juego si se hace clic en el botón de salir
            elif juego.verificar_click_reiniciar(event.pos):
                juego.reiniciar_nivel()  # Reiniciar el nivel si se hace clic en el botón de reiniciar
            else:
                # Colocar una torre en la posición del clic solo si no es sobre un botón
                juego.colocar_torre(event.pos)


    pygame.display.update()
    juego.clock.tick(30)  # Limitar el FPS

pygame.quit()
