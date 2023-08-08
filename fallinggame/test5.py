from tkinter import *
from shapes import *
from sprite import *
from datetime import datetime


def key_handler(evt):
    global quit_loop
    global paused
    print(evt.keycode)
    print(evt)
    if evt.char == 'q':
        quit_loop = True
    elif evt.char == 'p':
        paused = not paused


def now_in_milliseconds():
    ms = (datetime.utcnow() -
          datetime(1970, 1, 1)) \
             .total_seconds() * 1000
    return int(ms)


paused = False
quit_loop = False
last_tick = now_in_milliseconds()
print(last_tick)

root = Tk()
root.title("Drawing")
canvas = Canvas(root, width=800, height=600,
                background="white")
canvas.grid(row=0, column=0)
canvas.focus_set()
canvas.bind("<Key>", key_handler)
img = PhotoImage(file="0.png")

hr1 = HorizontalBouncer(img, 400, 50, 0, 800, 5, 10)
hr2 = HorizontalBouncer(img, 400, 150, 0, 800, 5, 30)
while not quit_loop:
    now = now_in_milliseconds()
    if not paused:
        canvas.create_rectangle(0, 0, 800, 600, fill='white')

        delta_time = now - last_tick
        hr1.update(delta_time)
        hr2.update(delta_time)
        hr1.draw(canvas)
        hr2.draw(canvas)

    canvas.update()
    last_tick = now
    canvas.after(5)

root.mainloop()
