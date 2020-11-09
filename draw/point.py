# клас
class Point():
    #Променлива на класа (статична променлива)
    label = 'A'
    count = 0
    # Конструктор на класа - инициализация на данните на класа
    def __init__(self, x = 0, y = 0, *args, **kwargs):
        print('Ctr Point')
        # данни на класа
        self._x = x
        self._y = y
        Point.count += 1

    # специални методи
    # function override
    def __str__(self):
        '''str(p1) -> string'''
        return f'({self._x}, {self._y})'

    def __add__(self, other):
        '''p = p1 + p2 '''
        # 1
        # assert isinstance(other, Point), 'operand must be inst. of Point'
        #  2
        # assert hasattr(other, '_x') and hasattr(other, '_y'), 'operand must have _x and _y'
        if isinstance(other,Point):
            new_x = self._x + other._x 
            new_y = self._y + other._y
            # raise TypeError('operand must be inst. of Point')
        elif isinstance(other,int):
            new_x = self._x + other 
            new_y = self._y + other
        else:
            return NotImplemented
        return Point(new_x, new_y)

    def __iadd__(self, other):
        ''' p1 += p2'''
        if not isinstance(other, Point):
            return NotImplemented
        self._x += other._x
        self._y += other._y

        return self

    def __eq__(self,other):
        ''' if p1 == p2: '''
        if not isinstance(other,Point):
            return NotImplemented
        return self._x == other._x and self._y == other._y 
    
    def __del__(self):
        '''destructor del p1'''
        Point.count -= 1
    # Достъп до данните
    # def set_x(self,x):
    #     self._x = x

    # def get_x(self):
    #     return self._x

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, x):
        assert x >= 0,'x must be positive'
        self._x = x

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, y):
        assert y >= 0,'y must be positive'
        self._y = y

    # Методи на класа
    def draw(self):
        print(f'draw point at:({self._x}, {self._y})')

    def move_to(self, dx, dy):
        self._x += dx
        self._y += dy



if __name__ == '__main__':
    pass