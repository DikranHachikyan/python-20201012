

if __name__ == '__main__':
    sq = lambda a: a**2

    pw = lambda a: a ** 3 if a % 2 else a ** 2 

    # 1.
    # print(f'4^2={sq(4)}')

    # print(f'pw(3)={pw(3)}')
    # print(f'pw(6)={pw(6)}')

    items = [('A', 5, 7), ('D', 2, 6), ('B', 4, 6), ('D', 2, 5)]
    # 2.
    # items.sort()
    # print(f'in-place sorted:{items}')
    
    # 3.
    # items.sort( key=lambda el: el[1], reverse=True) 
    # print(f'in-place sorted:{items}')
    
    # 4.
    # items.sort( key=lambda el: (el[1], el[0]) ) 
    # print(f'in-place sorted:{items}')
    
    sort_key = lambda el: (el[1], el[0], el[2])
    items.sort( key=sort_key ) 
    print(f'in-place sorted:{items}')
    

    values = [1,2,3,4,5]
    for v in map(lambda a: a * a , values):
        print(v)