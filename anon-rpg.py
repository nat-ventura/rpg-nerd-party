# 6-29-17
# nat
# first rpg

import pygame, sys, time
from scripts.textures import *
from scripts.map_engine import *
from scripts.fps_tracker import *

def create_window(window_width, window_height):
    pygame.display.set_caption("RPG")
    window = pygame.display.set_mode((window_width, window_height), pygame.HWSURFACE|pygame.DOUBLEBUF)
    return window

# def count_fps(current_sec, current_frame, fps):
#     if current_sec == time.strftime("%s"):
#         current_frame += 1
#     else:
#         fps = current_frame
#         current_frame = 0
#         current_sec = time.strftime("%s")
#     return (current_sec, current_frame)

# def display_fps(fps, fps_font, color, window):
#     fps_overlay = fps_font.render(fps, True, color("goldenrod"))
#     window.blit(fps_overlay, (0, 0))

def create_sky(window_width, window_height, sky, window):
    for x in range(0, window_width, sky.size):
        for y in range(0, window_height, sky.size):
            window.blit(sky.instance, (x, y))

# def create_terrain(window, terrain, camera_x, camera_y):
#     window.blit(terrain, (camera_x, camera_y))

def main():
    pygame.init()
    color = pygame.Color
    fps = FPS_Tracker()
    sky = Texture("sky")
    # world_map = Map()
    # terrain = world_map.load_map("maps/map.map", tiles)
    window_width, window_height = 800, 600
    camera_x, camera_y = 0, 0
    camera_move = 0
    window = create_window(window_width, window_height)
    
    # terrain!!!! = ?! "source" -- a source surface

    #RENDER GRAPHICS
    running = True
    while running:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    camera_y += 5
                elif event.key == pygame.K_s:
                    camera_y -= 5
                elif event.key == pygame.K_a:
                    camera_x += 5
                elif event.key == pygame.K_d:
                    camera_x -= 5
            elif event.type == pygame.KEYUP:
                camera_move = 0
        
        
        new_sky = create_sky(window_width, window_height, sky, window)

        new_count = fps.count()
        new_display = fps.display(window)

        pygame.display.update()

    pygame.quit()
    sys.exit

main()