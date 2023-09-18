from database import *
# searching through the text files for a book based on a given title, provided by the user
def searchTitle():
    title = input("Please enter the title of the book you wish to search:")
    #saves a list of all the records in book_info.txt into a variable 'bkrecords'
    bkrecords = read_info()
    found = []
    for i in bkrecords:
        if i[2] == title:
            bkid = i[0]
            logrecords = read_log()
            for j in logrecords:
                if j[0] == bkid: 
                    found.append(j + [title])
    return found
                


                    
                




    
    
