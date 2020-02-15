import math

def radix_sort(arr):
    length = most_digits(arr)
    for idx in range(0,length):
        partial_arr = [[],[],[],[],[],[],[],[],[],[]]
        for val in arr:
            dig = get_digit(val, idx)
            partial_arr[dig].append(val)
        
        arr = [j for i in partial_arr for j in i]
    return arr

def get_digit(num, pos):
    num = abs(num)
    dig = num % pow(10,pos+1)
    dig = dig // pow(10,pos)
    return dig

def digit_count(num):
    if num == 0:
        return 1
    return  math.floor(math.log10(abs(num))) + 1


def most_digits(arr):
    max = 0
    for val in arr:
        curr = digit_count(val)
        if curr > max:
            max = curr
    return max

print(radix_sort([12345678,1234567,123456,12345,1234,123,12,1]))


# arr = [123,12345,345,23,34,5232,345,423,32,52,52,5546,2]
# for val in arr:
#     get_digit()