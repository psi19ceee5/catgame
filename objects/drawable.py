import pygame as pg
from objects import utilities as ut
from objects import config as cfg
import time

class Drawable:

    colorkey = None
    draw = False
    despawned = False
    pos = (0,0)
    
    def __init__(self, object_stack):
        # import image and copy of it for reference
        self.image, self.rect = ut.imgld.load_image(self.imagefile, self.colorkey)
        self.origimage, self.origrect = ut.imgld.load_image(self.imagefile, self.colorkey)
        # append image and rect to object stack
        object_stack.append(self)
        # save timestamp of object creation
        self.timestamp = time.time()
        self.inittime = self.timestamp

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
            hscale = round(self.image.get_width() * (cfg.dwidth / cfg.width))
            vscale = round(self.image.get_height() * (cfg.dheight / cfg.height))
            self.image = pg.transform.scale(self.origimage, (hscale, vscale))
        else :
            self.image = pg.transform.scale(self.origimage, (self.origimage.get_width(), self.origimage.get_height()))

    def check_drawing(self) :
        # to be overridden by children
        pass
            
    def update(self, object_stack) :
        self.check_drawing()
        if self.despawned :
            object_stack.remove(self)
