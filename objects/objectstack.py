class Objectstack:
    def __init__(self):
        self.stack = []

    def append(self, drawable_obj):
        self.stack.append(drawable_obj)

    def update(self):
        for item in self.stack:
            item.update()

    def blit(self, screen):
        for item in self.stack:
            screen.blit(item.image, item.rect)
