
def get_squares(n):
    return [ v ** 2 for v in range(n + 1)]

def generate_squares(n):
    for v in range(n + 1):
        yield v ** 2

if __name__ == '__main__':
    #1.
    for v in generate_squares(10):
        print(f'v = {v}')


    #2.
    lst = list(generate_squares(5))
    print(f'lst = {lst}')