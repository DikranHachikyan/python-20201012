# глобална променлива
value = 100

def foo(*args):
    print('Hello pYthon')

# 1. дефиниция
def add_numbers(a, b, *args):
    # c е локална променлива
    # print(f'type of:{type(args)}')
    # print(f'args:{args}')
    c = a + b
    for v in args:
        c += v
    return c

if __name__ == '__main__':
    # 2. извикване
    x, y = 10, 20

    res = add_numbers(x, y)

    print(f'{x} + {y} = { res }')
    
    res = add_numbers(x, y, 1, 2, 3, 4, 5, 6, 7)

    print(f'{x} + {y} + ... = { res }')

    arr = list(range(5))

    res = add_numbers(x, y, *arr)
    print(f'{x} + {y} + ' + ' + '.join(str(v) for v in arr) + f'={res}')
    
