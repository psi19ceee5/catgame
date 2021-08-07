from objects import drawable

class Field(drawable.Drawable):

    imagefile = "background_field.png"
    tag = "field"
    colorkey = None
    draw = True

    occupied_cells = []

    def append_occupied_cell(self, coordinates) :
        self.occupied_cells.append(coordinates)

    def cell_is_occupied(self, coordinates) :
        for item in self.occupied_cells :
            if item == coordinates :
                return True
            
        return False
