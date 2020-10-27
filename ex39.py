


if __name__ == '__main__':
   squares = ( v  for v in range(5,50,5))

   print(f'1->{next(squares)}')
   print(f'2->{next(squares)}')
   print(f'3->{next(squares)}')
   print(f'4->{next(squares)}')

   lst1 = list(squares)
   print(f'lst1 = {lst1}')
   
   lst2 = list(squares)
   print(f'lst2 = {lst2}')
   