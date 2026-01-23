from p5 import *
from time import *
from random import randrange


def preload():
    global spot_diff_img, scary_img
    global start_time, scare_delay
    spot_diff_img = load_image("spot_the_diff.png")
    scary_img = load_image("scary_face.png")
    start_time = time()
    scare_delay = randrange(5, 15)


def setup():
    size(1920, 1080)


def draw():


run()
