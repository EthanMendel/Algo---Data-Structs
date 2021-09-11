def insertionSort(arr):
    for i in range(1,len(arr)):
        cur = arr[i]
        j = i - 1
        while j >= 0 and cur < arr[j]:
            arr[j+1] = arr[j]
            j = j - 1
        arr[j + 1] = cur

def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) / 2
        l = arr[:mid]
        r = arr[mid:]
        mergeSort(l)
        mergeSort(r)

        i = 0
        j = 0
        k = 0
        while i < len(l) and j < len(r):
            if l[i] < r[j]:
                arr[k] = l[i]
                i = i + 1
            else:
                arr[k] = r[j]
                j = j + 1
            k = k + 1
        if i < len(l):
            while i < len(l):
                arr[k] = l[i]
                i = i + 1
                k = k + 1
        if j < len(r):
            while j < len(r):
                arr[k] = r[j]
                j = j + 1
                k = k + 1

def swapBiggest(arr, n, i):
    biggest = i
    l = i * 2 + 1
    r = i * 2 + 2
    #check if left is bigger than root
    if l < n and arr[biggest] < arr[l]:
        biggest = l
    #check if right is bigger than root
    if r < n and arr[biggest] < arr[r]:
        biggest = r
    #change the root if needed
    if biggest != i:
        hold = arr[i]
        arr[i] = arr[biggest]
        arr[biggest] = hold

        swapBiggest(arr, n, biggest)

def heapSort(arr):
    n = len(arr)
    for i in range(n//2 - 1, -1, -1):
        swapBiggest(arr,n, i)
    for i in range(n-1, 0, -1):
        hold = arr[i]
        arr[i] = arr[0]
        arr[0] = hold

        swapBiggest(arr, i, 0)


arr = [12, 11, 13, 5, 7, 6]
print(arr)
heapSort(arr)
print(arr)