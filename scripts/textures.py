# 6-29-17
# nat
# rpg textures

import pygame
pygame.init()

class Texture(object):
    def __init__(self, png_string, size = 32):
        self.size = size
        self.png_string = png_string
        self.instance = self.load_texture("graphics/" + self.png_string + ".png", self.size)

#  does this even do anything omg
    # def load_texture(self, file, size):
    #     bitmap = pygame.image.load(file)
    #     bitmap = pygame.transform.scale(bitmap, (size, size))
    #     surface = pygame.Surface((size, size), pygame.HWSURFACE|pygame.SRCALPHA)
    #     surface.blit(bitmap, (0, 0))
    #     return surface