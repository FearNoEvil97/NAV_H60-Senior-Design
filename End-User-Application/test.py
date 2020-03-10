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

#Main UI Elements
root = Tk()
root.geometry('1220x600')

c = Canvas(root, height=320, width=1200, bg="white")
bg = ImageTk.PhotoImage(Image.open("bg.png"))
c.create_image(2,2, anchor=NW, image=bg)
c.pack(side = TOP)

#UI Widgets
progress = Progressbar(root, orient = HORIZONTAL, length = 1200, mode = 'determinate')

numlines = 1
state = "live"

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

def changeNamesButtonCallBack():
    top = Toplevel()
    top.title("About this application...")
    Label(top, text="Tag 1").grid(row=0)
    Label(top, text="Tag 2").grid(row=1)
    Label(top, text="Tag 3").grid(row=2)
    Label(top, text="Tag 4").grid(row=3)
    Label(top, text="Tag 5").grid(row=4)
    Label(top, text="Tag 6").grid(row=5)
    e1 = Entry(top)
    e1.grid(row=0, column=1)
    e1.insert(0,t1name)
    e2 = Entry(top)
    e2.grid(row=1, column=1)
    e2.insert(0,t2name)
    e3 = Entry(top)
    e3.grid(row=2, column=1)
    e3.insert(0,t3name)
    e4 = Entry(top)
    e4.grid(row=3, column=1)
    e4.insert(0,t4name)
    e5 = Entry(top)
    e5.grid(row=4, column=1)
    e5.insert(0,t5name)
    e6 = Entry(top)
    e6.grid(row=5, column=1)
    e6.insert(0,t6name)

    def saveButtonCallBack():
        t1name = e1.get()
        t2name = e2.get()
        t3name = e3.get()
        t4name = e4.get()
        t5name = e5.get()
        t6name = e6.get()

        t1Label["text"] = t1name
        t2Label["text"] = t2name
        t3Label["text"] = t3name
        t4Label["text"] = t4name
        t5Label["text"] = t5name
        t6Label["text"] = t6name

        with open("config.csv", 'w', encoding='utf-8-sig') as csvFile:
            dataWriter = csv.writer(csvFile, delimiter=',')
            dataWriter.writerow(["live", t1name, t2name, t3name, t4name, t5name, t6name])
            csvFile.close()
        top.destroy()

    button = Button(top, text="Save", command=saveButtonCallBack)
    button.grid(row=6)

def helloCallBack():
   print("yay")

progress['value'] = 100

#UI Buttons
crewNameButton = Button(root, text ="Change Crew Names", command = changeNamesButtonCallBack)
exportButton = Button(root, text = "Export To Flash Drive", command = helloCallBack)

#Read configuration data
with open("config.csv", 'r', encoding='utf-8-sig') as configFile:
    csvReader = csv.reader(configFile, delimiter=',')
    for row in csvReader:
        state = row[0]
        if state == "live":
            crewNameButton["state"] = "normal"
            exportButton["state"] = "normal"
        elif state == "replay":
            crewNameButton["state"] = "disabled"
            exportButton["state"] = "disabled"
            t1name = row[1]
            t2name = row[2]
            t3name = row[3]
            t4name = row[4]
            t5name = row[5]
            t6name = row[6]
            t1Label["text"] = t1name
            t2Label["text"] = t2name
            t3Label["text"] = t3name
            t4Label["text"] = t4name
            t5Label["text"] = t5name
            t6Label["text"] = t6name
            with open("data.csv", 'r', encoding='utf-8-sig') as csvFile:
                dataReader = csv.reader(csvFile, delimiter=',')
                numlines = sum(1 for line in dataReader)
                csvFile.close()

    #TODO: Read in names

#TODO: Add version for live version https://stackoverflow.com/questions/3346430/what-is-the-most-efficient-way-to-get-first-and-last-line-of-a-text-file
def moveAndUpdate():
    with open("data.csv", 'r', encoding='utf-8-sig') as csvFile:
        csvReader = csv.reader(csvFile, delimiter=',')
        count = 0
        for row in csvReader:
            count = count + 1
            progress['value'] = (count/numlines)*100

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

t1 = threading.Thread(target=moveAndUpdate, args=())

t1.start()
#c.pack()
progress.pack(pady = 5)
crewNameButton.pack()
exportButton.pack()
root.mainloop()
