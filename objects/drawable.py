from objects import utilities as ut
from objects import config as cfg
import time

class Drawable:

    colorkey = None
    draw = False
    
    def __init__(self, object_stack):
        self.image, self.rect = ut.imgld.load_image(self.imagefile, self.colorkey)
        self.origimage, self.origrect = ut.imgld.load_image(self.imagefile, self.colorkey)
        object_stack.append(self)
        self.timestamp = time.time()
        self.inittime = self.timestamp

    def setpos_init_leftbottom(self, xpos, ypos):
        self.rect.bottom = ypos
        self.rect.left = xpos
        self.origrect.bottom = ypos
        self.origrect.left = xpos

    def setpos_leftbottom(self, xpos, ypos):
        self.rect.bottom = ypos
        self.rect.left = xpos

    def update(self):
        pass
