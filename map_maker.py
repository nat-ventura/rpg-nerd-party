# 6-30-17
# nat
# map maker

import pygame, sys, math, pickle
from scripts.textures import *

def make_selector(earth):
    selector = pygame.Surface((earth.size, earth.size), pygame.HWSURFACE|pygame.SRCALPHA)
    selector.fill(pygame.Color("blue"))
    return selector

def main():
    big_window = Window(1280, 720)
    window = big_window.create("Map Maker")
    earth = Earth("grass")
    world_map = Map()

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

        elif event.type == pygame.KEYUP:
            camera_x = camera_x
            camera_y = camera_y

        # brushes
        if event.key == pygame.K_b:
            brush = "r"
        if event.key == pygame.K_t:
            brush = raw_input("brush tag: ")

        # selector boundaries
        if event.type == pygame.MOUSEMOTION:
            mouse_pos = pygame.mouse.get_pos()
            mouse_x = (mouse_pos[0] // earth.size) * earth.size
            mouse_y = (mouse_pos[1] // earth.size) * earth.size

        # selector painting
        if event.type == pygame.MOUSEBUTTONDOWN:
            current = [mouse_x - camera_x, mouse_y - camera_y, brush]
            done = False
            while not done:
                for tile in world_map.tiles:
                    # if it's the same location
                    if tile[0] == current[0] and tile[1] == current[1]:
                        if brush == "r":
                            world_map.tiles.remove(tile)
                            print "tile removed"
                            done = True
                        else:
                            tiles.append(current)
                            done = True
        
        # draw default sky.. maybe make this a method later too
        default_sky = make_sky(big_window.width, big_window.height, sky, window)        

        #draw map
        for tile in world_map.tiles:
            try:
                window.blit(tile[2], tile[0] + camera_x, tile[1] + camera_y)
            except:
                pass

        # draw highlighter
        window.blit(selector, (mouse_x, mouse_y))

        new_count = fps.count()
        new_display = fps.display(window)

        pygame.display.update()
    
    # i'm pretty sure these never get called lol
    # pygame.quit()
    # sys.exit

main()



main()