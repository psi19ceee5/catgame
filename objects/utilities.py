import os
import pygame as pg
from objects import config as cfg

class ImageLoader:
    def __init__(self):
        pass

    def set_data_dir(self, dir):
        self.data_dir = dir
        
    def load_image(self, name, colorkey=None):
        fullname = os.path.join(self.data_dir, name)
        try:
            image = pg.image.load(fullname)
        except pg.error:
            print("Cannot load image:", fullname)
            raise SystemExit(str(geterror()))
        image = image.convert()
        if colorkey is not None:
            if colorkey == -1:
                colorkey = image.get_at((0, 0))
            image.set_colorkey(colorkey, pg.RLEACCEL)
        native_width = round(image.get_rect().width)
        native_height = round(image.get_rect().height)
        width = native_width * round(cfg.width / cfg.owidth)
        height = native_height * round(cfg.height / cfg.oheight)
        image = pg.transform.scale(image, (width, height))
        return image, image.get_rect()

imgld = ImageLoader()


