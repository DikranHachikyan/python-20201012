class Number:
    def __getattr__(self,attr):
        ch = attr[0]
        s  = int(attr[1::])

        if ch == 'b':
            return bin(s)
        elif ch == 'o':
            return oct(s)
        elif ch == 'x':
            return hex(s)
        else:
            raise AttributeError('Valid prefixes b,o,x')

if __name__ == '__main__':
    n = Number()

    print(n.b8)
    print(n.o10)
    print(n.x251)
    print(n.d251)