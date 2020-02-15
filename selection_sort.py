def selection_sort(arr):
    for i in range(0,len(arr)):
        min = i
        for j in range(i+1,len(arr)):
            if arr[j] < arr[min]:
                min = j
        if i != min:
            arr[i],arr[min] = arr[min],arr[i]
            print(i)
    return arr


print(selection_sort([123,123,1234,53254,45,345,345,345,34,534,5425]))