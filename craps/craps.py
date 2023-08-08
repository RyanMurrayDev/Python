import die


class Craps:
    def __init__(self):
        print("Craps")
        global game_state
        game_state = "ongoing"
        global wins
        wins = 0
        global losses
        losses = 0
        global die1
        global die2
        die1 = die.Die()
        die2 = die.Die()
        die1.roll()
        die2.roll()
        die1 = die1.get_face()
        die2 = die2.get_face()
        global point
        point = int(die1) + int(die2)
        print("You rolled a " + str(point))

    def get_die1(self):
        global die1
        return die1

    def get_die2(self):
        global die2
        return die2

    def get_game_state(self):
        global game_state
        return game_state

    def get_point(self):
        global point
        return point

    def first_roll_rules(self):
        global point
        global game_state
        if point == 7 or point == 11:
            game_state = "win"
            global wins
            wins += 1
            print("You win!")
            return ()
        elif point == 2 or point == 3 or point == 12:
            game_state = "lose"
            global losses
            losses += 1
            print("You Lose!")
            return ()

    def future_roll_rules(self):
        global die1
        global die2
        die1 = die.Die()
        die2 = die.Die()
        die1.roll()
        die2.roll()
        die1 = die1.get_face()
        die2 = die2.get_face()
        global die_sum
        die_sum = int(die1) + int(die2)
        print("You rolled a " + str(die_sum))
        global game_state
        if die_sum == point:
            game_state = "win"
            global wins
            wins += 1
            print("You win!")
            return ()
        elif die_sum == 7:
            game_state = "lose"
            global losses
            losses += 1
            print("You Lose!")
            return ()


'''def play():
        global wins
        wins = 0
        global losses
        losses = 0
        global game_state
        response = "y"
        while response == "y":
            craps = Craps()
            craps.first_roll_rules()
            while game_state == "ongoing":
                if game_state != "win" or game_state != "lose":
                    craps.future_roll_rules()
            response = input("Play again? (y or n)")
        print("Thanks for playing! You had " + str(wins) + " wins and " + str(losses) + " losses.")


play()'''
