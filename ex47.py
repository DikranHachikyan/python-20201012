#2.

from functools import wraps


def upper_case(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.__original = func
        args = [ f'{v}'.upper() for v in args]
        return func(*args, **kwargs)
    return wrapper


@upper_case
def concat(*args, **kwargs):
    '''Concatenate list elements'''
    sep = kwargs.get('sep',';')
    return sep.join(map(str,args))

if __name__ == '__main__':
    users = ['anna','maria','markus','florian']

    print(concat(*users, sep = '|'))
    
    print(concat(11,22,'python',33,44, sep = '|'))
    
    print(concat.__original(*users, sep = '|'))
    print(concat.__original(11,22,'python',33,44, sep = '|'))

    print = upper_case(print)

    print('Hello Python')

    print = print.__original
    print('Hello Python')
