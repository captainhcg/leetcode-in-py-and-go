class Vector2D(object):
    def __init__(self, vec2d):
        self.vec2d = [l for l in vec2d if l]
        self.x, self.y = 0, 0

    def next(self):
        val = self.vec2d[self.y][self.x]
        if (self.x + 1) < len(self.vec2d[self.y]):
            self.x += 1
        else:
            self.x = 0
            self.y += 1
        return val

    def hasNext(self):
        if self.y < len(self.vec2d) and self.x < len(self.vec2d[self.y]):
            return True
        return False
