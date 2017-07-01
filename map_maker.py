# 6-30-17
# nat
# map maker

import pygame, sys, math, pickle
from scripts.textures import *

class Map(object):
    def __init__(self, width, height):
        earth = Earth("grass")
        self.tile_data = []

        # creates a square block of earth
        self.width, self.height = 100 * earth.size

        # creates a 2d list of map info
        for x in range(0, self.width, earth.size):
            for y in range(0, self.height, earth.size):
                self.tile_data.append([x, y, "earth"])

def make_selector(earth):
    selector = pygame.Surface((earth.size, earth.size), pygame.HWSURFACE|pygame.SRCALPHA)
    selector.fill(pygame.Color("blue"))
    return selector

def main():
    big_window = Window(1280, 720)
    window = big_window.create("Map Maker")
    mouse_position = 0
    mouse_x, mouse_y = 0, 0
    brush = 1



main()