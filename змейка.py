import random as r
import pygame as pg
import time

if __name__ == '__main__':
    pg.init()

    # разрешение экрана
    infoObject = pg.display.Info()
    wight_screen = infoObject.current_w
    height_screen = infoObject.current_h
    size_screen = (wight_screen, height_screen)

    screen = pg.display.set_mode(size_screen)

