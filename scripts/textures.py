# 6-29-17
# nat
# rpg textures

import pygame
pygame.init()

class Window(object):
    def __init__(self, width = 800, height = 600):
        self.width = width
        self.height = height
    
    def create(self, title):
        pygame.display.set_caption(title)
        window = pygame.display.set_mode((self.width, self.height), pygame.HWSURFACE|pygame.DOUBLEBUF)
        return window

class Texture(object):
    def __init__(self, png_string, size = 300):
        self.size = size
        self.png_string = png_string
        self.instance = self.load_texture("graphics/" + self.png_string + ".png", self.size)

    def load_texture(self, file, size):
        bitmap = pygame.image.load(file)
        bitmap = pygame.transform.scale(bitmap, (size, size))
        surface = pygame.Surface((size, size), pygame.HWSURFACE|pygame.SRCALPHA)
        surface.blit(bitmap, (0, 0))
        return surface

class Earth(Texture):
    def __init__(self, png_string, size = 100):
        self.size = size
        self.png_string = png_string
        self.width = 640
        self.height = 480
        self.instance = Texture.load_texture(self, "graphics/" + self.png_string + ".png", self.size)