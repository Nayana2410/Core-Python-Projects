#import module
from tkinter import *

#create a root window
root = Tk()

#create a canvas as a child to root window
c = Canvas(root, bg = 'white', height=700, width = 1200)

#copy images into file
file1 = PhotoImage(file='C:/Users/nayan/Desktop/gif/giphy.gif')
file2 = PhotoImage(fil='C:/Users/nayan/Desktop/gif/puppy-cute.gif')

#display the image in the canvas in NE direction.
#when mouse is placed on cat image, we can see puppy image
id = c.create_image(500,200, anchor = NE, image=file1, activeimage=file2)

#display some text bellow the image
id =c.create_text(500,500,text='This is a thrilling photo', font=('Helvetica',30,'bold',), fill='blue')

#add canvas to the root
c.pack()

#wait for any events
root.mainloop()
