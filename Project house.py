#import module
from tkinter import *

#create a root window
root = Tk()

#create a canvas as a child to root window, Background color is dark blue
c = Canvas(root, bg='#091e42', height=700, width=1200)

#create a house
c.create_polygon(600,250,700,200,800,250,800,400,600,400, width=2, fill='yellow',
                 outline='red')
c.create_line(600,250,800,250,width=2, fill='red')
c.create_rectangle(650,275,750,375, fill='red')

#create 3 bush at left side of house
x1,y1=0,350
x2,y2=200,450
for i in range(3):
    c.create_arc(x1,y1,x2,y2, start=0, extent=180, fill='green')
    x1+=200
    x2+=200

#create a bushesh at right side of the house
c.create_arc(800,350,1000,450, start=0, extent=180, fill='green')
c.create_arc(100,350,1200,450,start=0,extent=180,fill='green')

#display moon image
file1 =PhotoImage(file='')
c.create_image(10,10,anchor=NW,image=file1)

#display some text below the image
id = c.create_text(600,600,text='My Happy Home!',font=('Hevetica',30,'bold'), fill='magenta')

#add canvas to the root
c.pack()

#wait for any events
root.mainloop()

