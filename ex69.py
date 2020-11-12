
# import draw as p

# ако няма __init__.py
# from  draw.point import Point 

from draw import Rectangle
from draw import Point
from math import sqrt

class ShapeUtils:
    # статична променлива
    p0 = Point()

    @staticmethod
    def distance(p1,p2):
        if not isinstance(p1,Point) or not isinstance(p2,Point):
            raise TypeError('p1 and p2 must be Point')
        dx = p1.x - p2.x
        dy = p1.y - p2.y
        return sqrt( dx ** 2 + dy ** 2) 
    
    @staticmethod
    def compare(p1,p2):
        '''
        Return:
            negative value p1 < p2
            zero           p1 == p2
            positive value p1 > p2
        '''
        dist1 = ShapeUtils.distance(p1,ShapeUtils.p0)
        dist2 = ShapeUtils.distance(p2,ShapeUtils.p0)

        return dist1 - dist2

if __name__ == '__main__':
    pn1 = Point(9,8)
    pn2 = Point(6,4)

    print(f'dist: {pn1} and {pn1} = {ShapeUtils.distance(pn1,pn2)}')

    rc1 = Rectangle(40,20,120,300)
    rc2 = Rectangle(30,21,350,400)

    print(f'dist: {rc1} and {rc1} = {ShapeUtils.distance(rc1,rc2)}')

    if ShapeUtils.compare(pn1,pn2) > 0:
        print(f'{pn1} > {pn2}')