from tkinter import *
from tkinter.ttk import *
import random
from algorithms import bubble_Sort,selection_Sort,insertion_Sort,mergeSort,quickSort

root = Tk()
root.title("Sorting Algorithm Visualizer")
root.maxsize(1000,800)
root.config(bg="black")

selected_Alg = StringVar()
var = IntVar()
data = []
algos = ["Bubble Sort","Selection Sort","Insertion Sort","Merge Sort","Quick Sort"]
selected_Alg = algos[0]

def generateData():
    global data
    size = 50
    data = []
    for _ in range(0,size):
        data.append(random.randrange(0,101))

    drawData(data, ['red' for x in range(len(data))])
    start_btn["state"] = "normal"

def startAlgo():
    global data
    global selected_Alg
    if selected_Alg == algos[0]:
        bubble_Sort(data,drawData)
    elif selected_Alg == algos[1]:
        selection_Sort(data,drawData)
    elif selected_Alg == algos[2]:
        insertion_Sort(data,drawData)
    elif selected_Alg == algos[3]:
        mergeSort(data,0,len(data)-1,drawData)
    else:
        quickSort(data,0,len(data)-1,drawData)
        drawData(data,['green' for x in range(len(data))])

    start_btn["state"] = "disable"
    

def select():
    global data
    global selected_Alg
    selected_Alg = algos[var.get()]

def drawData(data,colorArray):
    canvas.delete("all")
    c_height = 480
    c_width = 960
    x_width = c_width / (len(data)+1)
    offset = 20
    spacing = 5
    normalizedData = [i / max(data) for i in data]
    for i,height in enumerate(normalizedData):
        x0 = i*x_width + offset + spacing
        y0 = c_height - height*440
        x1 = (i+1)*x_width + offset
        y1 = c_height
        canvas.create_rectangle(x0,y0,x1,y1,fill=colorArray[i])
        canvas.create_text(x0 + 1, y0, anchor=SW, text=str(data[i]))
    
    root.update_idletasks()

frame = Frame(root, width=1000, height=200)
frame.grid(row=0, column=0, padx=10, pady = 5)

canvas = Canvas(root, width=1000, height=480)
canvas.grid(row = 1,column = 0, padx=10, pady = 5)

generate_btn = Button(frame, text = "Generate", command = generateData)
generate_btn.grid(row = 0,column = 1,padx = 5)

rad1 = Radiobutton(frame, text="Bubble Sort", variable = var, value = 0, command=select)
rad2 = Radiobutton(frame, text="Selection Sort", variable = var, value = 1, command=select)
rad3 = Radiobutton(frame, text="Insertion Sort", variable = var, value = 2, command=select)
rad4 = Radiobutton(frame, text="Merge Sort", variable = var, value = 3, command=select)
rad5 = Radiobutton(frame, text="Quick Sort", variable = var, value = 4, command=select)
rad1.grid(row=2, column=0, padx = 5)
rad2.grid(row=2, column=1, padx = 5)
rad3.grid(row=2, column=2, padx = 5)
rad4.grid(row=2, column=3, padx = 5)
rad5.grid(row=2, column=4, padx = 5)

start_btn = Button(frame, text = "Start", command = startAlgo)
start_btn.grid(row = 0,column = 2,padx = 5)
start_btn["state"] = "disable"

root.mainloop()