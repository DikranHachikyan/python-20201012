
def get_letters(text):
    for t in text:
        yield t


if __name__ == '__main__':
    gn = get_letters('Lorem ipsum dolor sit amet, consectetur\n')

    try:
        while True:
            print(next(gn), end='')
    except StopIteration:
        pass
        