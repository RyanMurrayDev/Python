from tkinter import *
from shapes import *
from sprite import *

def drag(evt):
    r = Rectangle(evt.x, evt.y, 2, 2)
    r.draw(canvas)
    canvas.update()

root = Tk()
root.title("Drawing")
canvas = Canvas(root,width=800,height=600,
                background="white")
canvas.grid(row=0,column=0)
canvas.focus_set()
canvas.bind("<B1-Motion>",drag)

root.mainloop()
