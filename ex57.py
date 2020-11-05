
# клас
class Point():
    # Конструктор на класа - инициализация на данните на класа
    def __init__(self, x = 0, y = 0, *args, **kwargs):
        print('object constructor')
        # данни на класа
        self._x = x
        self._y = y

    # Метод на класа
    def draw(self):
        print(f'draw point at:({self._x}, {self._y})')

    def move_to(self, dx, dy):
        self._x += dx
        self._y += dy


if __name__ == '__main__':
    # p1 - обект, представител на класа
    p1 = Point()
    p2 = Point(12,45)

    p1.draw()
    p2.draw()

    p1.move_to(10,20)
    p1.draw()
    # p1._x = 200
    # p1._y = 300
    # p1.draw()