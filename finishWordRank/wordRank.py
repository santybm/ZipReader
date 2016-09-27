from string import punctuation
from operator import itemgetter
import urllib
import re
import URLParser

def wrcurl(url,word2):
	
	words = {}
	wordList = []
	words_gen = URLParser.getArticleContent(url)
	
	words_gen = words_gen.lower()
	
	wordList = re.sub("[^\w]", " ",  words_gen).split()
	
	#print(wordList)
	for key in wordList:
		if key in words:
			words[key] += 1
		else:
			words[key] = 1
		
	N =len(words.keys())
	#print(words)
		
	top_words = sorted(words.items(), key=itemgetter(1), reverse=True)[:N]
	
	#print(top_words)
	
	
	for i, (word, frequency) in enumerate(top_words):
		if(word2 in word):
			print("%s %d %d" % (word, i+1, frequency))
			break
			
			
#printfreq('An webpage url', 'word you are looking to find ranked')
#Example Site and word
#printfreq('http://blog.embed.ly/javascript-hackathon-downcityjs-betaspring','an')