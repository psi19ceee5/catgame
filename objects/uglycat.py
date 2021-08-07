from objects import config as cfg
from objects import movable

class UglyCat(movable.Movable):

    imagefile = "uglycat.png"
    tag = "cat"
    colorkey = -1

    def setpos(self, pos, object_stack):
        cellwidth = cfg.width/cfg.hfields
        cellheight = cfg.height/cfg.vfields
        hpos = pos[0] - pos[0]%cellwidth
        vpos = pos[1] - pos[1]%cellheight + cellheight
        super().setpos_leftbottom(hpos, vpos)
        if object_stack.isInObject((hpos, vpos-1), "cat") :
            self.draw = False
            object_stack.remove(self)
        else :
            self.draw = True
