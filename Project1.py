def insertionSort(arr):
    for i in range(1,len(arr)):
        cur = arr[i]
        j = i - 1
        while j >= 0 and cur < arr[j]:
            arr[j+1] = arr[j]
            j = j - 1
        arr[j + 1] = cur


arr = [12, 11, 13, 5, 6]
print(arr)
insertionSort(arr)
print(arr)