# 6-29-17
# nat
# first rpg

import pygame
import sys
import time
from scripts.textures import *
from scripts.globals import *

color = pygame.Color

pygame.init()

current_sec = 0
current_frame = 0
fps = 0

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
        if fps > 0:
            delta_time = 1 / fps

def display_fps():
    fps_overlay = fps_font.render(str(fps), True, color("goldenrod"))
    window.blit(fps_overlay, (0, 0))

#put this in a cleaner place
create_window()

running = True

#RENDER GRAPHICS
tiles = Tiles()

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


    
    


    # render simple terrain grid
    window.blit(tiles.sky, (0, 0))
    for x in range(0, 640, tiles.size):
        for y in range(0, 480, tiles.size):
            window.blit(tiles.grass, (x + Globals.camera_x, y + Globals.camera_y))

    
    display_fps()

    pygame.display.update()

    count_fps()

pygame.quit()
sys.exit