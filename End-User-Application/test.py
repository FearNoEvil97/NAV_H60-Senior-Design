from tag import *
from tkinter.ttk import *
from tkinter import *
from PIL import ImageTk, Image
import threading
from time import sleep
import math
import datetime

import csv

minDistance = 5

t1name = "Phillip Gaskin"
t2name = "Josh Hutchins"
t3name = "James Anderson"
t4name = "Jacob Beach"
t5name = "Zephan Spencer"
t6name = "Captain Dirk Diggler"

nanCounts = [0,0,0,0,0,0]

#Main UI Elements
root = Tk()
root.geometry('1220x650')

c = Canvas(root, height=320, width=1200, bg="white")
bg = ImageTk.PhotoImage(Image.open("bg.png"))
c.create_image(2,2, anchor=NW, image=bg)
c.pack(side = TOP)

#UI Widgets
progress = Scale(root, orient = HORIZONTAL, length = 1200, showvalue=0)

numlines = 1
state = "live"
paused = True

t1Label = Label(root, text=t1name, font=("Helvetica", 18))
t1Label.place(x = 50, y = 400 + 5)

t2Label = Label(root, text=t2name, font=("Helvetica", 18))
t2Label.place(x = 50, y = 400 + 45)

t3Label = Label(root, text=t3name, font=("Helvetica", 18))
t3Label.place(x = 50, y = 400 + 85)

t4Label = Label(root, text=t4name, font=("Helvetica", 18))
t4Label.place(x = 50, y = 400 + 125)

t5Label = Label(root, text=t5name, font=("Helvetica", 18))
t5Label.place(x = 50, y = 400 + 165)

t6Label = Label(root, text=t6name, font=("Helvetica", 18))
t6Label.place(x = 50, y = 400 + 205)

timeLabel = Label(root, text="00:00:00")
timeLabel.place(x=5, y=350)

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

def playPauseCallBack():
    global paused
    if paused:
        paused = False
    else:
        paused = True
    print(paused)

progress.set(100)

#UI Buttons
crewNameButton = Button(root, text ="Change Crew Names", command = changeNamesButtonCallBack)
exportButton = Button(root, text = "Export To Flash Drive", command = helloCallBack)
pauseButton = Button(root, text = "Play/Pause", command = playPauseCallBack)

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
def moveAndUpdate(row):
    # Collect Position Data
    try:
        x1 = row[0]
    except IndexError:
        x1 = -50
    try:
        y1 = row[1]
    except IndexError:
        y1 = -50
    try:
        x2 = row[2]
    except IndexError:
        x2 = -50
    try:
        y2 = row[3]
    except IndexError:
        y2 = -50
    try:
        x3 = row[4]
    except IndexError:
        x3 = -50
    try:
        y3 = row[5]
    except IndexError:
        y3 = -50
    try:
        x4 = row[6]
    except IndexError:
        x4 = -50
    try:
        y4 = row[7]
    except IndexError:
        y4 = -50
    try:
        x5 = row[8]
    except IndexError:
        x5 = -50
    try:
        y5 = row[9]
    except IndexError:
        y5 = -50
    try:
        x6 = row[10]
    except IndexError:
        x6 = -50
    try:
        y6 = row[11]
    except IndexError:
        y6 = -50

    #Update tag 1
    if (x1 == "NaN" or y1 == "NaN") and nanCounts[0] < 50:
        nanCounts[0] = nanCounts[0] + 1
    elif (x1 == "NaN" or y1 == "NaN") and nanCounts[0] >= 50:
        #Tag is missing
        t1Label["text"] = t1name + " (Missing)"
    else:
        nanCounts[0] = 0
        tag1.setCoords(int(x1), int(y1))
        tag1.updatePosition(c)
        t1Label["text"] = t1name

    #Update tag 2
    if (x2 == "NaN" or y2 == "NaN") and nanCounts[1] < 50:
        nanCounts[1] = nanCounts[1] + 1
    elif (x2 == "NaN" or y2 == "NaN") and nanCounts[1] >= 50:
        #Tag is missing
        t2Label["text"] = t2name + " (Missing)"
    else:
        nanCounts[1] = 0
        tag2.setCoords(int(x2), int(y2))
        tag2.updatePosition(c)
        t2Label["text"] = t2name

    #Update tag 3
    if (x3 == "NaN" or y3 == "NaN") and nanCounts[2] < 50:
        nanCounts[2] = nanCounts[2] + 1
    elif (x3 == "NaN" or y3 == "NaN") and nanCounts[2] >= 50:
        #Tag is missing
        t3Label["text"] = t3name + " (Missing)"
    else:
        nanCounts[2] = 0
        tag3.setCoords(int(x3), int(y3))
        tag3.updatePosition(c)
        t3Label["text"] = t3name

    #Update tag 4
    if (x4 == "NaN" or y4 == "NaN") and nanCounts[3] < 50:
        nanCounts[3] = nanCounts[3] + 1
    elif (x4 == "NaN" or y4 == "NaN") and nanCounts[3] >= 50:
        #Tag is missing
        t4Label["text"] = t4name + " (Missing)"
    else:
        nanCounts[3] = 0
        tag4.setCoords(int(x4), int(y4))
        tag4.updatePosition(c)
        t4Label["text"] = t4name

    #Update tag 5
    if (x5 == "NaN" or y5 == "NaN") and nanCounts[4] < 50:
        nanCounts[4] = nanCounts[4] + 1
    elif (x5 == "NaN" or y5 == "NaN") and nanCounts[4] >= 50:
        #Tag is missing
        t5Label["text"] = t5name + " (Missing)"
    else:
        nanCounts[4] = 0
        tag5.setCoords(int(x5), int(y5))
        tag5.updatePosition(c)
        t5Label["text"] = t5name

    #Update tag 5
    if (x6 == "NaN" or y6 == "NaN") and nanCounts[5] < 50:
        nanCounts[5] = nanCounts[5] + 1
    elif (x6 == "NaN" or y6 == "NaN") and nanCounts[5] >= 50:
        #Tag is missing
        t6Label["text"] = t6name + " (Missing)"
    else:
        nanCounts[5] = 0
        tag6.setCoords(int(x6), int(y6))
        tag6.updatePosition(c)
        t6Label["text"] = t6name

    root.update()

def runtimeLoop():
    if state == "live": #Live mode
        print("yay")
    else: #Replay mode
        currentRow = 0
        with open("data.csv", 'r', encoding='utf-8-sig') as csvFile:
            csvReader = csv.reader(csvFile, delimiter=',')
            data = list(csvReader)
            progress["to"] = numlines
            while True:
                d = datetime.timedelta(milliseconds=currentRow*100)
                timeLabel["text"] = d
                if currentRow < numlines and not paused:
                    currentRow = currentRow + 1
                    progress.set(currentRow)
                    moveAndUpdate(data[currentRow])
                    sleep(0.1) #100ms update time
                elif currentRow < numlines and paused:
                    currentRow = progress.get()
                    moveAndUpdate(data[currentRow])

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
cLegend.place(x=0, y=400, anchor=NW)

t1 = threading.Thread(target=runtimeLoop, args=())

t1.start()
#c.pack()
progress.pack(pady = 5)
crewNameButton.pack()
exportButton.pack()
pauseButton.pack()
root.mainloop()
