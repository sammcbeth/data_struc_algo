def sliding_window(list, num):
    if num > len(list):
        return 0
    i = 0
    j = num - 1
    temp = 0
    max = 0
    while j < len(list):
        temp = 0
        for x in range(i, j+1):
            temp += list[x]
        if temp > max:
            max = temp
        i += 1
        j += 1
    return max


print(sliding_window([2, 124, 12, 1224, 3, 5, 753, 23], 3))


def sliding_window_2(list, num):
    temp_sum = 0
    max_sum = 0
    for i in range(0, num):
        max_sum += list[i]
    temp_sum = max_sum
    i = num
    while i < len(list):
        temp_sum = temp_sum + list[i] - list[i-num]
        if temp_sum > max_sum:
            max_sum = temp_sum
        i += 1
    return max_sum


print(sliding_window_2([2, 124, 12, 1224, 3, 5, 753, 23], 3))
