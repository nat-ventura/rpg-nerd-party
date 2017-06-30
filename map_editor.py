# 6-30-17

import pygame, sys, math
from scripts.textures import *

def export_map(file):
    map_data = ""

    # get map dimensions
    max_x = 0
    max_y = 0

    for t in tile_data:
        if t[0] > max_x:
            max_x = t[0]
        if t[1] > max_y:
            max_y = t[1]

    # save map tiles
    for tile in tile_data:
        map_data = map_data + str(int(tile[0] / tiles.size)) + "," + str(int(tile[1] / tiles.size)) + ":" + tile[2] + "-"


    # save map dimensions
    map_data = map_data + str(int(max_x / tiles.size)) + "," + str(int(max_y / tiles.size))


    #write map file
    map_file = open(file, "w")
    map_file.write(map_data)



color = pygame.Color

window = pygame.display.set_mode((1280, 720), pygame.HWSURFACE)
pygame.display.set_caption("Map Editor")
clock = pygame.time.Clock()

tiles = Tiles()

txt_font = pygame.font.SysFont("fontname", 20)

mouse_position = 0
mouse_x, mouse_y = 0, 0

map_width, map_height = 100 * tiles.size

selector = pygame.Surface((tiles.size, tiles.size), pygame.HWSURFACE|pygame.SRCALPHA)
selector.fill(color("blue"))
tile_data = []

camera_x, camera_y = 0, 0
camera_move = 0

brush = 1

#initialize default map

for x in range(0, map_height, tiles.size):
    for y in range(0, map_height, tiles.size):
        tile_data.append([x, y, "1"])


running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                camera_move = 1
            elif event.key == pygame.K_s:
                camera_move = 2
            elif event.key == pygame.K_a:
                camera_move = 3
            elif event.key == pygame.K_d:
                camera_move = 4
            elif event.key == pygame.KEYUP:
                camera_move = 0
        
        #brushes
        if event.key == pygame.K_F4:
            brush = "r"
        if event.key == pygame.K_F1:
            brush = input("brush tag: ")

        # save map
        if event.key == pygame.K_F11:
            name = input("map name: ")
            export_map(name + ".map")
            print "map saved successfully!"


        if event.type == pygame.MOUSEMOTION:
            mouse_position = pygame.mouse.get_pos()
            mouse_x = math.floor(mouse_pos[0] / tiles.size) * tiles.size
            mouse_y = math.floor(mouse_position[1] / tiles.size) * tiles.size

        if event.type == pygame.MOUSEBUTTONDOWN:
            tile = [mouse_x - camera_x, mouse_y - camera_y, brush] # keep this as a list, not a tuple!
            found = False
            for t in tile_data:
                if t[0] == tile[0] and t[1] == tile[1]:
                    found = True
                    break
            
            if not found:
                if not brush == "r":
                    tile_data.append(tile)
            else:
                if brush == "r":
                    # remove tile
                    for t in tile_data:
                        if t[0] == tile[0] and t[1] == tile[1]:
                            tile_data.remove(t)
                            print "Tile removed!"

                else:
                    print "A tile is already placed here."

    # logic
    if camera_move == 1:
        camera_y += tiles.size
    elif camera_move == 2:
        camera_y -= tiles.size
    elif camera_move == 3:
        camera_x += tiles.size
    elif camera_move == 4:
        camera_x -= tiles.size

    # render graphics
    window.fill(color("black"))

    # draw map
    for tile in tile_data:
        try:
            # this tile reference will need to be fixed later
            window.blit(tiles.texture_tags[tile[2], (tile[0] + camera_x, tile[1] + camera_y)])
        except:
            pass

    # draw tile highlighter (selector)
    window.blit(selector, (mouse_x, mouse_y))



    pygame.display.update()

    clock.tick(60)

pygame.quit()
sys.exit()