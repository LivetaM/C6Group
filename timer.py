#This class controls the timing of the game, along with the spawning locations for all the items
#found within the game, it is also the hub for controlling the sorting algorithms and managing the scores

import pygame, map, SortingAlgorithms
from pygame.locals import *
from image_loader import load_image
from random import randint
import json


PENALTY_COOL = 180
FLAG_SCORE = 15
ENGINE_SCORE = 1000
WHEEL_SCORE = 200
STEERING_WHEEL_SCORE = 300
GEARBOX_SCORE = 500
BREAKPEDEL_SCORE = 250
CRASH_PENALTY = -2
HALF_TILE = 200
FULL_TILE = 400
COUNTDOWN_FULL = 7200
COUNTDOWN_EXTEND = 750
sort = SortingAlgorithms.SortAlgorithms()


#lists and dictionaries made in order to be able to store and order items when picked up.
SCORE = [ENGINE_SCORE, BREAKPEDEL_SCORE, GEARBOX_SCORE, WHEEL_SCORE, STEERING_WHEEL_SCORE]

A = {"Engine":0, "Break Pedal":0, "Gearbox":0, "Wheel":0, "Steering Wheel":0}
B = {0:"Engine", 1:"Break Pedal", 2:"Gearbox", 3:"Wheel", 4:"Steering Wheel"}

items = []
item_files = ['engine.png', 'break_peddal.png', 'gearbox.png', 'wheel.png', 'steeringwheel.png']


# This function handles loading the files in the item files list into the items, loading them as images vs filepaths
def initialize():
   for index in range(0, len(item_files)):
       items.append(load_image(item_files[index], True))

#This class is used as a single object, which moves around
#and keeps track of player score. It also manages the countdown timer.
class Finish(pygame.sprite.Sprite):

    #Initialize.
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.first = 0
        self.second = 0
        self.third = 0
        self.fourth = 0
        self.fith = 0
        self.score = 0
        self.timeleft = COUNTDOWN_FULL


#Update the timer and add the score from the sun of dictionary A.
    def update(self):
        if (self.timeleft > 0):
            self.timeleft -= 1
        self.score = sum(A.values())


#run reverse insertion sort on the dictionary A to order the data.
    def ReverseInsertionSort(self):


        Y = list(A.keys())
        X = list(A.values())
        zipped = list(zip(X,Y))

        sort.insertionSortReverse(zipped)

        X, Y = (list(t) for t in zip(*zipped))
        first = {Y[0]:X[0]}
        first = str(''.join('{} {}'.format(key, val) for key, val in first.items()))
        second = {Y[1]:X[1]}
        second = ''.join('{} {}'.format(key, val) for key, val in second.items())
        third = {Y[2]:X[2]}
        third = ''.join('{} {}'.format(key, val) for key, val in third.items())
        fourth = {Y[3]:X[3]}
        fourth = ''.join('{} {}'.format(key, val) for key, val in fourth.items())
        fith = {Y[4]:X[4]}
        fith = ''.join('{} {}'.format(key, val) for key, val in fith.items())
        self.first = first
        self.second = second
        self.third = third
        self.fourth = fourth
        self.fith = fith


#runs bubblesort on dictionary A to return the data in an ordered format.
    def bubblesort(self):

        X = list(A.keys())
        Y = list(A.values())

        zipped = list(zip(X,Y))

        sort.bubbleSort(zipped)

        Y,X = (list(t) for t in zip(*zipped))
        first = {Y[0]:X[0]}
        first = str(''.join('{} {}'.format(key, val) for key, val in first.items()))
        second = {Y[1]:X[1]}
        second = ''.join('{} {}'.format(key, val) for key, val in second.items())
        third = {Y[2]:X[2]}
        third = ''.join('{} {}'.format(key, val) for key, val in third.items())
        fourth = {Y[3]:X[3]}
        fourth = ''.join('{} {}'.format(key, val) for key, val in fourth.items())
        fith = {Y[4]:X[4]}
        fith = ''.join('{} {}'.format(key, val) for key, val in fith.items())
        self.first = first
        self.second = second
        self.third = third
        self.fourth = fourth
        self.fith = fith

    def first(self):
        return self.first

    def second(self):
        return self.second

    def third(self):
        return self.third

    def fourth(self):
        return self.fourth

    def fith(self):
        return self.fith


# Responsible for spawning the engines within the map
class Engine(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.index = 0
        self.image = items[self.index]
        self.rect = self.image.get_rect()
        self.image_orig = self.image
        self.screen = pygame.display.get_surface()
        self.area = self.screen.get_rect()
        self.x = 5
        self.y = 5
        self.penalty_cool = PENALTY_COOL
        self.rect.topleft = self.x, self.y
        self.score = 0
        self.timeleft = COUNTDOWN_FULL
        self.generate_finish()

    #Find an adequate point to spawn.
    def generate_finish(self):
        x = randint(0,24)
        y = randint(0,24)
        while (map.map_1[y][x] == 0):
            x = randint(0,24)
            y = randint(0,24)

        self.x = x * FULL_TILE + HALF_TILE
        self.y = y * FULL_TILE + HALF_TILE
        self.rect.topleft = self.x, self.y

    def returnEngineX(self):
        return self.x

    def returnEngineY(self):
        return self.y

    def claim_item(self):
        self.score += SCORE[self.index]
        collecteditem = B[self.index]
        A[collecteditem] += SCORE[self.index]

    def update(self, cam_x, cam_y):
        self.rect.topleft = self.x - cam_x, self.y - cam_y


# Responsible for spawning the wheels within the map
class Wheels(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.index = 3
        self.image = items[self.index]
        self.rect = self.image.get_rect()
        self.image_orig = self.image
        self.screen = pygame.display.get_surface()
        self.area = self.screen.get_rect()
        self.x = 5
        self.y = 5
        self.penalty_cool = PENALTY_COOL
        self.rect.topleft = self.x, self.y
        self.score = 0
        self.timeleft = COUNTDOWN_FULL
        self.generate_finish()

    #Find an adequate point to spawn.
    def generate_finish(self):
        x = randint(0,24)
        y = randint(0,24)
        while (map.map_1[y][x] == 0):
            x = randint(0,24)
            y = randint(0,24)


        self.x = x * FULL_TILE + HALF_TILE
        self.y = y * FULL_TILE + HALF_TILE
        self.rect.topleft = self.x, self.y


    def update(self, cam_x, cam_y):
        self.rect.topleft = self.x - cam_x, self.y - cam_y

    def claim_item(self):
        self.score += SCORE[self.index]
        collecteditem = B[self.index]
        A[collecteditem] += SCORE[self.index]

# Responsible for spawning the SteeringWheels within the map
class SteeringWheel(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.index = 4
        self.image = items[self.index]
        self.rect = self.image.get_rect()
        self.image_orig = self.image
        self.screen = pygame.display.get_surface()
        self.area = self.screen.get_rect()
        self.x = 5
        self.y = 5
        self.penalty_cool = PENALTY_COOL
        self.rect.topleft = self.x, self.y
        self.score = 0
        self.timeleft = COUNTDOWN_FULL
        self.generate_finish()

    #Find an adequate point to spawn.
    def generate_finish(self):
        x = randint(0,24)
        y = randint(0,24)
        while (map.map_1[y][x] == 0):
            x = randint(0,24)
            y = randint(0,24)


        self.x = x * FULL_TILE + HALF_TILE
        self.y = y * FULL_TILE + HALF_TILE
        self.rect.topleft = self.x, self.y


    def update(self, cam_x, cam_y):
        self.rect.topleft = self.x - cam_x, self.y - cam_y

    def claim_item(self):
        self.score += SCORE[self.index]
        collecteditem = B[self.index]
        A[collecteditem] += SCORE[self.index]


# Responsible for spawning the gearboxes within the map
class Gearbox(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.index = 2
        self.image = items[self.index]
        self.rect = self.image.get_rect()
        self.image_orig = self.image
        self.screen = pygame.display.get_surface()
        self.area = self.screen.get_rect()
        self.x = 5
        self.y = 5
        self.penalty_cool = PENALTY_COOL
        self.rect.topleft = self.x, self.y
        self.score = 0
        self.timeleft = COUNTDOWN_FULL
        self.generate_finish()

    #Find an adequate point to spawn.
    def generate_finish(self):
        x = randint(0,24)
        y = randint(0,24)
        while (map.map_1[y][x] == 0):
            x = randint(0,24)
            y = randint(0,24)


        self.x = x * FULL_TILE + HALF_TILE
        self.y = y * FULL_TILE + HALF_TILE
        self.rect.topleft = self.x, self.y


    def update(self, cam_x, cam_y):
        self.rect.topleft = self.x - cam_x, self.y - cam_y

    def claim_item(self):
        self.score += SCORE[self.index]
        collecteditem = B[self.index]
        A[collecteditem] += SCORE[self.index]


# Responsible for spawning the breakpedals within the map
class BreakPedal(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.index = 1
        self.image = items[self.index]
        self.rect = self.image.get_rect()
        self.image_orig = self.image
        self.screen = pygame.display.get_surface()
        self.area = self.screen.get_rect()
        self.x = 5
        self.y = 5
        self.penalty_cool = PENALTY_COOL
        self.rect.topleft = self.x, self.y
        self.score = 0
        self.timeleft = COUNTDOWN_FULL
        self.generate_finish()

    #Find an adequate point to spawn flag.
    def generate_finish(self):
        x = randint(0,24)
        y = randint(0,24)
        while (map.map_1[y][x] == 0):
            x = randint(0,24)
            y = randint(0,24)


        self.x = x * FULL_TILE + HALF_TILE
        self.y = y * FULL_TILE + HALF_TILE
        self.rect.topleft = self.x, self.y


    def update(self, cam_x, cam_y):
        self.rect.topleft = self.x - cam_x, self.y - cam_y

    def claim_item(self):
        self.score += SCORE[self.index]
        collecteditem = B[self.index]
        A[collecteditem] += SCORE[self.index]
