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
    except ValueError:
        print('Invalid Value')
    except KeyError:
        print('Unsupported operation')
    except :
        print('Unknown Error')
