# глобална променлива
value = 100

def foo():
    print('Hello pYthon')

# 1. дефиниция
def add_numbers(a, b, d = 0):
    # c е локална променлива
    c = a + b + d
    return c

if __name__ == '__main__':
    # 2. извикване
    x, y = 10, 20

    res = add_numbers(x, y)

    print(f'{x} + {y} = { res }')
    
    z = 2
    res = add_numbers(x, y, z)

    print(f'{x} + {y} + {z} = { res }')

    # z = foo()