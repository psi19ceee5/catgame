from objects import config as cfg
from objects import movable

class DogOwner(movable.Movable):
    
    trans_speed = 1*cfg.invader_base_speed
    trans_direc = (-1, 0)
    cont_wiggle_amplitude = 0.1
    cont_wiggle_freq = 1
    imagefile = "dogowner.png"
    tag = "dogowner"
    colorkey = -1
    
    def set_init_vfield(self, fieldnr):
        vpos = (fieldnr + 0.8)*(cfg.height/cfg.vfields)
        super().setpos_init_leftbottom(cfg.width,vpos)
        self.draw = True

    def check_drawing(self) :
        if self.rect.right < 0 :
            self.draw = False
            self.despawned = True
        else :
            self.draw = True

