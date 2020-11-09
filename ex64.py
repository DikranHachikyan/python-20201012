
from  draw import Point 

class Rectangle(Point):
    def __init__(self, x = 0, y = 0, width = 0, height = 0, *args,**kwargs):
        super().__init__(x,y)
        print('Ctr. Rectangle')
        self._width = width
        self._height = height

if __name__ == '__main__':
   r1 = Rectangle(1,2,100,200)

   r1.draw()
   r1.move_to(10,20)
   r1.draw()
   r1.x = 20
   r1.draw()