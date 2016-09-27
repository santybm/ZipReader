#!/usr/bin/python
# -*- coding: iso-8859-1 -*-
#Copyright ZIP READER
import tkinter
from tkinter import *
from tkinter.constants import *
from tkinter.filedialog import askopenfilename
import tkinter.messagebox
import sqlite3 as lite
from tkinter.scrolledtext import ScrolledText
import os
import time
import URLaccess
import ManageArticles
import URLParser

#Main Tkinter Class
class mainScreen_tk(tkinter.Tk):
	counter = 0
	
	#Initiatize the function
	def __init__(self,parent):
		tkinter.Tk.__init__(self,parent)
		self.parent = parent
		self.initialize()
		
		#Timer Function Global Variable
		self.indexCounter = 0
		self.isItRunning = False
		

	def initialize(self):
		self.grid()
		
		#Set the Left Frame and Place it
		LFrame = tkinter.Frame(self, background='#1B5778')
		LFrame.place(x=0, y=0, width=300, height=365)
		#Set Transition Frame
		LtoRFrame = tkinter.Frame(self, borderwidth=0, relief='flat')
		LtoRFrame.place(x=300, y=0, height=400, width=10)
		self.LtoRbgimg = tkinter.PhotoImage(file= os.getcwd() + '/images/border_LtoR.gif')
		LtoRLabel = tkinter.Label(LtoRFrame, image = self.LtoRbgimg, borderwidth=0, height=400, anchor=NE).place(relx=0, rely=0)
		#Set Right Frame area
		self.RFrame = tkinter.Frame(self, relief='flat', borderwidth=0)
		self.RFrame.place(x=310, y=0, height= 400, width=490)
		
		#Set the left frame header image
		self.LeftHeaderImg = tkinter.PhotoImage(file= os.getcwd() + '/images/LeftMenuBGImg.gif')
		LeftHeaderLabel = tkinter.Label(self, image = self.LeftHeaderImg, borderwidth=0, height=34, anchor=NE).place(x=0, y=0)
		
		#Establish the white design 
		whiteBorder1 = tkinter.Frame(LFrame, width= 300, height=4).place(x=0, y=33)
		whiteBorder2 = tkinter.Frame(LFrame, width= 300, height=4).place(x=0, y=354)
		
		#Article Holder Frame
		self.articleFrame = tkinter.Frame(LFrame, width=280, height=315, bg='#1B5778') 
		self.articleFrame.place(x=9, y=39)
		
		#Get all the Article IDs and place them in a list
		self.articleIDs = ManageArticles.selectAllArtileIDs()
		#Initiate the global Counter needed to control the creation of article buttons
		self.globalCounter = 0
		#Initiate the page global variable
		self.page = 0
		#Initiate the string of words needed later for placing the aricle content inside
		self.words = ''
		#Initation the list where the article words will be placed in.
		self.wordlist = []
		
		#Call the function to create the article buttons
		self.loadArticleButtons()
		
		
		#Bottom Menu Bar
		BottomLFrame = tkinter.Frame(self, background='#1B5778')
		BottomLFrame.place(x=0, y=362, width=300, height=45) 
		
		#Set up images for the button on the menu bar
		self.imgAddBTN = tkinter.PhotoImage(file= os.getcwd() + '/images/addBTN_mac.gif')
		self.imgREMBTN = tkinter.PhotoImage(file= os.getcwd() + '/images/remBTN_mac.gif')
		#Needed if paging function is activated
		#self.imgUPBTN = tkinter.PhotoImage(file= os.getcwd() + '/images/upBTN_mac.gif')
		#self.imgDWNBTN = tkinter.PhotoImage(file= os.getcwd() + '/images/downBTN_mac.gif')
		
		#Set up buttons in the bottom naviagation bar
		BLFAddBtn = tkinter.Button(BottomLFrame, image = self.imgAddBTN, height=25, bd=0, highlightbackground='#1B5778', command=self.openAddArticleWindow)
		BLFAddBtn.pack(side='left')
		BLFRemBtn = tkinter.Button(BottomLFrame, image = self.imgREMBTN, height=25, bd=0, highlightbackground='#1B5778', command=self.openDeleteArticleWindow)
		BLFRemBtn.pack(side='left')
		#Sets up widgets for multipage views
		#BLFUpBtn = tkinter.Button(BottomLFrame, image = self.imgUPBTN, height=25, bd=0, highlightbackground='#1B5778', command=self.resetGlobalCounter)
		#BLFUpBtn.pack(side='right')
		#BLFDownBtn = tkinter.Button(BottomLFrame, image = self.imgDWNBTN, height=25, bd=0, highlightbackground='#1B5778', command=self.resetGlobalCounter)
		#BLFDownBtn.pack(side='right')
		
		#Name the Variable for the Preview Frame title
		self.articleNamePreview = 'Article Preview: '
		
		#Call the StringVar that will display a preview of the article and set it to none for now
		self.varArticlePreviewContent = tkinter.StringVar()
		self.varArticlePreviewContent.set('')
		
		#Preview frame Area (with title text)
		self.previewFrame = tkinter.LabelFrame(self.RFrame, text=self.articleNamePreview, width=460, height=220).place(relx= 0.03, rely= 0.02)
		self.articlePreviewText = ''
		self.articlePreviewLabel = tkinter.Label(self.previewFrame, textvariable=self.varArticlePreviewContent, wraplength=420)
		self.articlePreviewLabel.place(x=340, y=30)

		#Play Button
		startButton = tkinter.Button(self.RFrame, text="Start Reading", command=self.startReader)
		startButton.place(relx = 0.39, rely=0.66)

		#Adding speed scale
		self.speedScale = tkinter.Scale(self.RFrame, orient='horizontal', length=400, from_=200, to=1000)
		self.speedScale.place(relx = 0.1, rely = 0.78) 
		self.speed = self.speedScale.get()
		#Speed Scale Label
		speedScaleLabel = tkinter.Label(self.RFrame, text="Select desired reading speed.").place(relx=0.33, rely=0.9)
		
		#Instantiate The Varibles
		self.entryVarFileLocation = tkinter.StringVar()
		self.entryVarArticleName = tkinter.StringVar()
		self.entryVarDeleteName = tkinter.StringVar()
		self.entryVarURL = tkinter.StringVar()
		self.entryVarPlainText = tkinter.StringVar()
		self.readerWords = tkinter.StringVar()
		self.readerButtonLabel = tkinter.StringVar()
		self.StartIt = tkinter.Button(self, text='test')
		self.entryVarFileLocation.set('')
		self.entryVarURL.set('http://')
		self.entryVarArticleName.set('')
		self.entryVarPlainText.set('')
		self.readerWords.set('')
		self.copyAddEntry = ScrolledText(self, height=8, width=44, wrap='word', relief='sunken', bd=2)

	#Open add article window
	def openAddArticleWindow(self):
		if(len(self.articleIDs) >= 8):
			self.displayMessageBox('Error','The Article view is already full. Please remove an article before adding another one.')
			return None
		
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
		
	#Open delete Article Window.
	def openDeleteArticleWindow(self):
		j = tkinter.Toplevel(self)
		j.wm_title('Delete an Article - Zip')
		j.wm_geometry('450x368+390+220')
		j.wm_resizable(0,0)
		
		deleteArticeLabel = tkinter.Label(j, text='Article Name to be deleted:').place(x=10, y=10)
		#Get the name of the Entry Label
		self.deleteArticeEntry = tkinter.Entry(j, width=52, textvariable=self.entryVarDeleteName).place(x=10, y=30)
		#Call the sendDeleteArticle() function on button call. This will get the global entryVarDeleteName 
		deleteArticleBTN = tkinter.Button(j, text='Delete it', command=self.sendDeleteArticle).place(x=170, y=81)
		
	#From delete button call, run this function to delete an article based on a given aritcle name
	def sendDeleteArticle(self):
		#Get the entry value for the delete article window from user input
		enteredName = self.entryVarDeleteName.get()
		#Check to see if it is empty
		if(enteredName == ''):
			self.displayMessageBox('Failed', 'Please enter an article name.')
			return None
		#Call the deleteArticle function from the MnageArticles function group (to manipulate the database) As always: Error Checking
		if(ManageArticles.deleteArticle(enteredName)):
			self.displayMessageBox('Success','The article was successfully deleted. Restart the program to view the changes.')
			self.entryVarDeleteName.set('')
		else:
			self.displayMessageBox('Failure','The article was not found. Please check the spelling and try again.')
			
	#Open file dialogue window for the Browse Button in Add Articles Window
	def openFileDiagloge(self):	
		filename = askopenfilename(filetypes=[("Text","*.txt")])
		#Save file path to StringVar entryVarFileLocation
		self.entryVarFileLocation.set(filename)
	
	#Parse Text from user selected file (With error checking)
	def parseTextfromFile(self):
		#Check to see if article view is full (8 article buttons)
		if(len(self.articleIDs) >= 8):
			self.displayMessageBox('Error','The Article view is already full. Please remove an article before adding another one.')
			return None
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
			self.displayMessageBox('Success','The article was successfully added. Restart the program to view the changes.')
			self.entryVarArticleName.set('')
			self.entryVarFileLocation.set('')
		else:
			self.displayMessageBox('Failed', 'An error has occured. Please verify that the path is entered correctly and verify the file location.')#12543
			self.displayMessageBox('Failed', 'The file location field must not be blank')
			
	#Parse text from a URL path
	def parseURLText(self):
		#Check to see if article view is full (8 article buttons)
		if(len(self.articleIDs) >= 8):
			self.displayMessageBox('Error','The Article view is already full. Please remove an article before adding another one.')
			return None
		enteredURL = self.entryVarURL.get()
		words = URLParser.getArticleContent(enteredURL)
		if(words == False):
			self.displayMessageBox('Failed','Not a valid URL field.')
			return None
		enteredName = self.entryVarArticleName.get()
		if(enteredName == ''):
			self.displayMessageBox('Failed', 'Please give the article a name.')
			return None
		result = ManageArticles.addArticle(enteredName, words)
		if(result):
			self.displayMessageBox('Success','The article was successfully added. Restart the program to view the changes.')
			self.entryVarURL.set('')
			self.entryVarArticleName.set('')
		else:
			self.displayMessageBox('Falied', 'An error has occured. Please verify that the URL is entered correctly and verify your internet connection.')
			
	#Parse text from a raw user input
	def parsePlainText(self):
		#Check to see if article view is full (8 article buttons)
		if(len(self.articleIDs) >= 8):
			self.displayMessageBox('Error','The Article view is already full. Please remove an article before adding another one.')
			return None
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
				self.displayMessageBox('Success','The article was successfully added. Restart the program to view the changes.')
				self.copyAddEntry.delete('1.0', END+'-1c')
				self.entryVarArticleName.set('')
			else:
				self.displayMessageBox('Falied', 'An error has occured. Please try again.')
					
	#For Page 
	def resetGlobalCounter(self):
		self.globalCounter = 0
		self.loadArticleButtons()
		
	def loadArticleButtons(self):
		self.globalCounter = 0
		#self.articleIDs
		#self.articleFrame.distroy(All)
				
		#self.articleFrame = tkinter.Frame(LFrame, width=280, height=315, bg='#1B5778') 
		#self.articleFrame.place(x=9, y=39)
		
		if(self.globalCounter == 0):
			i = 0
		else:
			i = 1
		
		if(self.globalCounter == len(self.articleIDs)):
			self.displayMessageBox('Whoops','No more articles to display.')
			
		
		for self.globalCounter in range(self.globalCounter, len(self.articleIDs)):
			
			#Create the button widgets for each id from aricle database
			
			if(self.globalCounter == 0):
				idvar1 = self.articleIDs[self.globalCounter]
				box1 = tkinter.Button(self.articleFrame, text= self.getArticleName(idvar1), justify = LEFT,  background = '#2F6B8C', relief='flat', width=24, fg='white', highlightbackground='#1B5778', activebackground="#437FB4", command=lambda:self.getArticleContent(idvar1)).grid(row=i,column=1, pady=5, padx=5)
				self.globalCounter += 1
				i += 1
				
			elif(((self.globalCounter % 7) == 0) and (self.page >= 1)):
				idvar1 = self.articleIDs[self.globalCounter]
				box1 = tkinter.Button(self.articleFrame, text= self.getArticleName(idvar1), justify = LEFT,  background = '#2F6B8C', relief='flat', width=24, fg='white', highlightbackground='#1B5778', activebackground="#437FB4", command=lambda:self.getArticleContent(idvar1)).grid(row=i,column=1, pady=5, padx=5)
				self.globalCounter += 1
				i += 1
			
			elif(((self.globalCounter % 7) != 0)):
				if (i==1):
					idvar2 = self.articleIDs[self.globalCounter]
					box2 = tkinter.Button(self.articleFrame, text= self.getArticleName(idvar2), justify = LEFT,  background = '#2F6B8C', relief='flat', width=24, fg='white', highlightbackground='#1B5778', activebackground="#437FB4", command=lambda:self.getArticleContent(idvar2)).grid(row=i,column=1, pady=5, padx=5)
					self.globalCounter += 1
					i += 1
				elif (i==2):
					idvar3 = self.articleIDs[self.globalCounter]
					box3 = tkinter.Button(self.articleFrame, text= self.getArticleName(idvar3), justify = LEFT,  background = '#2F6B8C', relief='flat', width=24, fg='white', highlightbackground='#1B5778', activebackground="#437FB4", command=lambda:self.getArticleContent(idvar3)).grid(row=i,column=1, pady=5, padx=5)
					self.globalCounter += 1
					i += 1
				elif (i==3):
					idvar4 = self.articleIDs[self.globalCounter]
					box4 = tkinter.Button(self.articleFrame, text= self.getArticleName(idvar4), justify = LEFT,  background = '#2F6B8C', relief='flat', width=24, fg='white', highlightbackground='#1B5778', activebackground="#437FB4", command=lambda:self.getArticleContent(idvar4)).grid(row=i,column=1, pady=5, padx=5)
					self.globalCounter += 1
					i += 1
				elif (i==4):
					idvar5 = self.articleIDs[self.globalCounter]
					box5 = tkinter.Button(self.articleFrame, text= self.getArticleName(idvar5), justify = LEFT,  background = '#2F6B8C', relief='flat', width=24, fg='white', highlightbackground='#1B5778', activebackground="#437FB4", command=lambda:self.getArticleContent(idvar5)).grid(row=i,column=1, pady=5, padx=5)
					self.globalCounter += 1
					i += 1
				elif (i==5):
					idvar6 = self.articleIDs[self.globalCounter]
					box6 = tkinter.Button(self.articleFrame, text= self.getArticleName(idvar6), justify = LEFT,  background = '#2F6B8C', relief='flat', width=24, fg='white', highlightbackground='#1B5778', activebackground="#437FB4", command=lambda:self.getArticleContent(idvar6)).grid(row=i,column=1, pady=5, padx=5)
					self.globalCounter += 1
					i += 1
				elif (i==6):
					idvar7 = self.articleIDs[self.globalCounter]
					box7 = tkinter.Button(self.articleFrame, text= self.getArticleName(idvar7), justify = LEFT,  background = '#2F6B8C', relief='flat', width=24, fg='white', highlightbackground='#1B5778', activebackground="#437FB4", command=lambda:self.getArticleContent(idvar7)).grid(row=i,column=1, pady=5, padx=5)
					self.globalCounter += 1
					i += 1
				elif (i==7):
					idvar8 = self.articleIDs[self.globalCounter]
					box8 = tkinter.Button(self.articleFrame, text= self.getArticleName(idvar8), justify = LEFT,  background = '#2F6B8C', relief='flat', width=24, fg='white', highlightbackground='#1B5778', activebackground="#437FB4", command=lambda:self.getArticleContent(idvar8)).grid(row=i,column=1, pady=5, padx=5)
					self.globalCounter += 1
					i += 1
			
			else:
				self.globalCounter += 1
				i = 0
				self.page += 1
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
		
		name = self.getArticleName(aID)
		self.articleNamePreview = ('Article Preview: ' + name)
		self.previewFrame = tkinter.LabelFrame(self.RFrame, text=self.articleNamePreview, width=460, height=220).place(relx= 0.03, rely= 0.02)
		wordLength=0
		self.words = ManageArticles.getArticleContent(aID)
		if (len(self.words) >= 500):
			wordLength = 500
		else:
			wordLength = len(self.words)
		self.varArticlePreviewContent.set(self.words[:wordLength])
		self.articlePreviewLabel.place(x=340, y=30)
						
	def displayMessageBox(self, msgTitle, msgMessage):
		tkinter.messagebox.showinfo(msgTitle, msgMessage)
		
	def deleteArticleFromDB(self, articleName):
		result = ManageArticles.deleteArticle(articleName)
		if(result):
			self.displayMessageBox('Success','The article was successfully deleted.')
		else:
			self.displayMessageBox('Oops', 'An Error has occured. Please try again.')
			
	def startReader(self):
		if(self.words == ''):
			self.displayMessageBox('Failed','Plesae select an article first.')
		else:
			self.speed = self.speedScale.get()
			self.wordlist = self.words
			self.wordlist = self.wordlist.split(' ')
			self.openReaderWindow()
			
	def openReaderWindow(self):
		self.r = tkinter.Toplevel(self)
		self.r.wm_title('Reader - Zip')
		self.r.wm_geometry('1300x700+80+50')
		self.r.wm_resizable(0,0)
		self.wordlist = self.words
		self.wordlist = self.wordlist.split(' ')
		
		self.readerWords.set('Press Button to Start')
		
		WORDLabel = tkinter.Label(self.r, textvariable=self.readerWords, height=20, font=("Avenir",40)).pack(anchor='center', pady=85)
		self.StartIt = tkinter.Button(self.r, text='to be added', command=self.checkIfWantToOpenDRW)
		self.StartIt['text'] = 'Start Reader: Press Here'
		self.StartIt.place(relx=0.43, rely=0.90)
		
	def checkIfWantToOpenDRW(self):
		if(self.isItRunning):
			return None
		else:
			self.StartIt['text'] = 'Hold to Pause'
			self.StartIt.place(relx=0.46, rely=0.90)
			self.displayReaderWords()
	
	def displayReaderWords(self):
		self.isItRunning = True
		if(self.indexCounter < len(self.wordlist)):
			WORDLabel = (self.wordlist[self.indexCounter])
			self.indexCounter += 1
			self.readerWords.set(WORDLabel)
			self._time = self.after(round(60000/self.speed), self.displayReaderWords)
		else:
			self.isItRunning = False
		
		
		
if __name__ == "__main__":
	app = mainScreen_tk(None)
	app.title('Zip - RSVP')
	app.geometry('800x400+100+200')
	app.mainloop()