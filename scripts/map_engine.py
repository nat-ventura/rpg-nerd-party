# 6-30-2017
# nat
# map engine


import pygame
from scripts.textures import *

class Map(object):
    def __init__(self):
        pass

    def add_tile(self, tile, pos, add):
        add.blit(tile, pos[0] * tile.size, pos[1] * tile.size)

    def load_map(self, file, tiles):
        map_file = open(file, 'r')
        map_data = map_file.read()

        # read tile data
        map_data = map_data.split("-") # split into list of tiles
        map_size = map_data[len(map_data) - 1] # get map dimensions
        map_data.remove(map_size)
        map_size = map_size.split(",")
        map_size[0] = int(map_size[0]) * tiles.size
        map_size[1] = int(map_size[1]) * tiles.size

        tiles = []

        for tiles in range(len(map_data)):
            map_data[tile] = map_data[tile].replace("\n", "")
            tiles.append(map_data[tile].split(":")) # splits position from texture

        for tile in tiles:
            tile[0] = tile[0].split(",") # split pos into list
            post = tile[0]
            for p in pos:
                pos[pos.index(p)] = int(p)
            
            tiles[tiles.index(tile)] = (pos, tile[1]) # save to tile list

        # create terrain
        terrain = pygame.Surface(map_size, pygame.HWSURFACE)

        for tile in tiles:
            if tile[1] in tiles.texture_tags:
                Map.add_tile(tiles.texture_tags[tile], tile[0], terrain)

        return terrain