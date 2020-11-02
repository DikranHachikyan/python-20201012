def suma(a, b):
    return a + b

def exit_app(*args):
    quit()

if __name__ == '__main__':
    actions = {
        '+': suma,
        'q': exit_app
    }
    while True:
        try:
            a = int(input('value of a(int):'))
            op = input('Enter +, -, *, /,q:')
            b = int(input('value of b(int):'))
            print(f'{a} {op} {b} = {actions[op](a,b)}')

        except (KeyError,ValueError) as e:
            print(f'Unsupported operation or invalid value ({e})')
        else:
            continue
        finally:
            print('finally (clean up)')
