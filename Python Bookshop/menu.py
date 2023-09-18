"""
this is the main module. 
it shows the menu and expects user interaction.

"""
from bookSearch import *
from bookCheckout import *
from bookReturn import *
from bookSelect import *

import matplotlib.pyplot as plt
#The line below enables you to create a canvas on the user interface (no pop-up window)
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg 
from tkinter import *
from matplotlib.figure import Figure

#Data
numbers=[[1,2,3,4],[1,2,2,1]]
numbers2=[[1,2,3,4],[2,1,2,1]]

win = Tk()
win.wn_title("Embedding in Tk")
win.geometry('500x300')

fig=createGraphs(numbers,numbers2)

canvas = FigureCanvasTkAgg(fig, master=win) #A tk.DrawingArea.
canvas.draw()
canvas.get_tk_widget().grid(column=0, row=0)

#Quit button 
button = Button(master=win, text="Quit", command=_quit)
button.grid(column=0, row=1)

win.mainloop()

def createGraphs(data,data2):
    fig=plt.figure(figsize=(5,2))
    ax1=fig.add_subplot(1,2,1)
    ax2=fig.add_subplot(1,2,2)
    ax1.plot(data[0],data[1],"r-")
    ax2.plot(data2[0],data2[1],"r-")
    return fig

def _quit():
    win.quit() #stops mainloop
    win.destroy() #close the windows
    
def display_menu():
    """
    Building Menu Options
    
    """
    print ("\n")
    print ("**********************")
    print ("*------Menu----------*")
    print ("**********************")
    print ("Please select an option below")
    print ("\t(s) to search for a book")
    print ("\t(c) to checkout books")
    print ("\t(r) to return books")
    print ("\t(p) to purchase books")
    print ("\t(e) to exit")


#################################################
#------------------Main-------------------------#
#################################################
testmarks=[]

while True:
    display_menu()
    choice=input("\t\n:>") 
    if choice=="e":
        print("See you next time!")
        break 
    elif choice=="s":
        searchTitle()
    elif choice=="c":
        checkout()
    elif choice=="r":
        returnbook()
    elif choice=="p":
        purchase() #need to come back to this 
        print ("sorry we don't have that option")
