from tkinter import *
from shapes import *
from sprite import *
from datetime import datetime
import random


def key_handler(evt):
    global quit_loop
    global paused
    if evt.char == 'q':
        quit_loop = True
    elif evt.char == 'p':
        paused = not paused
    global hr1
    if evt.keycode == 37:
        hr1.direction = "left"
    elif evt.keycode == 39:
        hr1.direction = "right"


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
img2 = PhotoImage(file="b.png")
score = 0
lives = 3


hr1 = HorizontalMover(img, 400, 550, 0, 800, 5, 10)
array = []
for x in range(10):
  r = random.randint(1, 800-img.width())
  m = random.randint(0, 200)
  s = random.randint(10,50 )
  vr1 = VerticalRepeater(img2, r, -m, 0, 680, 2, s)
  array.append(vr1)


while not quit_loop:
    now = now_in_milliseconds()
    if not paused:
        canvas.delete("all")

        delta_time = now - last_tick
        for x in range(array.__len__()):
            array[x].update(delta_time)
            array[x].draw(canvas)
        hr1.draw(canvas)
        hr1.update(delta_time)
        for x in array:
            if hr1.intersects(x):
                r = random.randint(1, 800 - img.width())
                m = random.randint(0, 200)
                print(x)
                x.x = r
                x.y = -m
                score += 1
                print(score)
            if x.bottom >= 590:
                r = random.randint(1, 800 - img.width())
                m = random.randint(0, 200)
                print(x)
                x.x = r
                x.y = -m
                lives -= 1
            if lives == 0:
                print("game over")
                quit_loop = True
            canvas.create_text(100, 10, fill="darkblue", font="Times 20 italic bold",
                               text="Score: " + str(score))
            canvas.create_text(100, 40, fill="darkblue", font="Times 20 italic bold",
                       text="Lives: " + str(lives))
            canvas.create_line(0,590,800,590, fill="red")
    canvas.update()
    last_tick = now
    canvas.after(5)

root.mainloop()
