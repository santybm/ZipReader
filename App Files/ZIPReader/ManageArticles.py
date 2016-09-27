import sqlite3 as lite

# These functions are in charge of managing the content, name, and ID of the articles in the zipData database. 

#Add an Article to the database given a title and a string of words
def addArticle(title, string):
	try:
		con = lite.connect('zipData')
		
		with con:
			cur = con.cursor()
			cur.execute("""INSERT INTO articles(ID,Name,Content) VALUES (?,?,?);""", (None, title, string))
		con.close
		return (True)
	
	except ValueError:
		return (False)

#Delete an article from the database based on the Article Name
def deleteArticle(title):
	try:
		con = lite.connect('zipData')
		with con:
			cur = con.cursor()
			cur.execute("""DELETE FROM articles WHERE Name = '%s';""" % (title))
		con.close
		return (True)
	except ValueError:
		return (False)
		
#Select all the Article IDs from the database
def selectAllArtileIDs():
	ids = []
	try:
		con = lite.connect('zipData')
		with con:
			cur = con.cursor()
			cur.execute('SELECT ID FROM articles')
			for row in cur.fetchall():
				ids.append(row[0])
		con.close
		return (ids)
	except ValueError:
		return(False)
		
#Select the article content from the database based on the ID
def getArticleContent(aID):
	try:
		con = lite.connect('zipData')
		with con:
			cur = con.cursor()
			cur.execute("""SELECT Content FROM articles WHERE ID = '%s';""" % (aID))
			for row in cur.fetchone():
				return(row)
			con.close
	except ValueError:
		return(False)
		

		