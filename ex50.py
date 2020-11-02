def suma(a, b):
    return a + b


if __name__ == '__main__':
    actions = {
        '+': suma
    }

    try:
        a = int(input('value of a(int):'))
        op = input('Enter +, -, *, /:')
        b = int(input('value of b(int):'))
        print(f'{a} {op} {b} = {actions[op](a,b)}')

    except KeyError as e:
        print(f'Unsupported operation({e})')
    except ValueError as e:
        print(f'Invalid Value ({e})')
    except Exception as e:
        print(f'Unknown Error ({e})')
    else:
        print('else part')
    finally:
        print('finally (clean up)')
