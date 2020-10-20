def main():
    # 1+2+3+.....+99+100 = 5050
    i = 1
    n_sum = 0

    while i <= 100:
        n_sum = n_sum + i
        i = i + 1 

    print(f'1+2+3+...+99+100 = {n_sum}')

main()