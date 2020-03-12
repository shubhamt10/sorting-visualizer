import time

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
