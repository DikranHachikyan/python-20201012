
# import draw as p

# ако няма __init__.py
# from  draw.point import Point 

from draw import Rectangle
from draw import Point
from draw import ShapeUtils



if __name__ == '__main__':
    pn1 = Point(9,8)
    pn2 = Point(6,4)

    print(f'dist: {pn1} and {pn1} = {ShapeUtils.distance(pn1,pn2)}')

    rc1 = Rectangle(40,20,120,300)
    rc2 = Rectangle(30,21,350,400)

    print(f'dist: {rc1} and {rc1} = {ShapeUtils.distance(rc1,rc2)}')

    if ShapeUtils.compare(pn1,pn2) > 0:
        print(f'{pn1} > {pn2}')