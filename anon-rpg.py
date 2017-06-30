# 6-29-17
# nat
# first rpg

import pygame
import sys
import time
from scripts.textures import *

color = pygame.Color

pygame.init()

current_sec = 0
current_frame = 0
fps = 0

tile_size = 32

fps_font = pygame.font.SysFont("fontname", 20)

def create_window():
    global window, window_height, window_width, window_title
    window_width, window_height = 800, 600
    window_title = "RPG"
    pygame.display.set_caption(window_title)
    window = pygame.display.set_mode((window_width, window_height), pygame.HWSURFACE|pygame.DOUBLEBUF)

def count_fps():
    global current_sec, current_frame, fps, delta_time

    if current_sec == time.strftime("%s"):
        current_frame += 1
    else:
        fps = current_frame
        current_frame = 0
        current_sec = time.strftime("%s")

def display_fps():
    fps_overlay = fps_font.render(str(fps), True, color("goldenrod"))
    window.blit(fps_overlay, (0, 0))

create_window()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    #LOGIC
    count_fps()

    #RENDER GRAPHICS
    window.fill(color("red"))
    display_fps()

    # render simple terrain grid
    for x in range(0, 640, tile_size):
        for y in range(0, 480, tile_size):
            window.blit(Tiles.grass, (x, y))

    pygame.display.update()

pygame.quit()
sys.exit