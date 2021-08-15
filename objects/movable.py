import pygame as pg
from objects import utilities as ut
from objects import config as cfg
from objects import drawable
import time
import math

class Movable(drawable.Drawable):

    trans_speed = 0
    trans_direc = (0, 0)
    cont_wiggle_amplitude = 0
    cont_wiggle_freq = 0
    npix_stash = [0, 0]

    def __init__(self, object_stack) :
        norm = (self.trans_direc[0]**2 + self.trans_direc[1]**2)**0.5
        if norm > 0 :
            self.trans_direc = (self.trans_direc[0]/norm, self.trans_direc[1]/norm)
        super().__init__(object_stack)

    
    def pixels_to_move(self) :
        distance = (time.time() - self.timestamp)*self.trans_speed
        npix_x = distance*self.trans_direc[0] + self.npix_stash[0]
        npix_y = distance*self.trans_direc[1] + self.npix_stash[1]
        if abs(npix_x) < 1 :
            self.npix_stash[0] = npix_x
            npix_x = 0
        else :
            self.npix_stash[0] = npix_x - math.floor(npix_x)
            npix_x = math.floor(npix_x)
        if abs(npix_y) < 1 :
            self.npix_stash[1] = npix_y
            npix_y = 0
        else :
            self.npix_stash[1] = npix_y - math.floor(npix_y)
            npix_y = math.floor(npix_y)

        return npix_x, npix_y

    def move(self, npix_x=0, npix_y=0) :
        self.pos = (self.pos[0] + npix_x, self.pos[1] + npix_y)
        self.setpos_leftbottom(self.pos[0], self.pos[1])

    def continuous_wiggle(self) :
        if cfg.fullscreen == True :
            vscale = round(self.origimage_scaled.get_height()*(1+self.cont_wiggle_amplitude*math.sin(2*math.pi*self.cont_wiggle_freq*(time.time() - self.inittime))))
            hscale = round(self.origimage_scaled.get_width()*(1-self.cont_wiggle_amplitude*0.5*math.sin(2*math.pi*self.cont_wiggle_freq*(time.time() - self.inittime))))
            self.image = pg.transform.scale(self.origimage_scaled, (hscale, vscale))
        else :
            vscale = round(self.origimage.get_height()*(1+self.cont_wiggle_amplitude*math.sin(2*math.pi*self.cont_wiggle_freq*(time.time() - self.inittime))))
            hscale = round(self.origimage.get_width()*(1-self.cont_wiggle_amplitude*0.5*math.sin(2*math.pi*self.cont_wiggle_freq*(time.time() - self.inittime))))
            self.image = pg.transform.scale(self.origimage, (hscale, vscale))
        self.rect = self.image.get_rect()
        self.setpos_leftbottom(self.pos[0], self.pos[1])

    def check_drawing(self) :
        # to be overridden by children
        pass
        
    def update(self, object_stack):
        npix_x, npix_y = self.pixels_to_move()
        self.move(npix_x, npix_y)
        self.continuous_wiggle()
        self.timestamp = time.time()
        super().update(object_stack)
