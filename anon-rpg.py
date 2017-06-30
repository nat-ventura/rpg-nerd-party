# 6-29-17
# nat
# first rpg

import pygame
import sys
import time
from scripts.textures import *
from scripts.globals import *
from scripts.map_engine import *


color = pygame.Color

pygame.init()

current_sec = 0
current_frame = 0
fps = 0

tiles = Tiles()
world_map = Map()


terrain = world_map.load_map("maps/map.map")



fps_font = pygame.font.SysFont("fontname", 20)

def create_window():
    # don't forget to make these not global and make a main function
    global window, window_height, window_width, window_title
    window_width, window_height = 800, 600
    window_title = "RPG"
    pygame.display.set_caption(window_title)
    window = pygame.display.set_mode((window_width, window_height), pygame.HWSURFACE|pygame.DOUBLEBUF)

def count_fps():
    #another useless global
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

#put this in a cleaner place
create_window()

running = True

#RENDER GRAPHICS

while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                Globals.camera_move = 1
            elif event.key == pygame.K_s:
                Globals.camera_move = 2
            elif event.key == pygame.K_a:
                Globals.camera_move = 3
            elif event.key == pygame.K_d:
                Globals.camera_move = 4
        
        elif event.type == pygame.KEYUP:
            Globals.camera_move = 0
    
    #LOGIC
    # he changed the added/subtracted value to 100 * delta_time
    # but that was making the map stop moving for me..
    # so for now I'm keeping it at 5
    if Globals.camera_move == 1:
        Globals.camera_y += 5
    elif Globals.camera_move == 2:
        Globals.camera_y -= 5
    elif Globals.camera_move == 3:
        Globals.camera_x += 5
    elif Globals.camera_move == 4:
        Globals.camera_x -= 5

    # sky
    for x in range(0, 800, tiles.size):
        for y in range(0, 600, tiles.size):
            window.blit(tiles.sky, (x, y))

    #terrain

    window.blit(terrain, (Globals.camera_x, Globals.camera_y))

    
    display_fps()

    pygame.display.update()

    count_fps()

pygame.quit()
sys.exit