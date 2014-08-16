#!/usr/bin/python3

from tkinter import *
from tkinter import simpledialog
#import tkinter.messagebox
#import tkinter.simpledialog
import json
import sys

class confpy:

	def popup(self,window,label):
		self.top = Toplevel(window)
		Label(self.top,text=label).pack()
		value = StringVar()
		entry(self.top,value)
		window.wait_window(self.top)
		return value.get()
	
	def label(self,window,text):
		retval = Label(window,text=text)
		retval.pack()
		return retval
	
	def entry(self,window,var):
		retval = Entry(window,textvariable=var)
		retval.pack()
		return retval

	def option(self,key,text,val):
		retval = Radiobutton(self.root[key],text=text,variable=self.final[key],value=val)
		retval.pack()
		return retval
		
	def scale(self):
		title = StringVar()
		prompt = StringVar()
		title.set("Minimum Value")
		prompt.set("Enter minimum scale value")
		self.min[self.k] = simpledialog.askinteger(title.get(),prompt.get())
		title.set("Maximum Value")
		prompt.set("Enter maximum scale value")
		self.max[self.k] = simpledialog.askinteger(title.get(),prompt.get())
	def stringoptions(self,key,val):
		#print(val)
		self.label(self.root[key],key)
		self.option(key,"Inputbox","entry")
		#empty = StringVar()
		#entry(root,empty)
		self.option(key,"TextBox","text")
		#Text(root).pack()
		#option

	def intoptions(self,key,val):
		self.label(self.root[key],key)
		self.option(key,"Inputbox","entry")
		Radiobutton(self.root[key],text="Scale",variable=self.final[key],value="scale",command=self.scale).pack()
		
	def erroroptions(self,key,val):
		tkinter.messagebox.showerror(key,"'%s' not a valid int or string" % val)
		

	def submit(self):
		self.output = open(self.outputfile.get(),"w")
		for k,v in self.final.items():
			self.finaljson[k] = v.get()
			if(self.min[k] and self.max[k]):
				self.finaljson[k] = [self.min[k],self.max[k]]
				
		json.dump(self.finaljson,self.output)
		print("Dumped")
		print(self.finaljson)
		print("In")
		print(self.outputfile.get())
	
	def renderwindow(self):
		for self.k,self.v in self.conf.items():
			self.final[self.k] = StringVar()
			self.root[self.k] = Frame(self.main,bd=5,relief=RIDGE)
			if (isinstance(self.v,str)):
				print("found string: ",self.v)
				self.stringoptions(self.k,self.v)
			elif (isinstance(self.v,int)):
				print("found int: ",self.v)
				self.intoptions(self.k,self.v)
			else:
				self.erroroptions(self.k,self.v)
		
		for k,v in self.root.items():
			v.pack()
			
		Label(self.main,text="Output File (JSON)").pack()
		Entry(self.main,textvariable=self.outputfile).pack()
		Button(self.main,text="Submit",command=self.submit).pack()
		self.main.mainloop()
		
		
	def __init__(self,file,window):
		self.main = window
		self.main.title = "ConfPy"
		self.final = {}
		self.finaljson = {}
		self.root = {}
		self.outputfile = StringVar()
		self.jfile = open(file,"r")
		self.conf = json.load(self.jfile)
	
if (__name__ == "__main__"):
	main = Tk()
	main.wm_title("ConfPy")
	app = confpy(sys.argv[1],main)
	app.renderwindow()
