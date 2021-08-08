import pygame as pg
from objects import utilities as ut
from objects import config as cfg
from objects import drawable
import time
import math

class Movable(drawable.Drawable):

    trans_speed = 0
    cont_wiggle_amplitude = 0
    cont_wiggle_freq = 0
    
    def pixels_to_move(self) :
        npix = (time.time() - self.timestamp)*self.trans_speed
        if npix > 1 :
            self.timestamp = time.time()
            return npix
        else:
            return 0

    def continuous_wiggle(self) :
        vscale = round(self.origimage.get_height()*(1+self.cont_wiggle_amplitude*math.sin(2*math.pi*self.cont_wiggle_freq*(time.time() - self.inittime))))
        hscale = round(self.origimage.get_width()*(1-self.cont_wiggle_amplitude*0.5*math.sin(2*math.pi*self.cont_wiggle_freq*(time.time() - self.inittime))))
        self.image = pg.transform.scale(self.origimage, (hscale, vscale))

        voffset = self.origimage.get_height() - self.image.get_height() 
        hoffset = round(0.5*(self.origimage.get_width() - self.image.get_width()))
        self.setpos_leftbottom(self.origrect.left + hoffset, self.origrect.bottom + voffset)

    def update(self):
        npix = self.pixels_to_move()
        if npix > 0:
            self.rect.move_ip((-1*npix, 0))

        self.continuous_wiggle()
