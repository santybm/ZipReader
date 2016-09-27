from tkinter import *
from tkinter.filedialog import askopenfilename

class Application(Frame):
	
	def openFileDiagloge(self):	
		filename = askopenfilename(filetypes=[("Text","*.txt")])
		self.inputLocation.insert(0, filename)
			
	def createWidgets(self):
		self.button = Button(root,text="Browse",command=self.openFileDiagloge)
		self.button.pack(side='right')
		self.inputLocation = Entry(root)
		self.inputLocation.pack(side='left')
			
	def __init__(self, master=None):	
		Frame.__init__(self, master)
		#fileLocation = self.filename
		self.pack()
		self.createWidgets()
	
	def getFileLocation(self):
		return (filename)
	
	def setFileLocation(self,fileURL):
		self.filename = fileURL
	
	
		
		

root = Tk()
root.title("Image Manipulation Program")
app = Application(master=root)
app.mainloop()