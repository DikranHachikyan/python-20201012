#2.

from functools import wraps

def upper_case(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        args = [ f'{v}'.upper() for v in args]
        return func(*args, **kwargs)
    return wrapper

def add_brackets(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        args = [f'[{v}]' for v in args]
        return func(*args, **kwargs)
    return wrapper

@upper_case
@add_brackets
def concat(*args, **kwargs):
    '''Concatenate list elements'''
    sep = kwargs.get('sep',';')
    return sep.join(args)

if __name__ == '__main__':
    users = ['anna','maria','markus','florian']

    print(concat(*users, sep = '|'))
    print(concat(11,22,'python',33,44, sep = '|'))