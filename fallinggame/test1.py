from tkinter import *
from shapes import *

root = Tk()
root.title("Drawing")
canvas = Canvas(root,width=800,height=600,
                background="white")
canvas.grid(row=0,column=0)
canvas.create_rectangle(50,50,100,100,fill="red",
                        outline="black",
                        width=2)
canvas.create_oval(100,100,150,200,fill="blue")
r1 = Rectangle(150,150,50,50)
star1 = Star(400,400,100,20)
p1 = Point(0,0)
p2 = Point(1,1)
print("Distance:", Point.distance(p1, p2))
while True:
    canvas.create_rectangle(0,0,800,600,fill='white')
    canvas.create_rectangle(50, 50, 100, 100, fill="red",
                            outline="black",
                            width=2)
    canvas.create_oval(100, 100, 150, 200, fill="blue")
    r1.x += 1
    r1.y += 1
    r1.draw(canvas)
    star1.draw(canvas)
    canvas.update()
    canvas.after(33)


root.mainloop()