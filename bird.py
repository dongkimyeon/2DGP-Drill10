from pico2d import load_image, get_time, load_font

import game_world
import game_framework
import random


PIXEL_PER_METER = (1.0 / 0.01)

FLY_SPEED_KMPH = 30.0 # 새 이동속도
FLY_SPEED_MPM = (FLY_SPEED_KMPH * 1000.0 / 60.0)
FLY_SPEED_MPS = (FLY_SPEED_MPM / 60.0)
FLY_SPEED_PPS = (FLY_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.1 # 날개짓 속도
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 14

#제출용
class Bird:
    image = None
    def __init__(self, x = 400, y = 300):
        if Bird.image == None:
            Bird.image = load_image('bird_animation.png')
        self.x, self.y = x, y
        self.frame = 0
        self.face_dir = 1
        self.dir = 1
        self.width = 183
        self.height = 168
        self.scale = 0.4

    def update(self):
        self.x += self.dir * FLY_SPEED_PPS * game_framework.frame_time
        if self.x < 0:
            self.dir = 1
            self.face_dir = 1
        elif self.x > 1600:
            self.dir = -1
            self.face_dir = -1

        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 14

    def draw(self):
        if self.face_dir == 1:
            self.image.clip_draw((int(self.frame) % 5) * self.width, 337 - (int(self.frame) // 5) * self.height, self.width, self.height, self.x, self.y, self.scale * self.width, self.scale * self.height)
        else:
            self.image.clip_composite_draw((int(self.frame) % 5) * self.width, 337 - (int(self.frame) // 5) * self.height, self.width, self.height, 0, 'h', self.x, self.y, self.scale * self.width, self.scale * self.height)