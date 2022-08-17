#write a python program to check fonts in tkinter module
#importing necessary module

from tkinter import*
from tkinter import font

#create a root window
root=Tk()

#get all the stupported font families
list_fonts = list(font.families())

#displaying  font
print(list_fonts)
