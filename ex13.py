def main():
    num = int(input('num='))
    m = 0
    
    # (condition)? true-expr:false-expr класически формат
    # true-expr (condition)? false-expr Python

    m = num if num > 0 else num ** 2

    # if num > 0:
    #     m = num        
    # else:
    #     m = num ** 2

    print(f'm = {m}')

main()