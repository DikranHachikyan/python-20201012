
#1.
# import time

#1.1
# import time as t
# t.time()

#2.
from time import time

#3.
# from time import time as tm

if __name__ == '__main__':
    N = 5000

    values = []

    t = time()
    for v in range(1,N):
        for s in range(v, N):
           values.append(divmod(v, s))
    print(f'nested loops:{time() - t:.4f}')

    t = time()
    values2 = [ divmod(v, s) for v in range(1,N) for s in range(v, N)]    
    print(f'loop expr:{time() - t:.4f}')

    t = time()
    values3 = list( (  divmod(v, s) for v in range(1,N) for s in range(v, N)) )    
    print(f'gen expr:{time() - t:.4f}')



   