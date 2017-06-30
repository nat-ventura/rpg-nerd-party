# 6-29-17
# nat
# rpg textures

import pygame

pygame.init()

class Tiles(object):
    def __init__(self):
    self.size = 32
    self.grass = load_texture("graphics/grass.png", size)
    self.stone = load_texture("graphics/stone.png", size)
    self.water = load_texture("graphics/water.png", size)

    def load_texture(self, file):
        bitmap = pygame.image.load(file)
        bitmap = pygame.transform.scale(bitmap, (size, size))
        surface = pygame.surface((size, size), pygame.HWSURFACE|pygame.SRCALPHA)
        surface.blit(bitmap, (0, 0))
        return surface
