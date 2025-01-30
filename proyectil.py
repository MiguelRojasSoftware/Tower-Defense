import pygame
from enemigo import Enemigo

class Proyectil:
    def __init__(self, x, y, enemigo):
        self.x = x
        self.y = y
        self.enemigo = enemigo
        self.velocidad = 5
        self.danio = 1  # Daño que hace el proyectil

    def mover(self):
        # Mover el proyectil hacia el enemigo
        if self.enemigo.posicion[0] > self.x:
            self.x += self.velocidad
        elif self.enemigo.posicion[0] < self.x:
            self.x -= self.velocidad
        if self.enemigo.posicion[1] > self.y:
            self.y += self.velocidad
        elif self.enemigo.posicion[1] < self.y:
            self.y -= self.velocidad

    def colision(self):
        # Comprobar si el proyectil ha alcanzado al enemigo
        distancia = ((self.x - self.enemigo.posicion[0]) ** 2 + (self.y - self.enemigo.posicion[1]) ** 2) ** 0.5
        if distancia < 10:  # Radio de colisión
            self.enemigo.recibir_dano(self.danio)  # Aplicar daño al enemigo
            return True
        return False

    def dibujar(self, screen):
        pygame.draw.circle(screen, (0, 0, 255), (int(self.x), int(self.y)), 5)
