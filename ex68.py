
# import draw as p

# ако няма __init__.py
# from  draw.point import Point 

from draw import Rectangle 


if __name__ == '__main__':
    r1 = Rectangle(10,20,100,200)
    r2 = Rectangle(10,20,300,400)

    if r1 == r2:
        print(f'{r1} = {r2}')
    else:
        print(f'{r1} <>{r2}')


    print(f'area:{r1} = {r1.area()}')