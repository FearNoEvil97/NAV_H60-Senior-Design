from tag import *
from tkinter.ttk import *
from tkinter import *
from PIL import ImageTk, Image
import threading
from time import sleep
import math

import csv

minDistance = 5

t1name = "Phillip Gaskin"
t2name = "Josh Hutchins"
t3name = "James Anderson"
t4name = "Jacob Beach"
t5name = "Zephan Spencer"
t6name = "Captain Dirk Diggler"

root = Tk()
root.geometry('1220x600')

c = Canvas(root, height=320, width=1200, bg="white")
bg = ImageTk.PhotoImage(Image.open("bg.png"))
c.create_image(2,2, anchor=NW, image=bg)
c.pack(side = TOP)
progress = Progressbar(root, orient = HORIZONTAL, length = 1200, mode = 'determinate')

numlines = 1

with open("data.csv", 'r', encoding='utf-8-sig') as csvFile:
    csvReader = csv.reader(csvFile, delimiter=',')
    numlines = sum(1 for line in csvReader)
    csvFile.close()

def helloCallBack():
   print("yay")

progress['value'] = 35
B = Button(root, text ="Change Crew Names", command = helloCallBack)

def moveAndUpdate():
    with open("data.csv", 'r', encoding='utf-8-sig') as csvFile:
        csvReader = csv.reader(csvFile, delimiter=',')
        count = 0
        for row in csvReader:
            count = count + 1
            progress['value'] = (count/numlines)*100
            #xcoords = [int(row[0]), int(row[2]), int(row[4]), int(row[6]), int(row[8]), int(row[10])]
            #ycoords = [int(row[1]), int(row[3]), int(row[5]), int(row[7]), int(row[9]), int(row[11])]

            #for x in range(0, len(xcoords)):
            #    for index in range(0, len(xcoords)):
            #        distance = math.sqrt(math.pow(xcoords[x] - xcoords[index], 2) + math.pow(math.pow(ycoords[x] - ycoords[index], 2)))
            #        if distance < 5:
            #            print("Distance less than specified!")

            tag1.setCoords(int(row[0]), int(row[1]))
            tag2.setCoords(int(row[2]), int(row[3]))
            tag3.setCoords(int(row[4]), int(row[5]))
            tag4.setCoords(int(row[6]), int(row[7]))
            tag5.setCoords(int(row[8]), int(row[9]))
            tag6.setCoords(int(row[10]), int(row[11]))

            tag1.updatePosition(c)
            tag2.updatePosition(c)
            tag3.updatePosition(c)
            tag4.updatePosition(c)
            tag5.updatePosition(c)
            tag6.updatePosition(c)

            root.update()
            sleep(0.1)

tag1 = tag(t1name, 5, 5, "t1.png", c)
tag2 = tag(t2name, 20, 3, "t2.png", c)
tag3 = tag(t3name, 10, 1, "t3.png", c)
tag4 = tag(t4name, 11, 1, "t4.png", c)
tag5 = tag(t5name, 11, 4, "t5.png", c)
tag6 = tag(t6name, 12, 3, "t6.png", c)

cLegend = Canvas (root, height = 280, width = 40)
cLegend.create_image(5,5, anchor = NW, image=tag1.imageObject)
cLegend.create_image(5,45, anchor = NW, image=tag2.imageObject)
cLegend.create_image(5,85, anchor = NW, image=tag3.imageObject)
cLegend.create_image(5,125, anchor = NW, image=tag4.imageObject)
cLegend.create_image(5,165, anchor = NW, image=tag5.imageObject)
cLegend.create_image(5,205, anchor = NW, image=tag6.imageObject)
cLegend.place(x=0, y=350, anchor=NW)

t1Label = Label(root, text=t1name, font=("Helvetica", 18))
t1Label.place(x = 50, y = 350 + 5)

t2Label = Label(root, text=t2name, font=("Helvetica", 18))
t2Label.place(x = 50, y = 350 + 45)

t3Label = Label(root, text=t3name, font=("Helvetica", 18))
t3Label.place(x = 50, y = 350 + 85)

t4Label = Label(root, text=t4name, font=("Helvetica", 18))
t4Label.place(x = 50, y = 350 + 125)

t5Label = Label(root, text=t5name, font=("Helvetica", 18))
t5Label.place(x = 50, y = 350 + 165)

t6Label = Label(root, text=t6name, font=("Helvetica", 18))
t6Label.place(x = 50, y = 350 + 205)

t1 = threading.Thread(target=moveAndUpdate, args=())

t1.start()
#c.pack()
progress.pack(pady = 5)
B.pack()
root.mainloop()
