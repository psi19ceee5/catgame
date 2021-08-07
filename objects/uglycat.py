from objects import config as cfg
from objects import movable

class UglyCat(movable.Movable):

    imagefile = "uglycat.png"
    tag = "cat"
    colorkey = -1

    def setpos(self, pos, field, object_stack):
        cellwidth = cfg.width/cfg.hfields
        cellheight = cfg.height/cfg.vfields
        hpos = pos[0] - pos[0]%cellwidth
        vpos = pos[1] - pos[1]%cellheight + cellheight
        super().setpos_leftbottom(hpos, vpos)
        hcoord = hpos/cellwidth
        vcoord = vpos/cellheight - 1
        if field.cell_is_occupied((hcoord, vcoord)) :
            self.draw = False
            object_stack.remove(self)
        else :
            self.draw = True
            field.append_occupied_cell((hcoord, vcoord))
