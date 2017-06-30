# 6-29-17
# nat
# fps tracker class

import pygame
pygame.init()

class FPS_Tracker(object):
    def __init__(self, sec = 0, frame = 0):
        self.sec = sec
        self.frame = frame
        self.font = pygame.font.SysFont("fontname", 20)

    def count_fps(self):
        if self.sec == time.strftime("%s"):
            self.frame += 1
        else:
            self.fps = self.frame
            self.frame = 0
            self.sec = time.strftime("%s")
        return (self.sec, self.frame)

    def display_fps(self, window):
        self.overlay = self.font.render(str(self.fps), True, pygame.Color("goldenrod"))
        window.blit(self.overlay, (0, 0))