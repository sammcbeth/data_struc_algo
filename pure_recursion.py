def collectOddValues(arr):
    newArr = []

    if len(arr) == 0:
        return newArr
    if arr[0] % 2 != 0:
        newArr.append(arr[0])
    newArr = newArr + collectOddValues(arr[1:])
    return newArr

print(collectOddValues([1,2,3,4,5,6,7,8]))
