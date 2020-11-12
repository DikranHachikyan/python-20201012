
# import draw as p

# ако няма __init__.py
# from  draw.point import Point 

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

if __name__ == '__main__':
    r1 = Rectangle(10,20,100,200)
    r2 = Rectangle(10,20,300,400)

    if r1 == r2:
        print(f'{r1} = {r2}')
    else:
        print(f'{r1} <>{r2}')


    print(f'area:{r1} = {r1.area()}')