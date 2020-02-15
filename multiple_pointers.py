
# def sumZero(list):
#     left = 0
#     right = len(list) - 1
#     while left < right:
#         sum = list[left] + list[right]
#         if sum == 0:
#             return [list[left], list[right]]
#         elif sum > 0:
#             right = right - 1
#         else:
#             left += 1


# print(sumZero([-4, -3, -2, -1, 0, 1, 2, 5]))


def count_unique_values(list):
    i = 0
    j = i+1
    if len(list) == 0:
        return 0
    while j < len(list):
        if list[i] == list[j]:
            j += 1
        else:
            i += 1
            list[i] = list[j]
            j += 1
    return i + 1


print(count_unique_values([]))
