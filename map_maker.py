# 6-30-17
# nat
# map maker

import pygame, sys, math, pickle
from scripts.textures import *
from scripts.fps_tracker import *

def make_selector(earth):
    selector = pygame.Surface((earth.size, earth.size), pygame.HWSURFACE|pygame.SRCALPHA)
    selector.fill(pygame.Color("blue"))
    return selector

def main():
    camera_x, camera_y = 0, 0
    big_window = Window(1280, 720)
    window = big_window.create("Map Maker")
    sky = Sky()
    earth = Earth()
    fps = FPS_Tracker()
    world_map = Map()
    selector = make_selector(earth)
    texture = Texture("sky")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # draw default sky and earth
        new_sky = sky.make(big_window, window)        
        new_earth = earth.make(window, camera_x, camera_y, world_map)

        # camera movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                camera_y += 10
            elif event.key == pygame.K_s:
                camera_y -= 10
            elif event.key == pygame.K_a:
                camera_x += 10
            elif event.key == pygame.K_d:
                camera_x -= 10
        
            # brushes
            if event.key == pygame.K_y:
                texture.png_string = "sky"
            if event.key == pygame.K_u:
                texture.png_string = "earth"
            if event.key == pygame.K_i:
                texture.png_string = "water"
            if event.key == pygame.K_o:
                texture.png_string = "stone"

        elif event.type == pygame.KEYUP:
            camera_x = camera_x
            camera_y = camera_y

        # selector boundaries
        if event.type == pygame.MOUSEMOTION:
            mouse_pos = pygame.mouse.get_pos()
            mouse_x = (mouse_pos[0] // earth.size) * earth.size
            mouse_y = (mouse_pos[1] // earth.size) * earth.size

        # selector painting
        if event.type == pygame.MOUSEBUTTONDOWN:
            current = [texture.instance, (mouse_x - camera_x, mouse_y - camera_y)]
            done = False
            while not done:
                for i in range(len(world_map.prev_tiles)):
                    # if it's in the same location and of the same type
                    if current != world_map.prev_tiles[i]:
                        world_map.new_tiles.append(current)
                        print "tile removed"
                    else:
                        world_map.new_tiles.append(world_map.prev_tiles[i])
                        print "that's the same type of tile"
                    world_map.prev_tiles = world_map.new_tiles
                    done = True

        # draw map
        for x in range(0, world_map.width, world_map.size):
            for y in range(0, world_map.height, world_map.size):
                window.blit(texture.instance, (x + camera_x, y + camera_y))

        # draw highlighter
        window.blit(selector, (mouse_x, mouse_y))

        new_count = fps.count()
        new_display = fps.display(window)

        pygame.display.update()
    
    # i'm pretty sure these never get called lol
    # pygame.quit()
    # sys.exit

main()