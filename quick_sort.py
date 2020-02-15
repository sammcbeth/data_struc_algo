
def pivot_helper(arr, start=0, end=0):
    pivot = arr[start]
    swapidx = start
    for index in range(start+1, end+1):
        if pivot > arr[index]:
            swapidx += 1
            arr[index],arr[swapidx] = arr[swapidx],arr[index]
    arr[start],arr[swapidx] = arr[swapidx],arr[start]
    return swapidx

def quick_sort(arr, left=0, right=0):
    

    if left < right:
        pivot = pivot_helper(arr,left,right)
        quick_sort(arr,pivot+1,right)
        quick_sort(arr,left,pivot-1)
    return arr


print(quick_sort([23,432,234,134,42,12,123],0,6))