import tkinter
from tkinter.constants import *
import os

#Create Child Window -- Add Article Window	
AddMenutk = tkinter.Tk()	
AddMenutk.title('Add an Article - Zip')	
AddMenutk.geometry('450x340+90+170')	
AddMenutk.resizable(0,0)	
#Add elements to window	
#topCanvas = tkinter.Canvas(AddMenutk, width=450, height=43).place(x=0,y=0)
#image = topCanvas.create_image(0, 0, anchor=NE, image=MenuLabelimg)
MenuLabelimg = tkinter.PhotoImage(file= os.getcwd() + '/images/addArticleBG.gif')
MenuTopLabel = tkinter.Label(AddMenutk,image = MenuLabelimg, bd=0, anchor=NE, width=450, height=43)
#MenuTopLabel.image = MenuLabelimg
MenuTopLabel.place(x=0, y=0)	
#adding URL label, text input, and submit button
URLAddLabel = tkinter.Label(AddMenutk, text='Add from URL').place(x=10, y=30)
URLAddField = tkinter.Entry(AddMenutk, width=38).place(x=10, y=51)
URLAddSubmit = tkinter.Button(AddMenutk, text='Add Article').place(x=335, y=51)
#adding add from file tool. label, text input, browse, and submit
fileAddLabel = tkinter.Label(AddMenutk, text='Add from File').place(x=10, y= 87)
fileAddField = tkinter.Entry(AddMenutk, width=28).place(x=10, y=107)
fileAddBrowse = tkinter.Button(AddMenutk, text='Browse').place(x=248, y=107)
fileAddSubmit = tkinter.Button(AddMenutk, text='Add Article').place(x=335, y=107)
#adding copy from text: label, multiline input, submit button
copyAddLabel = tkinter.Label(AddMenutk, text='Copy and Paste Text').place(x=10, y=140)
copyAddEntry = tkinter.Text(AddMenutk, height=8, width=44, wrap='word', relief='sunken', bd=2).place(x=10, y=162)
copyAddSubmit = tkinter.Button(AddMenutk, text='Add Artcle').place(x=335, y= 204)
#Cancel Button
button = tkinter.Button(AddMenutk, text='Cancel', pady=10,  command=AddMenutk.destroy).pack(side='bottom')

AddMenutk.mainloop()