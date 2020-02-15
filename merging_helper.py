def merging_helper(arr1, arr2):
    sorted_arr = []
    val1 = 0
    val2 = 0
    while val1 < len(arr1) or val2 < len(arr2):
        if val1 == len(arr1):
            sorted_arr += arr2[val2:]
            return sorted_arr
        if val2 == len(arr2):
            sorted_arr += arr1[val1:]
            return sorted_arr
        if arr1[val1] < arr2[val2]:
            sorted_arr.append(arr1[val1])
            val1+= 1
        else:
            sorted_arr.append(arr2[val2])
            val2 += 1
        
print(merging_helper([1,12,34,56,74],[1,34,63,77]))