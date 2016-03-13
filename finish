from image_loader import load_image
import pygame
from pygame.locals import *


NOTE_HALF_X = 212
NOTE_HALF_Y = 112

#This is the popup box that shows when the timer on the main class hit's 0
#the positioning for the alert is static as of now and changes in screen resolution
#is a problem
class Alert(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image('timeout.png')
        self.rect = self.image.get_rect()
        self.x =  int(pygame.display.Info().current_w /2) - NOTE_HALF_X
        self.y =  int(pygame.display.Info().current_h /3) - NOTE_HALF_Y
        self.rect.topleft = self.x, self.y
