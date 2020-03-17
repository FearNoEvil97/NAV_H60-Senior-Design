from tkinter import *
from PIL import ImageTk, Image
from time import sleep

class tag:
    inch = 3.33 #1200(pixels in 30 feet)/360(inches in 30 feet)
    size = 25
    def __init__(self, name, x, y, imageName, canvas):
        self.name = name
        self.x = x
        self.y = y
        self.image = Image.open(imageName)
        self.resizedImage = self.image.resize((self.size,self.size), Image.ANTIALIAS)
        self.imageObject = ImageTk.PhotoImage(self.resizedImage)
        self.thing = canvas.create_image((self.x*self.inch), (self.y*self.inch), anchor=NW, image=self.imageObject)
        self.inch = 3.33

    def setCoords(self, x, y):
        self.x = x #Meters to inches conversion *39.3701
        self.y = y
        print(self.name + " x: " + str(x))
        print(self.name + " y: " + str(y))

    def updatePosition(self, canvas):
        canvas.coords(self.thing, (self.x*self.inch)-10, (self.y*self.inch)-10)
