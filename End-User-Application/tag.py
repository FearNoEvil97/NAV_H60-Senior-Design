from tkinter import *
from PIL import ImageTk, Image
from time import sleep

class tag:
    tagDiameter = 35
    squareSideLength = 40
    center = (squareSideLength/2)-(tagDiameter/2)
    thing = 0

    def __init__(self, name, x, y, imageName, canvas):
        self.name = name
        self.x = x
        self.y = y
        self.imageObject = ImageTk.PhotoImage(Image.open(imageName))
        self.thing = canvas.create_image(((self.x-1)*self.squareSideLength)+self.center+2, ((self.y-1)*self.squareSideLength)+self.center+2, anchor=NW, image=self.imageObject)
    
    def setCoords(self, x, y):
        self.x = x
        self.y = y
        print(self.name + " x: " + str(x))
        print(self.name + " y: " + str(y))
    
    def updatePosition(self, canvas):
        canvas.coords(self.thing, ((self.x-1)*self.squareSideLength)+self.center+2, ((self.y-1)*self.squareSideLength)+self.center+2)
