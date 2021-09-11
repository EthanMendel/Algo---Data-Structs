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

arr = [12, 11, 13, 5, 7, 6]
print(arr)
mergeSort(arr)
print(arr)