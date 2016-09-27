#Won't work if you run it. Just an example

import sqlite3 as lite

def import_newID(cid:int):
    
    #call the function to hash the raw tapped Card ID Number. Store it to variable hashed_Id
    hashed_Id = hash_raw(cid) 
    con = lite.connect('cardSwipe')
    
    with con:
        cur = con.cursor()    
        cur.execute("""INSERT INTO accessList(id, cardID, tapCount) VALUES (?,?,?);""", (None, hashed_Id, 0))
    
    con.close()
    print('Card Added')

# <codecell>

def search_cardID(raw_tap:int)->bool:
    
    hashed_Id = hash_raw(raw_tap)
    con = lite.connect('cardSwipe')   
    
    with con:
        cur = con.cursor()
        cur.execute("""SELECT cardID FROM accessList WHERE cardID=?;""", (hashed_Id,))
        
        for row in cur:
            if(row == None):
                return False
            else:
                return True
            

# <codecell>

#import_newID('54345244')
#if(search_cardID('42342342')):
#    print('Welcome')
#else:
#    print('Access Denied')

# <codecell>