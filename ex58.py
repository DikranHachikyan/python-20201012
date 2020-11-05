
# клас
class Point():
    #Променлива на класа (статична променлива)
    label = 'A'
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

    p1.z = 200

    print(f'p1.z = {p1.z}')
    # AttributeError - p1.z е динамично закачен за обекта
    # print(f'p2.z = {p2.z}')
    print(f'Point Label:{Point.label}, p1.label:{p1.label}, p2.label:{p2.label}')
    Point.label = 'Start'
    print(f'Point Label:{Point.label}, p1.label:{p1.label}, p2.label:{p2.label}')
