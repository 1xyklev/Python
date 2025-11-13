from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename

readFile = askopenfilename()
if( readFile != None):
    infile = open(readFile, "r")

s = infile.read()
print(s)
infile.close() 