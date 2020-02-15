def insertion_sort(arr):
    for i in range(1, len(arr)):
        print(arr)
        temp = i
        for j in range(i-1,-1,-1):
            if arr[temp] < arr[j]:
                arr[temp],arr[j] = arr[j],arr[temp]
                temp = j
            
                
    return arr


print(insertion_sort([123,123,1234,53254,45,345,345,345,34,534,5425]))