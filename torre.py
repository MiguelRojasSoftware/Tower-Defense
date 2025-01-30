import pygame
import math
from proyectil import Proyectil

class Torre:
    def __init__(self, x, y, rango):
        self.x = x
        self.y = y
        self.rango = rango
        self.tiempo_recarga = 1000  # Tiempo de recarga en milisegundos
        self.ultimo_disparo = pygame.time.get_ticks()  # Tiempo del último disparo
        self.proyectiles = []

    def detectar_enemigos(self, enemigos):
        for enemigo in enemigos:
            if not enemigo.destruido:
                # Calcular la distancia entre la torre y el enemigo
                distancia = math.sqrt((self.x - enemigo.posicion[0]) ** 2 + (self.y - enemigo.posicion[1]) ** 2)
                if distancia <= self.rango:  # Si el enemigo está dentro del rango
                    self.disparar(enemigo)

    def disparar(self, enemigo):
        # Verificar si ha pasado suficiente tiempo para disparar
        tiempo_actual = pygame.time.get_ticks()
        if tiempo_actual - self.ultimo_disparo >= self.tiempo_recarga:
            self.proyectiles.append(Proyectil(self.x, self.y, enemigo))
            self.ultimo_disparo = tiempo_actual

    def dibujar(self, screen):
        pygame.draw.circle(screen, (0, 255, 0), (self.x, self.y), 20)  # Dibujar la torre
        # Dibujar los proyectiles
        for proyectil in self.proyectiles:
            proyectil.mover()
            proyectil.dibujar(screen)
