import random
import numpy as np
from datetime import datetime

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

def partition(arr, s, e, ix):
    arr[s], arr[ix] = arr[ix], arr[s]
    p = arr[s]
    i = s + 1
    j = s + 1
    while j <= e:
        if arr[j] <= p:
            hold = arr[i]
            arr[i] = arr[j]
            arr[j] = hold
            i += 1
        j += 1
    hold = arr[s]
    arr[s] = arr[i - 1]
    arr[i - 1] = hold
    return i - 1

def quickSort(arr, s=0, e=None):
    if e is None:
        e = len(arr) - 1
    if e - s < 1:
        return
    ix = random.randint(s, e)
    i = partition(arr, s, e, ix)

    quickSort(arr, s, i - 1)
    quickSort(arr, i + 1, e)

def med3Partition(arr,s,e):
    res = 0
    p = idx = None
    m = (s+e-1)//2
    if (arr[s] <= arr[m] <= arr[e]) or (arr[e] <= arr[m] <= arr[s]):
        p = arr[m]
        idx = m
    elif (arr[s] <= arr[e] <= arr[m]) or (arr[m] <= arr[e] <= arr[s]):
        p = arr[e]
        idx = e
    else:
        p = arr[s]
        idx = s
    arr[s],arr[idx] = arr[idx],arr[s]
    i = s + 1
    j = s + 1
    while j <= e:
        if arr[j] <= p:
            hold = arr[i]
            arr[i] = arr[j]
            arr[j] = hold
            i += 1
        j += 1
    hold = arr[s]
    arr[s] = arr[i - 1]
    arr[i - 1] = hold
    return i - 1

def med3QuickSort(arr, s=0, e=None):
    if e is None:
        e = len(arr) - 1
    if e - s < 1:
        return
    i = med3Partition(arr, s, e)

    med3QuickSort(arr, s, i - 1)
    med3QuickSort(arr, i + 1, e)

def isSorted(arr):
    for i in range(len(arr)):
        if i != 0:
            if arr[i-1] > arr[i]:
                return False
    return True

# arr = [12, 11, 13, 5, 7, 6]
# print(arr)
# start = datetime.now()
# med3QuickSort(arr, 0, len(arr) - 1)
# end = datetime.now()
# print(arr)
# print(isSorted(arr))
# print(end - start)
# n = [10,20,30]
n = [1000, 2000, 3000, 5000, 10000, 20000, 30000, 40000, 50000, 60000]
times = np.zeros((5,len(n),10))
for i in range(len(n)): #for each array size
    print("running for %s" % n[i])
    for j in range(10): #for each trial
        arr = np.random.rand(n[i]).tolist()#make array to use for all tests
        for k in range(5):
            start = end = None
            if(k==0):#insertion
                if(j==0):
                    print("\trunning insersion sort")
                unSorted = arr[:]
                start = datetime.now().microsecond
                insertionSort(unSorted)
                end = datetime.now().microsecond
            elif(k==1):#merge
                if(j==0):
                    print("\trunning merge sort")
                unSorted = arr[:]
                start = datetime.now().microsecond
                mergeSort(unSorted)
                end = datetime.now().microsecond
            elif(k==2):#heap
                if(j==0):
                    print("\trunning heap sort")
                unSorted = arr[:]
                start = datetime.now().microsecond
                heapSort(unSorted)
                end = datetime.now().microsecond
            elif(k==3):#quick
                if(j==0):
                    print("\trunning quick sort")
                unSorted = arr[:]
                start = datetime.now().microsecond
                quickSort(unSorted)
                end = datetime.now().microsecond
            else:#med 3 quick
                if(j==0):
                    print("\trunning med 3 quick sort")
                unSorted = arr[:]
                start = datetime.now().microsecond
                med3QuickSort(arr)
                end = datetime.now().microsecond
            elapsed = end - start
            # print(elapsed)
            times[k,i,j] = elapsed
print(times)
savetxt('times.csv', times, delimiter=',')
avgs = np.average(times,2)
print(avgs)
savetxt('averages.csv', avgs, delimiter=',')