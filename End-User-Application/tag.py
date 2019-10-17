from tkinter import *
from PIL import ImageTk, Image
class tag:
    tagDiameter = 35
    squareSideLength = 40
    center = (squareSideLength/2)-(tagDiameter/2)

    def __init__(self, name, x, y, imageName, canvas):
        self.name = name
        self.x = x
        self.y = y
        self.imageObject = ImageTk.PhotoImage(Image.open(imageName))
        canvas.create_image((self.x*self.squareSideLength)+self.center+2, (self.y*self.squareSideLength)+self.center+2, anchor=NW, image=self.imageObject)
    
    def setCoords(self, x, y):
        self.x = x
        self.y = y
    
    def updatePosition(self, canvas):
        canvas.coords(self.imageObject, self.x, self.y)
        canvas.after(5000, updatePosition(canvas))
