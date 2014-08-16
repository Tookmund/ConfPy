#!/usr/bin/python3

from tkinter import *
import json
import sys

class window:
	
	def editpopup(self,window,label):
		self.top = Toplevel(window)
		Label(self.top,text=label).pack()
		value = StringVar()
		entry(self.top,value)
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
		pass #popup? some way to get scale values...

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
		self.option(key,"Scale","scale")
		
	def erroroptions(self,key,val):
		pass

	def submit(self):
		self.output = open(self.outputfile.get(),"w")
		for k,v in self.final.items():
			self.finaljson[k] = v.get()
		json.dump(self.finaljson,self.output)
		print("Dumped")
		print(self.finaljson)
		print("In")
		print(self.outputfile.get())
	
	def renderwindow(self):
		for k,v in self.conf.items():
			self.final[k] = StringVar()
			self.root[k] = Frame(self.main,bd=5,relief=RIDGE)
			if (isinstance(v,str)):
				print("found string: ",v)
				self.stringoptions(k,v)
			elif (isinstance(v,int)):
				print("found int: ",v)
				self.intoptions(k,v)
			else:
				self.erroroptions(k,v)
		
		for k,v in self.root.items():
			v.pack()
			
		Label(self.main,text="Output File (JSON)").pack()
		Entry(self.main,textvariable=self.outputfile).pack()
		Button(self.main,text="Submit",command=self.submit).pack()
		self.main.mainloop()
		
		
	def __init__(self,file):
		self.main = Tk()
		self.main.title = "ConfPy"
		self.final = {}
		self.finaljson = {}
		self.root = {}
		self.outputfile = StringVar()
		self.jfile = open(file,"r")
		self.conf = json.load(self.jfile)
	
if (__name__ == "__main__"):
	app = window(sys.argv[1])
	app.renderwindow()
