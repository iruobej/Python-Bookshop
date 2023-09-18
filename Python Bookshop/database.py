from datetime import date
"""
Python Module 
file operation functions

"""

#read and return a list of the all the records in book_info.txt
def read_info():
    """
    no input parameters
    it returns a list
    
    Getting the student test results from the text file
      
    """
    bkrecords=[]
    f=open("Book_Info.txt","r")
    for record in f:
        cleanrecord=record.strip()
        inforecord=cleanrecord.split(",")
        bkrecords.append(inforecord)
    print("Book records have been read successfully. ")

    f.close()
    return bkrecords

#creating a list and adding every record in logfile.txt to it, then display it 
def read_log():
    """
    no input parameters
    it returns a list
    
    Getting the student test results from the text file
      
    """
    logrecords=[]
    f=open("logfile.txt","r")
    for line in f:
        line=line.strip()
        log=line.split(",")
        logrecords.append(log)
    f.close()
    return logrecords

def read_log2():
    file = open("logfile.txt","r")
    a = file.readlines()
    file.close()
    return a 
"""
Given the (correct) book ID and member ID, this function will add a new record
to logfile.txt with the date of reservation

"""
def reserve(b_id,m_id):
    f=open("logfile.txt","a")
    today = date.today()
    newrecord=b_id+","+m_id+","+today+","+" "+","+" "+","+"N"+'\n'
    #logrecords.append(newrecord)
    f.writeline(newrecord)
    f.close()

"""
This will write to logfile.txt by updating the correct of column of a given
record
"""
def dcheckout(b_id,m_id):
    f=open("logfile.txt","w")
    today = date.today()
    for record in f:
        freshrecord=record.strip()
        log=freshrecord.split(",")
        logrecords.append(log)
        if record[0] == b_id and record[1] == m_id:
            record[3] = today
            record[5] = "N"
        f.writeline(logrecords)
    f.close()

"""
This will check every record in logfile.txt, and once it finds the record
with the right bookidand empty reserve column, it will add the correct date
to that column
"""

def returnbk(bookid):
    f=open("logfile.txt","w") 
    for record in f:
        newrec = record.split(",")
        if record[0] == bookid and record[4] == " ":
            today = date.today()
            record[4] == today 

    f.close() 

def write_log(records):
    f=open("logfile.txt","w")
    for rec in records:
        newrecord= rec[0]+","+rec[1]+","+rec[2]+","+rec[3]+","+rec[4]+","+rec[5]+'\n'
        f.write(newrecord)
    f.close()

def wlog2(logrecords):
    write_file = open("logfile.txt", "w")
    write_file.writelines(logrecords)
    write_file.close()

"""    
def append(b_id, m_id):
    
    #bklist = read_log()
    today = date.today().strftime('%d/%m/%Y')
    f=open("logfile.txt","a")
    newrecord= str(b_id)+","+str(m_id)+","+" "+","+str(today)+","+" "+","+" "+'\n'
    print(newrecord)
    f.write(newrecord)
    f.close()
"""

