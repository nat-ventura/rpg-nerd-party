# 6-29-17
# nat
# first rpg

import pygame, sys, time
from scripts.textures import *
from scripts.globals import *
from scripts.map_engine import *

pygame.init()

def create_window(window_width, window_height):
    pygame.display.set_caption("RPG")
    window = pygame.display.set_mode((window_width, window_height), pygame.HWSURFACE|pygame.DOUBLEBUF)
    return window

def count_fps(current_sec, current_frame, fps, delta_time):
    if current_sec == time.strftime("%s"):
        current_frame += 1
    else:
        fps = current_frame
        current_frame = 0
        current_sec = time.strftime("%s")
    return (current_sec, current_frame)

def display_fps(fps):
    fps_overlay = fps_font.render(fps, True, color("goldenrod"))
    window.blit(fps_overlay, (0, 0))

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

def main():
    color = pygame.Color
    current_sec = 0
    current_frame = 0
    fps = 0
    tiles = Tiles()
    world_map = Map()
    terrain = world_map.load_map("maps/map.map", tiles)
    fps_font = pygame.font.SysFont("fontname", 20)

    window = create_window(800, 600)
    current_sec, current_frame = count_fps(current_sec, current_frame, fps, delta_time)
    fps_display = display_fps(fps)

main()