import tkinter
from tkinter.constants import *
from tkinter.filedialog import askopenfilename
import os
import test2

tk = tkinter.Tk()
tk.title('Zip : Read Fast')
tk.geometry('800x400+100+200')
tk.resizable(0,0)

#For use with scroll bar activation. If greater than 8, scrollbars will appear
counter = 15
fileLocation = ''

#scrolling bar for left nav menu 
def myfunction(event):
    canvas.configure(scrollregion=canvas.bbox('all'), bg='#1B5778')
    
#Enable Dynamic Label Additions
def data():
    for i in range(counter):
        tkinter.Button(interframe,text="my text"+str(i), justify = LEFT,  background = '#2F6B8C', relief='flat', width=24, fg='white', highlightbackground='#1B5778', activebackground="#437FB4").grid(row=i,column=1, pady=5, padx=5)
        tkinter.Label(interframe,text="54%", justify = RIGHT, background = '#1B5778', fg='white').grid(row=i,column=2, padx=2)
	
#Open new Window: Add an Article NOT WORKING
MenuLabelimg = tkinter.PhotoImage(file= os.getcwd() + '/images/addArticleBG.gif')
RandomLabel = tkinter.Label(image = MenuLabelimg)
RandomLabel.image = MenuLabelimg


def openAddArticleWindow():
	#Create Child Window -- Add Article Window
	AddMenutk = tkinter.Tk()
	AddMenutk.title('Add an Article - Zip')
	AddMenutk.geometry('450x340+90+170')
	AddMenutk.resizable(0,0)
	#adding URL label, text input, and submit button
	URLAddLabel = tkinter.Label(AddMenutk, text='Add from URL').place(x=10, y=20)
	URLAddField = tkinter.Entry(AddMenutk, width=38).place(x=10, y=41)
	URLAddSubmit = tkinter.Button(AddMenutk, text='Add Article').place(x=335, y=41)
	#adding add from file tool. label, text input, browse, and submit
	fileAddLabel = tkinter.Label(AddMenutk, text='Add from File').place(x=10, y= 77)
	fileAddField = tkinter.Entry(AddMenutk, width=28).place(x=10, y=97)
	fileAddBrowse = tkinter.Button(AddMenutk, text='Browse', command=loadBrowserWindow).place(x=248, y=97)
	fileAddSubmit = tkinter.Button(AddMenutk, text='Add Article').place(x=335, y=97)
	#adding copy from text: label, multiline input, submit button
	copyAddLabel = tkinter.Label(AddMenutk, text='Copy and Paste Text').place(x=10, y=130)
	copyAddEntry = tkinter.Text(AddMenutk, height=8, width=44, wrap='word', relief='sunken', bd=2).place(x=10, y=152)
	copyAddSubmit = tkinter.Button(AddMenutk, text='Add Artcle').place(x=335, y= 194)
	#Cancel Button
	button = tkinter.Button(AddMenutk, text='Cancel', pady=10,  command=AddMenutk.destroy).pack(side='bottom')
	AddMenutk.mainLoop()

def loadBrowserWindow(self):
	fileLocation = askopenfilename(filetypes=[("Text","*.txt")])
	print (fileLocation)
	

#Set LEFT and Right Frames
LFrame = tkinter.Frame(tk, background='#1B5778')
LFrame.place(x=0, y=0, width=300, height=365)
#Set Transition Frame
LtoRFrame = tkinter.Frame(tk, borderwidth=0, relief='flat')
LtoRFrame.place(x=300, y=0, height=400, width=10)
LtoRbgimg = tkinter.PhotoImage(file= os.getcwd() + '/images/border_LtoR.gif')
LtoRLabel = tkinter.Label(LtoRFrame, image = LtoRbgimg, borderwidth=0, height=400, anchor=NE).place(relx=0, rely=0)
#Set Right Frame area
RFrame = tkinter.Frame(tk, relief='flat', borderwidth=0)
RFrame.place(x=310, y=0, height= 400, width=490)


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

#Nessessary if statement for the code to work as intended because it won't if you put it on the actual if statement right below it....
#If the number of labels exceeds the number of labels that fit inside the interframe, enable scrollbars
if(counter > 8):
	whiteBorder1 = tkinter.Frame(LFrame, width= 300, height=4).place(x=0, y=33)
	whiteBorder2 = tkinter.Frame(LFrame, width= 300, height=6).place(x=0, y=354)

if(counter > 8):
    myscrollbar=tkinter.Scrollbar(LFrame,orient="vertical",command=canvas.yview)
    canvas.configure(yscrollcommand=myscrollbar.set)
    myscrollbar.place(x=285,y=33, height= 325)
    canvas.place(x=-3, y=33, width=302, height=325)
else:
    canvas.place(x=9, y=35, width=280, height=320)

canvas.create_window((0,0),window=interframe,anchor='nw')
interframe.bind("<Configure>",myfunction)
data()

#Bottom Menu Bar
BottomLFrame = tkinter.Frame(tk, background='#1B5778')
BottomLFrame.place(x=0, y=362, width=300, height=45) 

imgAddBTN = tkinter.PhotoImage(file= os.getcwd() + '/images/addBTN_mac.gif')
imgREMBTN = tkinter.PhotoImage(file= os.getcwd() + '/images/remBTN_mac.gif')

BLFAddBtn = tkinter.Button(BottomLFrame, image = imgAddBTN, height=25, bd=0, highlightbackground='#1B5778', command=openAddArticleWindow).grid(row=0, column=0, padx=55)
BLFRemBtn = tkinter.Button(BottomLFrame, image = imgREMBTN, height=25, bd=0, highlightbackground='#1B5778').grid(row=0, column=1, padx=45)

#Exit button //Test only remove later
#button = tkinter.Button(LFrame,text="Exit",width='38',command=tk.destroy)
#button.pack(side=BOTTOM)



#Preview frame Area (with title text)
previewFrame = tkinter.LabelFrame(RFrame, text="Article Preview: [ARTICLENAME]", width=460, height=220).place(relx= 0.03, rely= 0.02)


#Play Button
startButton = tkinter.Button(RFrame, text="Start Reading").place(relx = 0.39, rely=0.66)

#Adding speed scale
speed = 0
speedScale = tkinter.Scale(RFrame, orient='horizontal', length=400, from_=200, to=1000)
speedScale.place(relx = 0.1, rely = 0.78) 
#Speed Scale Label
speedScaleLabel = tkinter.Label(RFrame, text="Select desired reading speed.").place(relx=0.33, rely=0.9)


tk.mainloop()
