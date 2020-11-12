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