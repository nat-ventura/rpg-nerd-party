# 6-30-17
# nat
# map maker

import pygame, sys, math
from scripts.textures import *

def create_window(window_width, window_height):
    pygame.display.set_caption("Map Maker")
    window = pygame.display.set_mode((window_width, window_height), pygame.HWSURFACE|pygame.DOUBLEBUF)
    return window