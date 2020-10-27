
# 1. дефиниция

def get_squares(n):
    return [ v ** 2 for v in range(n + 1)]

def generate_squares(n):
    for v in range(n + 1):
        yield v ** 2

if __name__ == '__main__':
#    2. извикване
    values = get_squares(10)

    print(f'values = {values}')

    # 1. присвояваме генератора на пром
    sqr = generate_squares(10)

    print(type(generate_squares))
    print(type(sqr))

    print(f'1->{next(sqr)}')
    print(f'2->{next(sqr)}')
    print(f'3->{next(sqr)}')
    print(f'4->{next(sqr)}')
    print(f'5->{next(sqr)}')
