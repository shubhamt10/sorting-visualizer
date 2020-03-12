from tkinter import *
from tkinter.ttk import *
import random
from algorithms import bubble_Sort,selection_Sort

root = Tk()
root.title("Sorting Algorithm Visualizer")
root.maxsize(1000,800)
root.config(bg="black")

selected_Alg = StringVar()
data = []

def generateData():
    global data
    size = 50
    data = []
    for _ in range(0,size):
        data.append(random.randrange(0,101))

    return data

def startAlgo(algo):
    global data
    if algo == "Bubble Sort":
        bubble_Sort(data,drawData)
    elif algo == "Selection Sort":
        selection_Sort(data,drawData)
    else:
        selection_Sort(data,drawData)

def select(sb):
    selected_Alg = sb['text']
    data = generateData()
    drawData(data, ['red' for x in range(len(data))])
    startAlgo(selected_Alg)

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

btn1 = Button(frame, text = "Selection Sort",command = lambda: select(btn1))
btn1.grid(row=0,column=0,padx=5)
btn2 = Button(frame, text = "Bubble Sort",command = lambda: select(btn2))
btn2.grid(row=0,column=2,padx=5)
btn3 = Button(frame, text = "Insertion Sort",command = lambda: select(btn3))
btn3.grid(row=0,column=4,padx=5)

root.mainloop()