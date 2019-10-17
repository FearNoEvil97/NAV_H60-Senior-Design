import csv
import tkinter as tk
root = tk.Tk()

canvas = tk.Canvas(root, width = 500, height = 500)
canvas.pack()
radius = 10
bbox = (-radius, -radius, radius, radius)
oval = canvas.create_oval(*bbox)

def move_oval():
    canvas.move(oval, 10, 10)
    canvas.after(5000, move_oval)

# Start moving!
move_oval()

root.mainloop()