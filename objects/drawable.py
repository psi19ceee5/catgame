from objects import utilities as ut
from objects import config as cfg
import time

class Drawable:

    colorkey = None
    
    def __init__(self, object_stack):
        self.image, self.rect = ut.imgld.load_image(self.imagefile, self.colorkey)
        object_stack.append(self)
        self.timestamp = time.time()

    def setpos_leftbottom(self, xpos, ypos):
        self.rect.bottom = ypos
        self.rect.left = xpos
    
    def update(self):
        pass
