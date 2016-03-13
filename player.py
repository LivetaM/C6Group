#Jonthan Salmon

#This class manages the player, it is responsible for controling the logic behind the movement,
#checking if the car is located on a grass tile and rotation of the car

import math
import pygame
import timer
from image_loader import load_image

GRASS_SPEED = 0.715
GRASS_GREEN = 100
CENTER_X = -1
CENTER_Y = -1
playerspawn = timer.Finish()

#Rotate car around the center point
def rot_center(image, rect, angle):
        """rotate an image while keeping its center"""
        rot_image = pygame.transform.rotate(image, angle)
        rot_rect = rot_image.get_rect(center=rect.center)
        return rot_image,rot_rect

def findspawn():
    x = 300
    y = 800
    return x, y

#define car as Player.
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image('player.png')
        self.rect = self.image.get_rect()
        self.image_orig = self.image
        self.screen = pygame.display.get_surface()
        self.area = self.screen.get_rect()
        CENTER_X =  int(pygame.display.Info().current_w /2)
        CENTER_Y =  int(pygame.display.Info().current_h /2)
        self.x = CENTER_X
        self.y = CENTER_Y
        self.rect.topleft = self.x, self.y
        self.x, self.y = findspawn()
        self.dir = 0
        self.speed = 0.0
        self.maxspeed = 21.5
        self.minspeed = -1.85
        self.acceleration = 0.095
        self.deacceleration = 0.12
        self.softening = 0.04
        self.steering = 1.60

#If the car is on grass, decrease speed and emit tracks.
    def grass(self, value):
        if value > GRASS_GREEN:
            if self.speed - self.deacceleration > GRASS_SPEED * 2:
                self.speed = self.speed - self.deacceleration * 2

#If car is moving offset the movement by the softening amount in order to
#eventually bring it to a standstill if no other forces are applied
    def soften(self):
            if self.speed > 0:
                self.speed -= self.softening
            if self.speed < 0:
                self.speed += self.softening

#Accelerate the vehicle
    def accelerate(self):
        if self.speed < self.maxspeed:
            self.speed = self.speed + self.acceleration


#Deaccelerate the car
    def deaccelerate(self):
        if self.speed > self.minspeed:
            self.speed = self.speed - self.deacceleration

#Steer the car left
    def steerleft(self):
        self.dir = self.dir+self.steering
        if self.dir > 360:
            self.dir = 0
        self.image, self.rect = rot_center(self.image_orig, self.rect, self.dir)

#Steer the car right
    def steerright(self):
        self.dir = self.dir-self.steering
        if self.dir < 0:
            self.dir = 360
        self.image, self.rect = rot_center(self.image_orig, self.rect, self.dir)

#Updates the car's position based off of current speed
    def update(self, last_x, last_y):
        self.x = self.x + self.speed * math.cos(math.radians(270-self.dir))
        self.y = self.y + self.speed * math.sin(math.radians(270-self.dir))



