#!/usr/bin/python3

from tkinter import *


def hithere ():
	print("Hi there!!")
def pick():
	print(whichone.get())

root = Tk()
whichone = StringVar()
button = Button(root, text="hi there", command=hithere)
button.pack()

radiobutton = Radiobutton(root,text="This one?",variable=whichone, value="You Picked This one",command=pick)
radiobutton.pack()

radiobutton2 = Radiobutton(root,text="That one?",variable=whichone,value="You picked That one", command=pick)
radiobutton2.pack()

root.mainloop()
