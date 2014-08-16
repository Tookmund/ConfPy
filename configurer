#!/usr/bin/python3

from tkinter import *
from tkinter.simpledialog import *
from tkinter import ttk, messagebox
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
		self.min[self.k] = askinteger('Minimum Value', 'Enter minimum scale value')
		self.max[self.k] = askinteger('Maximum Value', 'Enter maximum scale value')
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
	
	def booloptions(self,key,value):
		self.label(self.root[key],key)
		self.option(key,"1/0","10")
		self.option(key,"True/False","tf")
		
	def erroroptions(self,key,val):
		messagebox.showerror(key,"'%s' not a valid int or string" % val)
		

	def submit(self):
		self.output = open(self.outputfile.get(),"w")
		for k,v in self.final.items():
			self.finaljson[k] = v.get()
			if(k in self.min and k in self.max):
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
				print("found string:",self.v)
				self.stringoptions(self.k,self.v)
			elif (isinstance(self.v,bool)):
				print("found bool:",self.v)
				self.booloptions(self.k,self.v)
			elif (isinstance(self.v,int) or isinstance(self.v,float)):
				print("found int:",self.v)
				self.intoptions(self.k,self.v)
			
			
			else:
				self.erroroptions(self.k,self.v)
		i = 0
		j = 0
		for k,v in self.root.items():
			v.grid(row=i,column=j)
			j += 1
			if (j > 10):
				i += 1
				j = 0
		i += 1
		j = 0
		Label(self.main,text="Output File (JSON)").grid(row=i,column=j)
		i+=1
		Entry(self.main,textvariable=self.outputfile).grid(row=i,column=j)
		i+=1
		Button(self.main,text="Submit",command=self.submit).grid(row=i,column=j)
		self.main.mainloop()
		
		
	def __init__(self,file,window):
		self.main = window
		self.main.title = "ConfPy"
		self.final = {}
		self.finaljson = {}
		self.root = {}
		self.min = {}
		self.max = {}
		self.outputfile = StringVar()
		self.jfile = open(file,"r")
		self.conf = json.load(self.jfile)
	
if (__name__ == "__main__"):
	main = Tk()
	main.wm_title("ConfPy")
	try:
		app = confpy(sys.argv[1],main)
	except IndexError:
		print("Please provide an filename")
	else:
		app.renderwindow()
