
# 1. дефиниция

def sum_numbers(n):
    print(f'n={n}')
    if n > 0:
        return n + sum_numbers(n-1)
    return 0

if __name__ == '__main__':
#    2. извикване
    x = 5
    res = sum_numbers(x)
    print(f'sum {list(range(x + 1))} = {res}')