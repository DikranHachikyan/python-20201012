
# import draw as p

# ако няма __init__.py
# from  draw.point import Point 

from draw import Point

class Rectangle(Point):
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

    def draw(self):
        super().draw()
        print(f'draw rectangle:[{self.width} x{self.height}]')

if __name__ == '__main__':
    shapes = [Point(2,3), Rectangle(6,7,100,200), Point(15,20)]

    for s in shapes:
        s.draw()
        print('-' * 20)