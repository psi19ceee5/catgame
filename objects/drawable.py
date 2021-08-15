import pygame as pg
from objects import utilities as ut
from objects import config as cfg
import time

class Drawable:

    colorkey = None
    draw = False
    despawned = False
    pos = (0,0)
    hscale = 1
    vsale = 1
    
    def __init__(self, object_stack):
        # import image and copy of it for reference
        self.image, self.rect = ut.imgld.load_image(self.imagefile, self.colorkey)
        self.origimage, self.origrect = ut.imgld.load_image(self.imagefile, self.colorkey)
        # append image and rect to object stack
        object_stack.append(self)
        # save timestamp of object creation
        self.timestamp = time.time()
        self.inittime = self.timestamp
        # calc fullscreen reslution
        self.hscale = cfg.dwidth / cfg.width
        self.vscale = cfg.dheight / cfg.height
        width_scaled = round(self.image.get_width() * self.hscale)
        height_scaled = round(self.image.get_height() * self.vscale)
        self.origimage_scaled = pg.transform.scale(self.origimage, (width_scaled, height_scaled))
        self.origrect_scaled = self.origimage_scaled.get_rect()
        

    def setpos_init_leftbottom(self, xpos, ypos):
        self.rect.bottom = ypos
        self.rect.left = xpos
        self.origrect.bottom = ypos
        self.origrect.left = xpos
        self.pos = (xpos, ypos)

    def setpos_leftbottom(self, xpos, ypos):
        self.rect.bottom = ypos
        self.rect.left = xpos
        self.pos = (xpos, ypos)

    def adapt_fullscreen(self) :
        if cfg.fullscreen == True :
            self.image = self.origimage_scaled
            self.rect = self.origrect_scaled
            self.pos = self.pos[0] * self.hscale, self.pos[1] * self.vscale
        else :
            self.image = self.origimage
            self.rect = self.origrect
            self.pos = self.pos[0] / self.hscale, self.pos[1] / self.vscale

    def check_drawing(self) :
        # to be overridden by children
        pass
            
    def update(self, object_stack) :
        self.check_drawing()
        if self.despawned :
            object_stack.remove(self)
