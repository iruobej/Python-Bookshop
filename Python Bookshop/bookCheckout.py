from database import *
# function to checkout books
def checkout():
    no_books = int(input("How many books are you checking out?: "))
    memberid = int(input("Please enter your Member ID: "))
    #creating the current date in a dd/mm/yyyy format
    today = date.today().strftime('%d/%m/%Y')
    for i in range(0,no_books):
        #Validating the Member ID
        if memberid>=1000 and memberid<=9999:
                bookid = int(input("Please enter your book's ID: "))
                #Validating the Book ID
                if bookid>=1 and bookid<=20:
                    #all the logs in logfile.txt are stored in the variable logrecords
                    logrecords=read_log()
                    found = False
                    for srec in logrecords[1:]:
                        
                        if str(bookid) == srec[0] and srec[1] == str(memberid) and srec[2] != " ":
                            srec[3] = str(today)
                            print("Hello")
                            found = True
                    #If there is no existing record with the Book ID and Member ID given that has also been reserved, this will append a new record to 
                    if found == False:
                        #newrecord= str(bookid)+","+str(memberid)+","+" "+","+str(today)+","+" "+","+" "+'\n'
                        newrecord = [str(bookid), str(memberid), " ", str(today), " ", "N"]
                        logrecords.append(newrecord) 
                    write_log(logrecords)
                else:                        
                    print("Error: Invalid Book ID")
        else:
            print("Error: Invalid Member ID")

checkout()

