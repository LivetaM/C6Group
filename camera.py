#This class initializes the camera function and sets an initial x and y value
#theese values are mute as they are updated based on player location as soon as the game starts
class Camera():
    def __init__(self):
        self.x = 500
        self.y = 500

    def set_pos(self, x, y):
        self.x = x
        self.y = y
