#!/usr/bin/python
# -*- coding: iso-8859-1 -*-
import tkinter
from tkinter import *
from tkinter.constants import *
from tkinter.filedialog import askopenfilename
import tkinter.messagebox
import sqlite3 as lite
from tkinter.scrolledtext import ScrolledText
import os
import URLaccess
import ManageArticles

class mainScreen_tk(tkinter.Tk):
	counter = 0
	
	def __init__(self,parent):
		tkinter.Tk.__init__(self,parent)
		self.parent = parent
		self.initialize()

	def initialize(self):
		self.grid()
		
		LFrame = tkinter.Frame(self, background='#1B5778')
		LFrame.place(x=0, y=0, width=300, height=365)
		#Set Transition Frame
		LtoRFrame = tkinter.Frame(self, borderwidth=0, relief='flat')
		LtoRFrame.place(x=300, y=0, height=400, width=10)
		self.LtoRbgimg = tkinter.PhotoImage(file= os.getcwd() + '/images/border_LtoR.gif')
		LtoRLabel = tkinter.Label(LtoRFrame, image = self.LtoRbgimg, borderwidth=0, height=400, anchor=NE).place(relx=0, rely=0)
		#Set Right Frame area
		RFrame = tkinter.Frame(self, relief='flat', borderwidth=0)
		RFrame.place(x=310, y=0, height= 400, width=490)
		
		self.LeftHeaderImg = tkinter.PhotoImage(file= os.getcwd() + '/images/LeftMenuBGImg.gif')
		LeftHeaderLabel = tkinter.Label(self, image = self.LeftHeaderImg, borderwidth=0, height=34, anchor=NE).place(x=0, y=0)
		
		whiteBorder1 = tkinter.Frame(LFrame, width= 300, height=4).place(x=0, y=33)
		whiteBorder2 = tkinter.Frame(LFrame, width= 300, height=4).place(x=0, y=354)
		
		#Article Holder
		self.articleFrame = tkinter.Frame(LFrame, width=280, height=315, bg='#1B5778') 
		self.articleFrame.place(x=9, y=39)
		
		self.articleIDs = ManageArticles.selectAllArtileIDs()
		self.globalCounter = 0
		
		self.loadArticleButtons()
		
		
		#Bottom Menu Bar
		BottomLFrame = tkinter.Frame(self, background='#1B5778')
		BottomLFrame.place(x=0, y=362, width=300, height=45) 
		
		self.imgAddBTN = tkinter.PhotoImage(file= os.getcwd() + '/images/addBTN_mac.gif')
		self.imgREMBTN = tkinter.PhotoImage(file= os.getcwd() + '/images/remBTN_mac.gif')
		
		BLFAddBtn = tkinter.Button(BottomLFrame, image = self.imgAddBTN, height=25, bd=0, highlightbackground='#1B5778', command=self.openAddArticleWindow)
		BLFAddBtn.grid(row=0, column=0, padx=55)
		BLFRemBtn = tkinter.Button(BottomLFrame, image = self.imgREMBTN, height=25, bd=0, highlightbackground='#1B5778', command=self.loadArticleButtons)
		BLFRemBtn.grid(row=0, column=1, padx=45)

		#Preview frame Area (with title text)
		previewFrame = tkinter.LabelFrame(RFrame, text="Article Preview: [ARTICLENAME]", width=460, height=220).place(relx= 0.03, rely= 0.02)


		#Play Button
		startButton = tkinter.Button(RFrame, text="Start Reading")
		startButton.place(relx = 0.39, rely=0.66)

		#Adding speed scale
		self.speed = 0
		speedScale = tkinter.Scale(RFrame, orient='horizontal', length=400, from_=200, to=1000)
		speedScale.place(relx = 0.1, rely = 0.78) 
		#Speed Scale Label
		speedScaleLabel = tkinter.Label(RFrame, text="Select desired reading speed.").place(relx=0.33, rely=0.9)
		
		#Instantiate The Varibles
		self.entryVarFileLocation = tkinter.StringVar()
		self.entryVarArticleName = tkinter.StringVar()
		self.entryVarURL = tkinter.StringVar()
		self.entryVarPlainText = tkinter.StringVar()
		
		self.entryVarFileLocation.set('')
		self.entryVarURL.set('http://')
		self.entryVarArticleName.set('')
		self.entryVarPlainText.set('')
		self.copyAddEntry = ScrolledText(self, height=8, width=44, wrap='word', relief='sunken', bd=2)

		
	def openAddArticleWindow(self):
		self.counter += 1
		t = tkinter.Toplevel(self)
		t.wm_title('Add an Article - Zip')
		t.wm_geometry('450x368+90+170')
		t.wm_resizable(0,0)
		
		#Article Name Label, text entry input
		articleLabel = tkinter.Label(t, text='Article Name:').place(x=10, y=10)
		self.articleAddField = tkinter.Entry(t, width=52, textvariable=self.entryVarArticleName).place(x=10, y=30)
		
		#adding URL label, text input, and submit button
		URLAddLabel = tkinter.Label(t, text='Add from URL').place(x=10, y=60)
		self.URLAddField = tkinter.Entry(t, width=38, textvariable=self.entryVarURL).place(x=10, y=81)
		URLAddSubmit = tkinter.Button(t, text='Add Article', command=self.parseURLText).place(x=335, y=81)
		#adding add from file tool. label, text input, browse, and submit
		fileAddLabel = tkinter.Label(t, text='Add from File').place(x=10, y= 117)
		self.fileAddField = tkinter.Entry(t, textvariable=self.entryVarFileLocation, width=28).place(x=10, y=137)
		fileAddBrowse = tkinter.Button(t, text='Browse', command=self.openFileDiagloge).place(x=248, y=137)
		fileAddSubmit = tkinter.Button(t, text='Add Article', command=self.parseTextfromFile).place(x=335, y=137)
		#adding copy from text: label, multiline input, submit button
		copyAddLabel = tkinter.Label(t, text='Copy and Paste Text').place(x=10, y=170)
		self.copyAddEntry = ScrolledText(t, height=8, width=41, wrap='word', relief='sunken', bd=2)
		self.copyAddEntry.place(x=10, y=192)
		copyAddSubmit = tkinter.Button(t, text='Add Artcle', command=self.parsePlainText).place(x=335, y= 234)
		#Cancel Button
		button = tkinter.Button(t, text='Cancel', pady=10,  command=t.destroy).pack(side='bottom')
	
	def openFileDiagloge(self):	
		filename = askopenfilename(filetypes=[("Text","*.txt")])
		self.entryVarFileLocation.set(filename)
	
	def parseTextfromFile(self):
		enteredPath = self.entryVarFileLocation.get()
		words = URLaccess.parseFiletoWords(enteredPath)
		if(words == False):
			self.displayMessageBox('Failed','The file does not exist or the entry field is blank. Please check again.')
			return None
		enteredName = self.entryVarArticleName.get()
		if(enteredName == ''):
			self.displayMessageBox('Failed', 'Please give the article a name.')
			return None
		result = ManageArticles.addArticle(enteredName, words)
		if(result):
			self.displayMessageBox('Success','The article was successfully added.')
			self.entryVarArticleName.set('')
			self.entryVarFileLocation.set('')
		else:
			self.displayMessageBox('Failed', 'An error has occured. Please verify that the path is entered correctly and verify the file location.')#12543
			self.displayMessageBox('Failed', 'The file location field must not be blank')
			
	def parseURLText(self):
		enteredURL = self.entryVarURL.get()
		words = URLaccess.URL_Parse(enteredURL)
		if(words == False):
			self.displayMessageBox('Failed','Not a valid URL field.')
			return None
		enteredName = self.entryVarArticleName.get()
		if(enteredName == ''):
			self.displayMessageBox('Failed', 'Please give the article a name.')
			return None
		result = ManageArticles.addArticle(enteredName, words)
		if(result):
			self.displayMessageBox('Success','The article was successfully added.')
			self.entryVarURL.set('')
			self.entryVarArticleName.set('')
		else:
			self.displayMessageBox('Falied', 'An error has occured. Please verify that the URL is entered correctly and verify your internet connection.')
			
	def parsePlainText(self):
		#enteredText = self.entryVarPlainText.get()
		enteredText = self.copyAddEntry.get('1.0', END+'-1c')
		enteredName = self.entryVarArticleName.get()
		if(enteredText == ''):
			self.displayMessageBox('Failed', 'The text field does not contain any content. Please ensure that the text is correctly placed and try again.')
		elif(enteredName == ''):
			self.displayMessageBox('Failed', 'Please give the article a name.')
		else:
			result = ManageArticles.addArticle(enteredName, enteredText)
			if(result):
				self.displayMessageBox('Success','The article was successfully added.')
				self.copyAddEntry.delete('1.0', END+'-1c')
				self.entryVarArticleName.set('')
			else:
				self.displayMessageBox('Falied', 'An error has occured. Please try again.')
					
	
	def loadArticleButtons(self):
		#self.globalCounter 
		#self.articleIDs
		i = 0
		
		if(self.globalCounter == len(self.articleIDs)):
			self.displayMessageBox('Whoops','No more articles to display.')
			
		
		for self.globalCounter in range(self.globalCounter, len(self.articleIDs)):
			
			if(self.globalCounter == 0):
				idvar1 = self.globalCounter
				box1 = tkinter.Button(self.articleFrame, text= self.getArticleName(self.articleIDs[self.globalCounter]), justify = LEFT,  background = '#2F6B8C', relief='flat', width=24, fg='white', highlightbackground='#1B5778', activebackground="#437FB4", command=lambda:self.getArticleContent(self.articleIDs[idvar1])).grid(row=i,column=1, pady=5, padx=5)
				self.globalCounter += 1
				i += 1
			
			elif(((self.globalCounter % 7) != 0)):
					if (i==0):
						idvar2 = self.globalCounter
						box1 = tkinter.Button(self.articleFrame, text= self.getArticleName(self.articleIDs[self.globalCounter]), justify = LEFT,  background = '#2F6B8C', relief='flat', width=24, fg='white', highlightbackground='#1B5778', activebackground="#437FB4", command=lambda:self.getArticleContent(self.articleIDs[idvar2])).grid(row=i,column=1, pady=5, padx=5)
						self.globalCounter += 1
						i += 1
					elif (i==1):
						idvar3 = self.globalCounter
						box2 = tkinter.Button(self.articleFrame, text= self.getArticleName(self.articleIDs[self.globalCounter]), justify = LEFT,  background = '#2F6B8C', relief='flat', width=24, fg='white', highlightbackground='#1B5778', activebackground="#437FB4", command=lambda:self.getArticleContent(self.articleIDs[idvar3])).grid(row=i,column=1, pady=5, padx=5)
						self.globalCounter += 1
						i += 1
					elif (i==2):
						idvar4 = self.globalCounter
						box3 = tkinter.Button(self.articleFrame, text= self.getArticleName(self.articleIDs[self.globalCounter]), justify = LEFT,  background = '#2F6B8C', relief='flat', width=24, fg='white', highlightbackground='#1B5778', activebackground="#437FB4", command=lambda:self.getArticleContent(self.articleIDs[idvar4])).grid(row=i,column=1, pady=5, padx=5)
						self.globalCounter += 1
						i += 1
					elif (i==3):
						idvar5 = self.globalCounter
						box4 = tkinter.Button(self.articleFrame, text= self.getArticleName(self.articleIDs[self.globalCounter]), justify = LEFT,  background = '#2F6B8C', relief='flat', width=24, fg='white', highlightbackground='#1B5778', activebackground="#437FB4", command=lambda:self.getArticleContent(self.articleIDs[idvar5])).grid(row=i,column=1, pady=5, padx=5)
						self.globalCounter += 1
						i += 1
					elif (i==4):
						idvar6 = self.globalCounter
						box5 = tkinter.Button(self.articleFrame, text= self.getArticleName(self.articleIDs[self.globalCounter]), justify = LEFT,  background = '#2F6B8C', relief='flat', width=24, fg='white', highlightbackground='#1B5778', activebackground="#437FB4", command=lambda:self.getArticleContent(self.articleIDs[idvar6])).grid(row=i,column=1, pady=5, padx=5)
						self.globalCounter += 1
						i += 1
					elif (i==5):
						idvar7 = self.globalCounter
						box6 = tkinter.Button(self.articleFrame, text= self.getArticleName(self.articleIDs[self.globalCounter]), justify = LEFT,  background = '#2F6B8C', relief='flat', width=24, fg='white', highlightbackground='#1B5778', activebackground="#437FB4", command=lambda:self.getArticleContent(self.articleIDs[idvar7])).grid(row=i,column=1, pady=5, padx=5)
						self.globalCounter += 1
						i += 1
					elif (i==6):
						idvar8 = self.globalCounter
						box7 = tkinter.Button(self.articleFrame, text= self.getArticleName(self.articleIDs[self.globalCounter]), justify = LEFT,  background = '#2F6B8C', relief='flat', width=24, fg='white', highlightbackground='#1B5778', activebackground="#437FB4", command=lambda:self.getArticleContent(self.articleIDs[idvar8])).grid(row=i,column=1, pady=5, padx=5)
						self.globalCounter += 1
						i += 1
			
			else:
				self.globalCounter += 1
				i = 0
				break
				
	def getArticleName(self, articleID):
		try:
			con = lite.connect('zipData')
			with con:
				cur = con.cursor()
				cur.execute("""SELECT Name FROM articles WHERE ID = '%s';""" % (articleID))
				for row in cur.fetchone():
					return(row)
				con.close
			#return (articleName)
		except ValueError:
			return(False)
			
	def getArticleContent(self, aID):
		
		print('Tst stset stest', aID)
						
	def displayMessageBox(self, msgTitle, msgMessage):
		tkinter.messagebox.showinfo(msgTitle, msgMessage)
		
	def deleteArticleFromDB(self, articleName):
		result = ManageArticles.deleteArticle(articleName)
		if(result):
			self.displayMessageBox('Success','The article was successfully deleted.')
		else:
			self.displayMessageBox('Oops', 'An Error has occured. Please try again.')		
		
if __name__ == "__main__":
	app = mainScreen_tk(None)
	app.title('my application')
	app.geometry('800x400+100+200')
	app.mainloop()