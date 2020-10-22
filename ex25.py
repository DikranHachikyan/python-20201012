
if __name__ == '__main__':
    lst = [ x ** 2 for x in range(10)]

    print(lst)
    print(sum(lst))

    letters = [ v for v in 'hello python']

    print(letters)

    print('|'.join(letters))
