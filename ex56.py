
# клас
class Point():
    # Конструктор на класа - инициализация на данните на класа
    def __init__(self):
        print('object constructor')
        # данни на класа
        self.x = 10
        self.y = 20

    # Метод на класа
    def draw(self):
        print(f'draw point at:({self.x}, {self.y})')

if __name__ == '__main__':
    # p1 - обект, представител на класа
    p1 = Point()

    p1.draw()
    print(f'Point p1:({p1.x},{p1.y})')
    print(f'type:{p1}')