from tkinter import *

## GUI color map ###
black = "#000000"

root = Tk()
root.title("Canvas Scrollbar Example")
root.geometry('800x400+100+200')
root.resizable(0,0)

topFrame = Frame(root, bd=2, relief=SUNKEN)
topFrame.pack()

xscrollbar = Scrollbar(topFrame, orient=HORIZONTAL)
xscrollbar.pack(side=BOTTOM, fill=X)

yscrollbar = Scrollbar(topFrame, orient=VERTICAL)
yscrollbar.pack(side=RIGHT, fill=Y)

canvasFrame = Canvas(topFrame, width=500, height=500, scrollregion=(0, 0, 1000, 1000),
                xscrollcommand=xscrollbar.set,
                yscrollcommand=yscrollbar.set)

canvasFrame.pack(side=TOP, fill=BOTH, expand=1)

xscrollbar.config(command=canvasFrame.xview)
yscrollbar.config(command=canvasFrame.yview)

entryFrame = Frame(canvasFrame, bd=2, relief=SUNKEN)
entryFrame.pack()

var = {}
for i in range(1,30):
    var[i] = StringVar()
    var[i].set(i)
    e = Entry(entryFrame, width=148, foreground=black, textvariable=var[i])
    e.pack(side=TOP, padx=2)

canvasFrame.create_window(0, 0, window=entryFrame, anchor='nw')

mainloop()