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
    sky = Sky("sky")
    earth = Earth("grass")
    fps = FPS_Tracker()
    world_map = Map(earth)
    selector = make_selector(earth)
    brush = "earth"

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
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
            if event.key == pygame.K_r:
                brush = "remove"
            if event.key == pygame.K_u:
                brush = "earth"
            if event.key == pygame.K_i:
                brush = "water"
            if event.key == pygame.K_o:
                brush = "stone"

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
            current = [mouse_x - camera_x, mouse_y - camera_y, brush]

            found = False
            while not found:
                for tile in world_map.tiles:
                    if tile[0] == current[0] and tile[1] == current[1]:
                        found = True
                    if not found:
                        if brush != "remove":
                            world_map.tiles.append(tile)
                else:
                    if brush == "remove":
                        for tile in world_map.tiles:
                            if tile[0] == current[0] and tile[1] == current[1]:
                                world_map.tiles.remove(tile)
                                print "tile removed"
                    else:
                        print("a tile is already here...")


            # for tile in world_map.tiles:
            #     # if it's the same location
            #     if tile[0] == current[0] and tile[1] == current[1]:
            #         if brush == "remove":
            #             world_map.tiles.remove(tile)
            #             print "tile removed"
                        
            #         else:
            #             world_map.tiles.append(current)
            #             print "tile added"
            #     else:
            #         print "A tile is already here.."
            
        # draw default sky
        new_sky = sky.make_sky(big_window, window)        

        #draw map
        for tile in world_map.tiles:
            window.blit(earth.instance, (tile[0] + camera_x, tile[1] + camera_y))

        # draw highlighter
        window.blit(selector, (mouse_x, mouse_y))

        new_count = fps.count()
        new_display = fps.display(window)

        pygame.display.update()
    
    # i'm pretty sure these never get called lol
    # pygame.quit()
    # sys.exit

main()