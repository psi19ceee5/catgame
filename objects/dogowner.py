from objects import utilities as ut
from objects import config as cfg
import time


class DogOwner:

    speed = 1*cfg.invader_base_speed
    
    def __init__(self, object_stack):
        self.image, self.rect = ut.imgld.load_image("dogowner.png", -1)
        self.rect.left = cfg.width
        object_stack.append((self.image, self.rect, "dogowner"))
        self.timestamp = time.time()

    def startpos(self, fieldnr):
        vpos = (fieldnr + 0.7)*(cfg.height/cfg.vfields)
        self.rect.bottom = vpos

    def velocity_control(self):
        if time.time() - self.timestamp > 1./self.speed :
            self.timestamp = time.time()
            return True
        else:
            return False

    def update(self):
        if self.velocity_control() :
            self.rect.move_ip((-1, 0))
