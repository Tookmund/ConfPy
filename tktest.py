#!/usr/bin/python3

from tkinter import *

def hithere ():
	print("Hi there!!")

root = Tk()
button = Button(root, text="hi there", command=hithere)
button.pack()
root.mainloop()
