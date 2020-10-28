#2.
from time import time, sleep
from functools import wraps

def show(f):
    if f.__name__ == 'foo':
        f()

def measure(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        t = time()
        func(*args,**kwargs)
        print(f'{func.__name__}:{time() - t:.4f}')
        print(f'doc_str:{func.__doc__}')
    return wrapper

@measure
def foo(sleep_time = 0.3):
    '''Function foo sleeps sleep_time seconds '''
    sleep(sleep_time)


@measure
def display():
    print('Hello Python')

if __name__ == '__main__':
    

    foo(0.5)
    foo()

    print(f'{foo.__name__} => {foo.__doc__}')

    # show(foo) 
    display()   