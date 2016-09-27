######### WARNING #########
#Embedly dependency required. 
from embedly import Embedly
import re

#How to get this thing to work
#Look at the location of this file:
#     print(re.__file__)
#Run this code in terminal 
#   pip install embedly
#  or -- get the embedly.zip and unzip it --> save the two folders inside to the location above from outside of the terminal. 
#then it will work.

import re

client = Embedly('421bf471c4f04eda8520febc129506b8')

def takeOutTags(data):
	p = re.compile(r'<.*?>')
	return p.sub('', data)
	
def takeOutUChar(data):
	p = re.compile(r'&#220;')
	return p.sub('ü', data)
	
def takeOutNewLine(data):
	p = re.compile(r'\n')
	return p.sub('', data)

def getArticleContent(url):
	
	obj = client.extract(url)
	rawArticle = str(obj['content'])
	
	beautifulString = takeOutTags(rawArticle)
	evenBetterString = takeOutUChar(beautifulString)
	evenBetterTwo = takeOutNewLine(evenBetterString)
	return(evenBetterTwo)