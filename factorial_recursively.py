# def factorial(num):
#     if num == 1:
#         return 1
#     return num * factorial(num-1)


# print(factorial(100))

def collectOddValues(arr):
    result = []
    def helper(helperInput):
        if len(helperInput) == 0:
            return
        elif helperInput[0] % 2 != 0:
            result.append(helperInput[0])
        helper(helperInput[1:])
    helper(arr)
    return result

print(collectOddValues([1,2,3,4,5,6,7,8]))