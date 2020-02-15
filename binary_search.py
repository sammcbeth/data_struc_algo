def binary_search(arr, val):
    left = 0
    right = len(arr)-1
    while left != right:
        middle = (right + left) // 2
        if arr[middle] == val:
            return middle
        elif arr[middle] > val:
            right = middle - 1
        else:
            left = middle + 1
    return -1

print(binary_search([1,2,3,4,5,6,7,8,9,10,11,12], 14))

