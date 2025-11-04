
from pico2d import load_image

import game_world
import game_framework


class Bird:
    image = None
    def __init__(self, x=50, y=50):
        self.x = x
        self.y = y
        self.width = 183
        self.height = 168
        if Bird.image == None:
            Bird.image = load_image('bird_animation.png')


    def draw(self):
        Bird.image.clip_draw(0, 0, self.width, self.height, self.x, self.y)
    def update(self):
        pass