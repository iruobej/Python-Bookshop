#Importing functions from database.py to read and write to the text files
from database import *
def returnbook ():
    no_of_returns = int(input("How many books are being returned?: "))
    #bklist is a list that holds all the records in in logfile.txt
    bklist = read_log()
    #Enables user to return multiple books at one time
    for i in range (0, no_of_returns):
        bookid = int(input("Please enter the ID of book number: "))
        #Validating the Book ID given by the user
        if bookid>=1 and bookid<= 20:
            returned = False
            for record in bklist:
                #Finds the record in the list with the matching book ID and empty 'return' slot
                if record[0] == str(bookid) and record[4] == " ":
                    today = date.today().strftime('%d/%m/%Y')
                    record[4] = str(today)
                    returned = True
            if returned == False:
                print("Error: Book not returned successfully")
            else:
                print("Book returned successfully")
        else:
            print("Error: Invalid ID")
    #wiping logfile.txt and replacing it with the modified list
    write_log(bklist)

returnbook()
