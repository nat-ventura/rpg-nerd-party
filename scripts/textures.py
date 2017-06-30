# 6-29-17
# nat
# rpg textures

import pygame

pygame.init()

class Tiles(object):
    def __init__(self):
        self.size = 32
        self.grass = self.load_texture("graphics/grass.png", self.size)
        self.stone = self.load_texture("graphics/stone.png", self.size)
        self.water = self.load_texture("graphics/water.png", self.size)
        self.sky = self.load_texture("graphics/sky.png", self.size)
        self.texture_tags = {"0" : self.grass, "1" : self.stone, "2" : self.water}

    def load_texture(self, file, size):
        bitmap = pygame.image.load(file)
        bitmap = pygame.transform.scale(bitmap, (size, size))
        surface = pygame.Surface((size, size), pygame.HWSURFACE|pygame.SRCALPHA)
        surface.blit(bitmap, (0, 0))
        return surface
