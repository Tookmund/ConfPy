#!/usr/bin/python3
import json 

inp = input("Enter json: ")

jsonstr = json.loads(inp)

for i in jsonstr:
	print(i)
	print(jsonstr[i])
