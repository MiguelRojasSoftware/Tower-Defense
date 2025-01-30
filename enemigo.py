import pygame
import math

class Enemigo:
    def __init__(self, camino):
        self.camino = camino  # El camino por el que el enemigo se moverá
        self.posicion = self.camino[0]  # Iniciar la posición del enemigo en el primer punto del camino
        self.vida = 3  # Vida del enemigo
        self.velocidad = 2  # Velocidad de movimiento ajustada
        self.destruido = False  # Indica si el enemigo ha sido destruido
        self.color = (255, 0, 0)  # Color inicial del enemigo (rojo)
        self.indice_camino = 0  # Índice para saber en qué punto del camino está el enemigo
    
    def mover(self):
        if not self.destruido:
            if self.indice_camino < len(self.camino) - 1:
                siguiente_punto = self.camino[self.indice_camino + 1]
                direccion = (siguiente_punto[0] - self.posicion[0], siguiente_punto[1] - self.posicion[1])
                distancia = math.sqrt(direccion[0] ** 2 + direccion[1] ** 2)

                # Calcular el movimiento hacia el siguiente punto
                if distancia > self.velocidad:
                    # Moverse parcialmente hacia el siguiente punto
                    self.posicion = (self.posicion[0] + direccion[0] / distancia * self.velocidad, 
                                     self.posicion[1] + direccion[1] / distancia * self.velocidad)
                else:
                    # Llegar directamente al siguiente punto
                    self.posicion = siguiente_punto
                    self.indice_camino += 1  # Avanzar al siguiente punto en el camino

            # Si llegó al final del camino
            if self.indice_camino == len(self.camino) - 1:
                self.destruido = True  # El enemigo ha llegado al final y se destruye

    def dibujar(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.posicion[0]), int(self.posicion[1])), 10)
    
    def cambiar_color(self):
        # Cambiar color cuando el enemigo es impactado
        if self.color == (255, 0, 0):  # Si el enemigo es rojo
            self.color = (0, 255, 0)  # Cambiar a verde
        elif self.color == (0, 255, 0):  # Si el enemigo es verde
            self.color = (0, 0, 255)  # Cambiar a azul
        elif self.color == (0, 0, 255):  # Si el enemigo es azul
            self.color = (255, 0, 0)  # Cambiar de nuevo a rojo
    
    def recibir_dano(self, dano):
        """Método para recibir daño cuando es impactado por un proyectil."""
        self.vida -= dano
        if self.vida <= 0:
            self.destruido = True  # Si la vida es 0 o menor, el enemigo se destruye
