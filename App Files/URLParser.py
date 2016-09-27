######### WARNING #########
#Embedly dependency required. 
try:
	from embedly import Embedly
except:
	import re
	print ('Dependency not found. Please install with \'pip install embedly\' or by placing the unzipped embedly folder in the python /site-packages/ folder. Use this file path to find the correct python directory')
	print (re.__file__)

import re

#How to get this thing to work
#Look at the location of this file:
#     print(re.__file__)
#Run this code in terminal 
#   pip install embedly
#  or -- get the embedly.zip and unzip it --> save the two folders inside to the location above from outside of the terminal. 
#then it will work.

#private API key
client = Embedly('421bf471c4f04eda8520febc129506b8')

def takeOutTags(data):
	p = re.compile(r'<.*?>')
	return p.sub('', data)
	
def takeOutUChar(data):
	p = re.compile(r'&#220;')
	return p.sub('ü', data)
	
def takeOutAChar(data):
	p = re.compile(r'&#225;')
	return p.sub('á', data)
	
def takeOutNChar(data):
	p = re.compile(r'&#241;')
	return p.sub('ñ', data)
	
def takeOutEChar(data):
	p = re.compile(r'&#233;')
	return p.sub('é', data)
	
def takeOutNNChar(data):
	p = re.compile(r'&#209;')
	return p.sub('Ń', data)
	
def takeOutIChar(data):
	p = re.compile(r'&#237;')
	return p.sub('í', data)

def takeOutOChar(data):
	p = re.compile(r'&#243;')
	return p.sub('ó', data)
	
def takeOutUUChar(data):
	p = re.compile(r'&#250;')
	return p.sub('ú', data)
	
def takeOutNewLine(data):
	p = re.compile(r'\n')
	return p.sub(' ', data)

def getArticleContent(url):
	
	try:
		obj = client.extract(url)
		rawArticle = str(obj['content'])
		
		beautifulString = takeOutTags(rawArticle)
		evenBetterString = takeOutUChar(beautifulString)
		evenBetterTwo = takeOutNewLine(evenBetterString)
		evenBetterThree = takeOutAChar(evenBetterTwo)
		evenBetterFour = takeOutNChar(evenBetterThree)
		evenBetter5 = takeOutIChar(evenBetterFour)
		evenB6 = takeOutOChar(evenBetter5)
		eb7 = takeOutUUChar(evenB6)
		eb8 = takeOutNNChar(eb7)
		eb9 = takeOutEChar(eb8)
		return(eb9)
		
	except:
		return(False)