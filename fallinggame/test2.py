from tkinter import *
from shapes import *


def click_handler(evt):
    print("clicked at", evt.x, evt.y)
    p = Point(evt.x, evt.y)
    print("Is in r1: ", r1.contains(p))


root = Tk()
root.title("Drawing")
canvas = Canvas(root,width=800,height=600,
                background="white")
canvas.grid(row=0,column=0)
canvas.bind("<Button-1>", click_handler)

r1 = Rectangle(100, 100, 100, 100)
r2 = Rectangle(50, 49, 50, 50)
print("R1 contains R2? ", r1.contains_rect(r2))
print("R1 intersects R2?", r1.intersects(r2))
r1.draw(canvas)
r2.draw(canvas)

root.mainloop()

