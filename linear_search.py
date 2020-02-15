def linear_search(arr, val):
    for idx,thing in enumerate(arr):
        if thing == val:
            return idx
    return -1

print(linear_search([1,2,3,4,5,6,7,8,9], 0))
            