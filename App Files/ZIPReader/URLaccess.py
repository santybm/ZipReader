import urllib.request
import re
import unicodedata
import time

def URL_Parse(URL):
	#opens requested webpage and converts it into python text.
	try:
		page = urllib.request.urlopen(URL)
	except:
		return(False)
	uniText = page.read().decode('utf8')
	text = str(unicodedata.normalize('NFKD', uniText).encode('ascii','ignore'))
	articleText = str()
	
	#separates all data designated by <p>-</p>
	for x in range (0,len(text)):
		startP = text[x:x+3]
		if '<p>' in startP:
			startPoint = x+3
			for x in range (startPoint,len(text)):
				endP = text[x:x+4]
				if '</p>' in endP:
					endPoint = x
					articleText += text[startPoint:endPoint]
					break
					
	startPlace = 0
	endPlace = 0
	articleText_Stage2 = ''
	articleText_Final = ''
	
	##pulls all supperflous information within paragragh tags signalled by '<' and '>'
	for x in range (0,len(articleText)):
		counter = articleText[x]
		if '<' in counter:
			startPlace = x
			articleText_Stage2 +=' '+ articleText[endPlace:startPlace]
		elif '>' in counter:
			endPlace = x+1

	#final scrub of extra information
	articleText_Stage3 = articleText_Stage2.replace('&rsquo;','') 
	articleText_Stage4 = articleText_Stage3.replace('&nbsp;','')
	articleText_Stage5 = articleText_Stage4.replace('&mdash;','')
	articleText_Final = articleText_Stage5.replace('\\','')
	
	return (articleText_Final)

def inputwordsperminute(x,data):
    data = data.split(' ')
    for w in range (0, len(data)):
        print (data[w])
        time.sleep((60/x))

def parseFiletoWords(fileLocation):
	try:
		fileHandle = open (fileLocation, 'r' )
	except:
		return (False)
	str = fileHandle.read()
	fileHandle.close()
	return (str)
	
#parsedData = URL_Parse('http://www.theverge.com/2013/12/5/5175850/hp-chromebook-14-review')
#inputwordsperminute(600,parsedData)
