from objects import config as cfg
from objects import movable

class DogOwner(movable.Movable):
    
    trans_speed = 1*cfg.invader_base_speed
    imagefile = "dogowner.png"
    tag = "dogowner"
    colorkey = -1
    
    def set_init_vfield(self, fieldnr):
        vpos = (fieldnr + 0.8)*(cfg.height/cfg.vfields)
        super().setpos_init_leftbottom(cfg.width,vpos)
        self.draw = True
        
    def update(self):
        npix = self.pixels_to_move()
        if npix > 0:
            self.rect.move_ip((-1*npix, 0))
