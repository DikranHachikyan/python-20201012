def main():
    # 2+4+6.....+98+100 = 2550
    i = 1
    n_sum = 0

    while i <= 100:
        i += 1       
        if ( i % 2 ) != 0:
            break
        n_sum += i  
    else:
        print('else after while')

    print(f'1+2+3+...+99+100 = {n_sum}')

main()