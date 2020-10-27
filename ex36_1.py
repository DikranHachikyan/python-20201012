
# 1. дефиниция

def foo(a = None, b = None):
    if not a: a = []
    if not b: b = {}
    
    print(f'a:{a}')
    print(f'b:{b}')
    print('-' * 15)
    a.append(len(a))
    b[len(a)] = len(a)

if __name__ == '__main__':
#    2. извикване
    foo()
    foo([1,2,3], {'B':100})
    foo()
    foo([11,22,33], {'C':100})
    foo()