from draw import Point
from draw import Shape

class Rectangle(Point,Shape):
    def __init__(self, x = 0, y = 0, width = 0, height = 0, *args,**kwargs):
        super().__init__(x,y)
        print('Ctr. Rectangle')
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self,width):
        self._width = width

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        self._height = height

    def __eq__(self,other):
        if not isinstance(other,Rectangle):
            return NotImplemented
        p = super().__eq__(other)
        return p and self.width == other.width and self.height == other.height 

    def __str__(self):
        return super().__str__() + f'[{self.width} x {self.height}]'

    def draw(self):
        super().draw()
        print(f'draw rectangle:[{self.width} x{self.height}]')
