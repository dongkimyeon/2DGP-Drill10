
from pico2d import load_image

import game_world
import game_framework


class Bird:
    image = None
    def __init__(self):
        self.x = 50
        self.y = 50
        if Bird.image == None:
            Bird.image = load_image('bird_animation.png')
        
    def draw(self):
        pass
    def update(self):
        pass