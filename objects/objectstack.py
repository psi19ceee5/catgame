class Objectstack:
    def __init__(self) :
        self.stack = []

    def append(self, drawable_obj) :
        self.stack.append(drawable_obj)

    def size(self) :
        return len(self.stack)

    def remove(self, item) :
        self.stack.remove(item)

    def update(self) :
        for item in self.stack :
            item.update()

    def blit(self, screen) :
        for item in self.stack :
            if item.draw :
                screen.blit(item.image, item.rect)

    def isInField(self, pos) :
        for item in self.stack :
            if item.tag == "field" :
                return item.rect.collidepoint(pos)

    def isInObject(self, pos, tag) :
         for item in self.stack :
             if item.tag == tag :
                 if item.draw == True :
                     if item.rect.collidepoint(pos) :
                         return True
