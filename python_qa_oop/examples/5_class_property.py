class Materials:
    WOOD = 15.0
    STEEL = 50.0
    PAPER = 1.0


class Cube:

    def __init__(self, h, w, d, material):
        self.h = h
        self.w = w
        self.d = d
        self.material = material

    @property
    def price(self):
        return self.w * self.d * self.h * self.material


cube = Cube(h=10, w=2, d=5, material=Materials.WOOD)
