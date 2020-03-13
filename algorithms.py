import time
import sys 
  
sys.setrecursionlimit(10**6) 

def bubble_Sort(data,drawData):
    for _ in range(len(data)-1):
        for j in range(len(data)-1):
            if(data[j]>data[j+1]):
                data[j], data[j+1] = data[j+1], data[j]
                drawData(data,['green' if x==j or x==j+1 else 'red' for x in range(len(data))])
                time.sleep(0.01)

    drawData(data,['green' for x in range(len(data))])

def selection_Sort(data, drawData):
    for i in range(len(data)-1):
        min = data[i]
        minindex = i
        for j in range(i+1,len(data)):
            if(data[j]<min):
                min = data[j]
                minindex = j
                drawData(data,['green' if x==j or x==i else 'red' for x in range(len(data))])
                time.sleep(0.02)

        data[i], data[minindex] = data[minindex],data[i]
        drawData(data,['green' if x==minindex or x==i else 'red' for x in range(len(data))])
        time.sleep(0.04)
    
    drawData(data,['green' for x in range(len(data))])

def insertion_Sort(data, drawData):
    for i in range(1, len(data)):
        j = i-1
        key = data[i]
        while(j>=0 and data[j]>key):
            data[j+1] = data[j]
            j -= 1
            drawData(data,['green' if x==j or x==i else 'red' for x in range(len(data))])
            time.sleep(0.02)

        data[j+1] = key
        drawData(data,['green' if x==j or x==i else 'red' for x in range(len(data))])
        time.sleep(0.04)
        
    drawData(data,['green' for x in range(len(data))])

def merge(arr, l, m, r, drawData):
    n1 = m - l + 1 
    n2 =  r - m 
  
    L = arr[l:m+1]
    R = arr[m+1:r+1]   

    i = 0  
    j = 0  
    k = l
    while (i < n1 and j < n2): 
        if (L[i] <= R[j]): 
            arr[k] = L[i] 
            i+=1
            drawData(arr,['green' if x==k or x==i else 'red' for x in range(len(arr))])
            time.sleep(0.02)  
        else: 
            arr[k] = R[j] 
            j+=1
            drawData(arr,['green' if x==k or x==j else 'red' for x in range(len(arr))])
            time.sleep(0.02)
        k+=1
  
    while (i < n1): 
        arr[k] = L[i] 
        i+=1 
        k+=1
        drawData(arr,['green' if x==j or x==i else 'red' for x in range(len(arr))])
        time.sleep(0.02) 
  
    while (j < n2):
        arr[k] = R[j] 
        j+=1 
        k+=1
        drawData(arr,['green' if x==j or x==i else 'red' for x in range(len(arr))])
        time.sleep(0.02)

    time.sleep(0.04)
    drawData(arr,['green' for x in range(len(arr))])

  
def mergeSort(arr, l, r, drawData):
    if (l < r):  
        m = l+(r-l)//2
        mergeSort(arr, l, m, drawData)
        mergeSort(arr, m+1, r, drawData) 
        merge(arr, l, m, r, drawData)

def partition(data,l,r,drawData):
    key = data[r]
    j = l-1
    i = l
    for i in range(l,r):
        if(data[i] < key):
            data[j+1],data[i] = data[i],data[j+1]
            drawData(data,['green' if x==j or x==i else 'red' for x in range(len(data))])
            time.sleep(0.02)
            j += 1

    data[j+1],data[r] = key,data[j+1]
    drawData(data,['green' if x==j or x==r else 'red' for x in range(len(data))])
    time.sleep(0.02)
    return j+1

def quickSort(data,l,r,drawData):
    if(l<r):
        pos = partition(data,l,r,drawData)
        quickSort(data,l,pos-1,drawData)
        quickSort(data,pos+1,r,drawData)
