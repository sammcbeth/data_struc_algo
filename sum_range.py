def sum_range(num):
    if num == 1:
        return 1
    else:
        return sum_range(num-1) + num


print(sum_range(5))
