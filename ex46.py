
def sort_priority(values, group):
    def helper(item):
        if item in group:
            return (0, item)
        return (1,item)
        
    return values.sort(key = helper)

if __name__ == '__main__':
    nums  = [3, 2, 4, 7, 8, 9, 1, 5]
    group = {9, 8, 7}

    sort_priority(nums, group)

    print(f'nums:{nums}')