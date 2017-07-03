# 6-30-2017
# nat
# map engine

import pygame
from scripts.textures import *

    # def add_tile(self, tile, pos, add):
    #     add.blit(tile, pos[0] * tile.size, pos[1] * tile.size)

    # def load_map(self, file):
    #     map_file = open(file, 'r')
    #     self.map_data = map_file.read()

    # this should create world map dimensions
    for y in range(len(world_map.height)):
        for x in range(len(world_map.height)):
            world_map[0] = world_map[0] * world_map.size
            world_map[1] = world_map[1] * world_map.size

        for tile in tiles:
            position = tile[0]
            # oh shit i think this is how he made the tuple??
            for i in position:
                position[position.index(i)] = i
            
            tiles[tiles.index(tile)] = (position, tile[1]) # save to tile list

        terrain = pygame.Surface(map_size, pygame.HWSURFACE)

        for tile in tiles:
            if tile[1] in tiles.texture_tags:
                Map.add_tile(tiles.texture_tags[tile], tile[0], terrain)

        return terrain

        # read tile data
        # map_data = map_data.split("-") # split into list of tiles
        # map_size = map_data[len(map_data) - 1] # get map dimensions
        # map_data.remove(map_size)
        # map_size = map_size.split(",")
        # map_size[0] = int(map_size[0]) * tiles.size
        # map_size[1] = int(map_size[1]) * tiles.size

        # for tiles in range(len(map_data)):
        #     map_data[tile] = map_data[tile].replace("\n", "")
        #     tiles.append(map_data[tile].split(":")) # splits position from texture



        # create terrain
        

