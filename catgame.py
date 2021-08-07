import os
import sys
import pygame as pg
import time
import random
from random import randint
from objects import utilities as ut
from objects import dogowner, config as cfg

pg.init()
random.seed(time.time())

main_dir = os.path.split(os.path.abspath(__file__))[0]
data_dir = os.path.join(main_dir, "data")
print(data_dir)

screen = pg.display.set_mode(cfg.size)

def main():

    # generation of field should also be wrapped within a class
    ut.imgld.set_data_dir(data_dir)
    field, fieldrect = ut.imgld.load_image("background_field.png")
    object_stack = [(field, fieldrect, "field")]

    # generate a dummy dog owner -- for testing
    invader = dogowner.DogOwner(object_stack)
    invader.startpos(randint(1,6))
    
    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            elif event.type == pg.MOUSEBUTTONDOWN:
                 pos = pg.mouse.get_pos()
                 place_cat(pos, object_stack)

        invader.update()
                 
        pg.time.Clock().tick(cfg.fps)
        screen.fill(cfg.white)
        for obj in object_stack:
            screen.blit(obj[0], obj[1])
        pg.display.flip()

if __name__ == "__main__":
    main()
