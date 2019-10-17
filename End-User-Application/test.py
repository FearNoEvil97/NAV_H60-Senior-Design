import 
from tag import *
from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.geometry('1220x600')

c = Canvas(root, height=320, width=1200, bg="white")
bg = ImageTk.PhotoImage(Image.open("bg.png"))
c.create_image(2,2, anchor=NW, image=bg)
c.pack(side = TOP)

tag1 = tag("pbillip", 5, 5, "t1.png")
tag1.updatePosition(c)
c.pack()

root.mainloop()