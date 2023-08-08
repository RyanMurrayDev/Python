from tkinter import *
import craps

root = Tk()

global game_state
game_state = "ongoing"
global rolls
rolls = 0
global wins
global losses
wins = 0
losses = 0
global craps_game
d1 = PhotoImage(file="dice/dice1.png")
d2 = PhotoImage(file="dice/dice1.png")
image1 = Label(root, image=d1)
#image1.pack(padx=100, side=LEFT)
image1.place(x=400, y=200)
image2 = Label(root, image=d2)
#image2.pack(padx=100, side=RIGHT)
image2.place(x=500, y=200)


def roll():
    btn.config(text="Roll")
    message2.configure(text="")
    global craps_game
    global rolls
    #print("clicked")
    global d1
    global d2
    global wins
    global losses
    if rolls == 0:
        global craps_game
        craps_game = craps.Craps()
        craps_game.first_roll_rules()
        die1 = craps_game.get_die1()
        die2 = craps_game.get_die2()
        die1 = str(die1)
        die2 = str(die2)
        d1 = PhotoImage(file="dice/dice" + die1 + ".png")
        d2 = PhotoImage(file="dice/dice" + die2 + ".png")
        image1.config(image=d1)
        image1.image = d1
        image2.config(image=d2)
        image2.image = d2
        point = craps_game.get_point()
        point = str(point)
        message.configure(text="Your point is " + point)
        gamestate = craps_game.get_game_state()
        gamestate = str(gamestate)
        print(gamestate)
        if gamestate == "win":
            wins += 1
            message2.configure(text="You win. You have " + str(wins) + " wins and " + str(losses) + " losses.")
            btn.config(text="Play again")
        elif gamestate == "lose":
            losses += 1
            message2.configure(text="You lose. You have " + str(wins) + " wins and " + str(losses) + " losses.")
            btn.config(text="Play again")
        else:
            rolls += 1
    elif rolls != 0:
        craps_game.future_roll_rules()
        die1 = craps_game.get_die1()
        die2 = craps_game.get_die2()
        die1 = str(die1)
        die2 = str(die2)
        d1 = PhotoImage(file="dice/dice" + die1 + ".png")
        d2 = PhotoImage(file="dice/dice" + die2 + ".png")
        image1.config(image=d1)
        image1.image = d1
        image2.config(image=d2)
        image2.image = d2
        root.update_idletasks()
        gamestate = craps_game.get_game_state()
        gamestate = str(gamestate)
        if gamestate == "win":
            wins += 1
            message2.configure(text="You win. You have " + str(wins) + " wins and " + str(losses) + " losses.")
            btn.config(text="Play again")
            rolls = 0
        if gamestate == "lose":
            losses += 1
            message2.configure(text="You lose. You have " + str(wins) + " wins and " + str(losses) + " losses.")
            btn.config(text="Play again")
            rolls = 0


root.title("Craps")
lbl = Label(root,
            text="Craps",
            font=("Chiller", 20),
            fg="black")
lbl.pack(pady=50, side=TOP)
message = Label(root,
            text="Roll to Play",
            font=("Times", 20),
            fg="black")
message2 = Label(root,
            text="",
            font=("Times", 20),
            fg="black")
message2.pack(side="bottom")
message.pack(side="bottom")
btn = Button(root, text="Roll", command=roll)
#btn.pack(side="bottom")
btn.place(x=450, y=300)
root.configure(background='blue')
root.geometry("950x500")
root.mainloop()
