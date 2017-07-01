# 6-29-17
# nat
# rpg textures

import pygame
from operator import *
pygame.init()

class Window(object):
    def __init__(self, width = 800, height = 600):
        self.width = width
        self.height = height
    
    def create(self, title):
        pygame.display.set_caption(title)
        window = pygame.display.set_mode((self.width, self.height), pygame.HWSURFACE|pygame.DOUBLEBUF)
        return window

class Map(object):
    def __init__(self):
        self.prev_tiles = [[0,(0,0)],[0,(0,0)]]
        self.new_tiles = [[]]
        self.width = 400
        self.height = 400
        self.size = 32

    def __getitem__(self, key):
        return self.prev_tiles[key]

class Texture(object):
    def __init__(self, png_string, size = 32):
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
    def __init__(self, size = 32):
        self.size = size
        self.width = 640
        self.height = 480
        self.instance = Texture.load_texture(self, "graphics/grass.png", self.size)
    
    def make(self, window, camera_x, camera_y, world_map):
        for x in range(0, self.width, self.size):
            for y in range(0, self.height, self.size):
                window.blit(self.instance, (x + camera_x, y + camera_y))
                tile = self.instance, (x + camera_x, y + camera_y)
                world_map.prev_tiles.append(tile)

class Sky(Texture):
    def __init__(self, size = 300):
        self.size = size
        self.instance = Texture.load_texture(self, "graphics/sky.png", self.size)

    def make(self, big_window, window):
        for x in range(0, big_window.width, self.size):
            for y in range(0, big_window.height, self.size):
                window.blit(self.instance, (x, y))