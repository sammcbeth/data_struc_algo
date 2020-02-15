def bubble_sort(arr):
    
    i = len(arr) -1
    while i > 0:
        noSwaps = True
        for idx,val in enumerate(arr):
            if idx == i:
                break
            if arr[idx] > arr[idx + 1]:
                arr[idx],arr[idx + 1] = arr[idx + 1], arr[idx]
                noSwaps = False
        i -= 1
        print(arr)
        if noSwaps:
            break
    return arr

bubble_sort([123,123,1234,53254,45,345,345,345,34,534,5425])