from tkinter import *

root = Tk()
"""
# Creating a label widget
myLable = Label(root, text = "Hello World!")
#show it onto the screen
myLable.pack()
"""
#Create Labels widget
myLable1 = Label(root, text = "Hello \n World!")
myLable2 = Label(root, text = "My name is Binh")
#Show it onto screen

myLable1.grid(row = 0, column = 0)
myLable2.grid(row = 1, column = 0)

root.mainloop()

                
