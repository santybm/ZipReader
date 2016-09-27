from tkinter import *
from tkinter.constants import *
from tkinter import filedialog
import os

counter = 15

class App:
	
	def createWidgets(self):
		
	
	def __init__(self,master=None):
		#Set LEFT and Right Frames
		LFrame = tkinter.Frame(tk, background='#1B5778')
		LFrame.place(x=0, y=0, width=300, height=365)
		#Set Transition Frame
		LtoRFrame = tkinter.Frame(tk, borderwidth=0, relief='flat')
		LtoRFrame.place(x=300, y=0, height=400, width=10)
		LtoRbgimg = tkinter.PhotoImage(file= os.getcwd() + '/images/border_LtoR.gif')
		LtoRLabel = tkinter.Label(LtoRFrame, image = LtoRbgimg, borderwidth=0, height=400, anchor=NE)
		LtoRLabel.image = LtoRbgimg #Prevent Garbage Collection
		LtoRLabel.place(relx=0, rely=0)
		#Set Right Frame area
		RFrame = tkinter.Frame(tk, relief='flat', borderwidth=0)
		RFrame.place(x=310, y=0, height= 400, width=490)
		
		#Set Background on Left Menu
		img = tkinter.PhotoImage(file= os.getcwd() + '/images/LeftMenuBGImg.gif')
		label = tkinter.Label(LFrame, image = img, borderwidth=0, height=34, anchor=NE)
		label.image = img
		label.place(x=0, y=0)
		
		#set scrolling canvas
		canvas=tkinter.Canvas(LFrame)
		interframe=tkinter.Frame(canvas, bg='#1B5778')
		
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
		canvas.configure(scrollregion=canvas.bbox('all'), bg='#1B5778')
		App.getArticleData(interframe)
		
		#Bottom Menu Bar
		BottomLFrame = tkinter.Frame(tk, background='#1B5778')
		BottomLFrame.place(x=0, y=362, width=300, height=45) 

		imgAddBTN = tkinter.PhotoImage(file= os.getcwd() + '/images/addBTN_mac.gif')
		imgREMBTN = tkinter.PhotoImage(file= os.getcwd() + '/images/remBTN_mac.gif')

		BLFAddBtn = tkinter.Button(BottomLFrame, image = imgAddBTN, height=25, bd=0, highlightbackground='#1B5778')
		BLFAddBtn.image = imgAddBTN
		BLFAddBtn.grid(row=0, column=0, padx=55)
		BLFRemBtn = tkinter.Button(BottomLFrame, image = imgREMBTN, height=25, bd=0, highlightbackground='#1B5778')
		BLFRemBtn.image = imgREMBTN
		BLFRemBtn.grid(row=0, column=1, padx=45)


		#Preview frame Area (with title text)
		previewFrame = tkinter.LabelFrame(RFrame, text="Article Preview: [ARTICLENAME]", width=460, height=220).place(relx= 0.03, rely= 0.02)

		#Play Button
		startButton = tkinter.Button(RFrame, text="Start Reading").place(relx = 0.39, rely=0.66)

		#Adding speed scale
		speed = 0
		speedScale = tkinter.Scale(RFrame, orient='horizontal', length=400, from_=200, to=980)
		speedScale.place(relx = 0.1, rely = 0.78) 
		#Speed Scale Label
		speedScaleLabel = tkinter.Label(RFrame, text="Select desired reading speed in WPM.").place(relx=0.33, rely=0.9)
		
	#scrolling bar for left nav menu 
	def scrollbarFunction(event, Scrollcanvas):
	    Scrollcanvas.configure(scrollregion=Scrollcanvas.bbox('all'), bg='#1B5778')
	
	def getNumArticles():
		return counter
		
	def setNumArticle(number:int):
		counter = number
	
	#Enable Dynamic Label Additions
	def getArticleData(placementFrame):
		for i in range(counter):
			        tkinter.Button(placementFrame,text="my text"+str(i), justify = LEFT,  background = '#2F6B8C', relief='flat', width=24, fg='white', highlightbackground='#1B5778', activebackground="#437FB4").grid(row=i,column=1, pady=5, padx=5)
			        tkinter.Label(placementFrame,text="54%", justify = RIGHT, background = '#1B5778', fg='white').grid(row=i,column=2, padx=2)

tk = tkinter.Tk()
#Declare Images

tk.title('Zip : Read Fast')	
tk.geometry('800x400+100+200')
tk.resizable(0,0)

app = App(tk)
tk.mainloop()
