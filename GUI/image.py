from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Learn to code at my home!")
root.iconbitmap("D:/binh bui/python/GUI/icon.ico")



button_quit = Button(root, text = "Exit Program", command = root.quit)
button_quit.pack()
root.mainloop()
