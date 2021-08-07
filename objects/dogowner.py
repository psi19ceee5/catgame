from objects import utilities as ut
from objects import config as cfg

class DogOwner:

    def __init__(self, object_stack):
        self.image, self.rect = ut.imgld.load_image("dogowner.png", -1)
        self.rect.left = cfg.width
        object_stack.append((self.image, self.rect, "dogowner"))

    def startpos(self, fieldnr):
        vpos = (fieldnr + 0.7)*(cfg.height/cfg.vfields)
        self.rect.bottom = vpos

    def update(self):
        self.rect.move_ip((-1,0))
