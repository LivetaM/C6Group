#Jonthan Salmon

import os, pygame

#This class is a simple image loader to reduce code amounts required with trailing filepaths
#for instance all media is stored within /media within our projects folder structure
#entering "player.png" will automatically add /media to that filepath and return the image
#after checking the colorkey for transparency
def load_image(file, transparent = True):
    print("Loading " + file + " ..")
    fullname = os.path.join('media', file)
    image = pygame.image.load(fullname)
    if transparent == True:
        image = image.convert()
        colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image