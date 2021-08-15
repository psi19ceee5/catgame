from objects import config as cfg
from objects import movable

class UglyCat(movable.Movable):

    imagefile = "uglycat.png"
    tag = "cat"
    colorkey = -1
    cont_wiggle_amplitude = 0.1
    cont_wiggle_freq = 0.5

    def setpos(self, pos, field, object_stack):
        cellwidth = field.image.get_width()/cfg.hfields
        cellheight = field.image.get_height()/cfg.vfields
        hpos = pos[0] - pos[0]%cellwidth
        vpos = pos[1] - pos[1]%cellheight + cellheight
        super().setpos_init_leftbottom(hpos, vpos)
        hcoord = hpos/cellwidth
        vcoord = vpos/cellheight - 1
        if field.cell_is_occupied((hcoord, vcoord)) :
            self.draw = False
            object_stack.remove(self)
        else :
            self.draw = True
            field.append_occupied_cell((hcoord, vcoord))
