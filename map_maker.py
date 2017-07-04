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
    world_map = Map()
    selector = make_selector(earth)
    fps = FPS_Tracker()
    brush = "grass"

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # draw default sky and earth
        # self.width and self.height for earth right now are hard coded
        new_sky = sky.make(big_window, window)        
        new_earth = earth.make(window, camera_x, camera_y, world_map)
        # looks like you're trying to add the info of each `tile`
        # to a 2d list stored in world_map.prev_tiles
        # looks like: (self.instance, (camera_x, camera_y))

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
            # if event.key == pygame.K_y:
            #     texture.png_string = "sky"
            # I'm taking this out because I think `sky` should be like absence
            # of `earth` or other terrain
            if event.key == pygame.K_u:
                brush = "earth"
            if event.key == pygame.K_i:
                brush = "water"
            if event.key == pygame.K_o:
                brush = "stone"
            if event.key == pygame.K_r:
                brush = "remove"

        # this keeps camera from continuing to move
        elif event.type == pygame.KEYUP:
            camera_x = camera_x
            camera_y = camera_y

        # selector boundaries
        if event.type == pygame.MOUSEMOTION:
            mouse_pos = pygame.mouse.get_pos()
            mouse_x = (mouse_pos[0] // 64) * 64 # hard-coding the tile size here eek
            mouse_y = (mouse_pos[1] // 64) * 64

        # selector painting
        if event.type == pygame.MOUSEBUTTONDOWN:
            done = False
            while not done:

                if brush == "remove":
                    for tile in world_map.tiles:
                        if (mouse_x - camera_x, mouse_y - camera_y) == tile[1]:
                            try:
                                world_map.tiles.remove(tile)
                                done = True
                                for tile in world_map.tiles:
                                    window.blit(earth.instance, (x + camera_x, y + camera_y))
                            except:
                                print "no tile there!"                
                
                elif brush in ["grass", "water", "stone"]:
                    earth.png_string = brush
                    for tile in world_map.tiles:
                        # if it's in the same location and of the same type
                        if brush == tile[0] and (mouse_x - camera_x, mouse_y - camera_y) == tile[1]:
                            print "that's the same type of tile"
                            done = True
                        elif brush != tile[0] and (mouse_x - camera_x, mouse_y - camera_y) == tile[1]:
                            world_map.tiles.remove(tile)
                            world_map.tiles.append([brush, tile[1]])
                            window.blit(earth.instance, (x + camera_x, y + camera_y))
                            print "tile replaced"
                            done = True
                            # something that i'm appending or blitting isn't working out...

        # # draw map
        # for x in range(0, world_map.width, world_map.size):
        #     for y in range(0, world_map.height, world_map.size):
        #         window.blit(texture.instance, (x + camera_x, y + camera_y))

        # draw highlighter
        window.blit(selector, (mouse_x, mouse_y))

        new_count = fps.count()
        new_display = fps.display(window)

        pygame.display.update()
    
    # i'm pretty sure these never get called lol
    # pygame.quit()
    # sys.exit

main()