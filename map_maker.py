# 6-30-17
# nat
# map maker

import pygame, sys, math, pickle
# from scripts.textures import *
from scripts.fps_tracker import *

class Window(object):
    def __init__(self, width = 800, height = 600):
        self.width = width
        self.height = height
    
    def create(self, title):
        pygame.display.set_caption(title)
        window = pygame.display.set_mode((self.width, self.height), pygame.HWSURFACE|pygame.DOUBLEBUF)
        return window
        
# class Map(object):
#     def __init__(self):
#         self.tiles = [[0,(0,0)]] # remember that these are going to be stored as (self.instance, (camera_x, camera_y))
#         self.width = 400
#         self.height = 400
#         self.size = 32

#     def load_map(self, file, texture):
#         saved_map = open(file, 'r')
#         self.tiles = saved_map.read()

#         # this should create world map dimensions
#         # for i in range(len(self.tiles):
#         #     for j in range(len(self.tiles[i])):
#         #         world_map[i][j] = world_map[i][j] * texture.size

#     # def __getitem__(self, key):
#     #     return self.tiles[key]

class Texture(object):
    def __init__(self, png_string, size = 32):
        self.size = size
        self.png_string = png_string
        self.instance = self.load_texture("graphics/" + self.png_string + ".png", self.size)

    def load_texture(self, file, size):
        bitmap = pygame.image.load(file)
        bitmap = pygame.transform.scale(bitmap, (size, size))
        surface = pygame.Surface((size, size), pygame.HWSURFACE|pygame.SRCALPHA)
        surface.blit(bitmap, (0, 0))
        return surface

class Earth(Texture):
    def __init__(self):
        self.size = 32
        self.width = 640
        self.height = 480
        self.tiles = []
        self.png_string = "grass"
        self.instance = Texture.load_texture(self, "graphics/" + self.png_string + ".png", self.size)
    
    def make(self, window, camera_x, camera_y):
        for x in range(0, self.width, self.size):
            for y in range(0, self.height, self.size):
                window.blit(self.instance, (x + camera_x, y + camera_y))
                tile = self.png_string, (x + camera_x, y + camera_y)
                self.tiles.append(tile)

class Sky(Texture):
    def __init__(self, size = 300):
        self.size = size
        self.instance = Texture.load_texture(self, "graphics/sky.png", self.size)

    def make(self, big_window, window):
        for x in range(0, big_window.width, self.size):
            for y in range(0, big_window.height, self.size):
                window.blit(self.instance, (x, y))

def make_selector(earth):
    selector = pygame.Surface((earth.size, earth.size), pygame.HWSURFACE|pygame.SRCALPHA)
    selector.fill(pygame.Color("blue"))
    return selector

def main():
    camera_x, camera_y = 0, 0
    mouse_x, mouse_y = 0, 0
    big_window = Window(1280, 720)
    window = big_window.create("Map Maker")
    sky = Sky()
    earth = Earth()
    selector = make_selector(earth)
    fps = FPS_Tracker()
    brush = "stone"

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # draw default sky and earth
        # self.width and self.height for earth right now are hard coded
        new_sky = sky.make(big_window, window)        
        earth.make(window, camera_x, camera_y)
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
            if event.key == pygame.K_r:
                brush = "remove"
            if event.key == pygame.K_u:
                brush = "grass"
            if event.key == pygame.K_i:
                brush = "water"
            if event.key == pygame.K_o:
                brush = "stone"
            

        # this keeps camera from continuing to move
        elif event.type == pygame.KEYUP:
            camera_x = camera_x
            camera_y = camera_y

        # selector boundaries
        if event.type == pygame.MOUSEMOTION:
            mouse_pos = pygame.mouse.get_pos()
            mouse_x = (mouse_pos[0] // 32) * 32 # hard-coding the tile size here eek
            mouse_y = (mouse_pos[1] // 32) * 32

        # selector painting
        if event.type == pygame.MOUSEBUTTONDOWN:
            # done = False
            # while not done:
                # if brush == "remove":
                #     for tile in world_map.tiles:
                #         if (mouse_x - camera_x, mouse_y - camera_y) == tile[1]:
                #             try:
                #                 world_map.tiles.remove(tile)
                #                 done = True
                #                 for tile in world_map.tiles:
                #                     window.blit(earth.instance, (x + camera_x, y + camera_y))
                #             except:
                #                 print "no tile there!"                
                
                if brush in ["grass", "water", "stone"]:
                    earth.png_string = brush
                    # done = True
                    for tile in earth.tiles:
                        # if it's in the same location and of the same type
                        if brush != "stone": #tile[0] and (mouse_x - camera_x, mouse_y - camera_y) == tile[1]:
                            print "nooooooo" #"that's the same type of tile"
                            # done = True
                        elif brush == "stone": #!= tile[0] and (mouse_x - camera_x, mouse_y - camera_y) == tile[1]:
                            earth.tiles.remove(tile)
                            earth.tiles.append([brush, tile[1]])
                            # window.blit(earth.instance, (mouse_x + camera_x, mouse_y + camera_y))
                            print "tile replaced"
                            # done = True
                # #             # something that i'm appending or blitting isn't working out...

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