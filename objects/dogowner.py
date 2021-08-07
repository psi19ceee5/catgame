from objects import config as cfg
from objects import movable

class DogOwner(movable.Movable):
    
    speed = 1*cfg.invader_base_speed
    imagefile = "dogowner.png"
    tag = "dogowner"
    colorkey = -1
    
    def set_init_vfield(self, fieldnr):
        vpos = (fieldnr + 0.8)*(cfg.height/cfg.vfields)
        super().setpos_leftbottom(cfg.width,vpos)
        
    def update(self):
        if self.velocity_control() :
            self.rect.move_ip((-1, 0))
