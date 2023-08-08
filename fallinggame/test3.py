from tkinter import *
from shapes import *
from sprite import *

def key(evt):
    print(evt)
    print("state:",evt.state)
    print(evt.keysym)
    print("pressed:", evt.char)
    print("keycode:",str(evt.keycode))
    if evt.keycode == 37:
        image_sprite.increment_x(-5)
    elif evt.keycode == 38:
        image_sprite.increment_y(-5)
    elif evt.keycode == 39:
        image_sprite.increment_x(5)
    elif evt.keycode == 40:
        image_sprite.increment_y(5)
    image_sprite.draw(canvas)
    canvas.update()

root = Tk()
root.title("Drawing")
canvas = Canvas(root,width=800,height=600,
                background="white")
canvas.grid(row=0,column=0)
canvas.focus_set()
canvas.bind("<Key>",key)


img = PhotoImage(file="0.png")
image_sprite = ImageSprite(img, 200, 200)
image_sprite.draw(canvas)


root.mainloop()
