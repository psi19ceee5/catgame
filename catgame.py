import os
import sys
import pygame as pg
import time
import random
from random import randint
from objects import utilities as ut
from objects import dogowner
from objects import uglycat
from objects import config as cfg
from objects import field as fld
from objects import objectstack as objs

pg.init()
random.seed(time.time())

main_dir = os.path.split(os.path.abspath(__file__))[0]
data_dir = os.path.join(main_dir, "data")

screen = pg.display.set_mode(cfg.size)

def main():

    # generation of field should also be wrapped within a class
    ut.imgld.set_data_dir(data_dir)
    object_stack = objs.Objectstack()
    field = fld.Field(object_stack)

    # generate a dummy dog owner -- for testing
    invader = dogowner.DogOwner(object_stack)
    invader.set_init_vfield(randint(0,5))
    
    running = True
    while running:
        for event in pg.event.get() :
            if event.type == pg.QUIT :
                sys.exit()
            elif event.type == pg.MOUSEBUTTONDOWN :
                pos = pg.mouse.get_pos()
                if object_stack.isInField(pos) :
                    cat = uglycat.UglyCat(object_stack)
                    cat.setpos(pos, field, object_stack)
            elif event.type == pg.KEYDOWN and event.key == pg.K_f :
                if screen.get_flags() and cfg.fullscreen:
                    pg.display.set_mode(cfg.size)
#                   pg.display.toggle_fullscreen()
                    cfg.fullscreen = False
                    object_stack.adapt_fullscreen()
                    time.sleep(0.1)
                else :
                    pg.display.set_mode((cfg.display_size), pg.NOFRAME)
#                    pg.display.toggle_fullscreen()
                    cfg.fullscreen = True
                    object_stack.adapt_fullscreen()
                    time.sleep(0.1)

        object_stack.update()
                 
        pg.time.Clock().tick(cfg.fps)
        screen.fill(cfg.white)
        object_stack.blit(screen)
        pg.display.flip()

    pg.quit()
    sys.exit()

if __name__ == "__main__":
    main()
