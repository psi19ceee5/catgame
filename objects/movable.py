from objects import utilities as ut
from objects import config as cfg
from objects import drawable
import time

class Movable(drawable.Drawable):

    def velocity_control(self):
        if time.time() - self.timestamp > 1./self.speed :
            self.timestamp = time.time()
            return True
        else:
            return False
