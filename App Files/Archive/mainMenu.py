import tkinter
from tkinter.constants import *
import os

tk = tkinter.Tk()
tk.title('Zip : Read Fast')
tk.geometry('800x400+300+200')

#scrolling bar for left nav menu 
def myfunction(event):
    canvas.configure(scrollregion=canvas.bbox('all'), bg='#1B5778')
    
counter = 5

def data():
    for i in range(counter):
        tkinter.Button(interframe,text="my text"+str(i), justify = LEFT,  background = '#2F6B8C', relief='flat', width=29, fg='white', activebackground="#437FB4").grid(row=i,column=1, pady=5, padx=5)
        tkinter.Label(interframe,text="54%", justify = RIGHT, background = '#1B5778', fg='white').grid(row=i,column=2, padx=2)


#Set LEFT and Right Frames
LFrame = tkinter.Frame(tk, background='#1B5778')
LFrame.place(x=0, y=0, width=300, height=365)
#Set Right Frame area
RFrame = tkinter.Frame(tk, relief='flat', borderwidth=0)
RFrame.place(x=300, y=0, height= 400, width=500)


#Set Background on Left Menu
img = tkinter.PhotoImage(file= os.getcwd() + '/images/LeftMenuBGImg.gif')
label = tkinter.Label(LFrame,
                       image = img,
                       borderwidth=0,
                       height=34,
                       anchor=NE ).place(x=0, y=0)
#set scrolling canvas
canvas=tkinter.Canvas(LFrame)
interframe=tkinter.Frame(canvas, bg='#1B5778')
if(counter > 8):
    myscrollbar=tkinter.Scrollbar(LFrame,orient="vertical",command=canvas.yview)
    canvas.configure(yscrollcommand=myscrollbar.set)
    myscrollbar.place(x=280,y=35, height= 325)
    canvas.place(x=-1, y=35, width=282, height=325)
else:
    canvas.place(x=9, y=35, width=280, height=320)

canvas.create_window((0,0),window=interframe,anchor='nw')
interframe.bind("<Configure>",myfunction)
data()


#Place Dynamic Labels in Left Menu. AKA Article Titles
#article1Title = tkinter.Button(LFrame, 
#                              #MAX CHAR COUNT for text is 33 + ...)
#                              text="New Surface tablet announced for...",
#                              justify = LEFT,
#                              background = '#2F6B8C', fg='white', activebackground="#437FB4").place(x=8, y=40)
#article1Progress = tkinter.Label(LFrame,
#                                 text="54%",
#                                 justify = RIGHT,
#                                 background = '#1B5778',
#                                fg='white').place(x=250, y=45)

#Bottom Menu Bar
BottomLFrame = tkinter.Frame(tk, background='#1B5778')
BottomLFrame.place(x=0, y=362, width=300, height=45) 

imgAddBTN = tkinter.PhotoImage(file= os.getcwd() + '/images/addBTN.gif')
imgREMBTN = tkinter.PhotoImage(file= os.getcwd() + '/images/remBTN.gif')
imgCNFBTN = tkinter.PhotoImage(file= os.getcwd() + '/images/confBTN.gif')

BLFAddBtn = tkinter.Button(BottomLFrame, image = imgAddBTN, height=25, bd=0).grid(row=0, column=0, padx=40)
BLFRemBtn = tkinter.Button(BottomLFrame, image = imgREMBTN, height=25, bd=0).grid(row=0, column=1, padx=10)
BLRCnfBtn = tkinter.Button(BottomLFrame, image = imgCNFBTN, height=25, bd=0).grid(row=0, column=2, padx=38)

#Exit button //Test only remove later
#button = tkinter.Button(LFrame,text="Exit",width='38',command=tk.destroy)
#button.pack(side=BOTTOM)



#Preview Area                      
label2 = tkinter.Label(RFrame, text="right side")
label2.pack(fill=X, expand=0)


tk.mainloop()
