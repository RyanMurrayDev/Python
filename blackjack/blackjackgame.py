import blackjackhand
import deck


class BlackJackGame:
    def __init__(self):
        print("Blackjack Game")
        global game_state
        game_state = "ongoing"
        global d
        d = deck.Deck()
        d.shuffle()
        global dealer_hand
        dealer_hand = blackjackhand.BlackJackHand()
        global player_hand
        player_hand = blackjackhand.BlackJackHand()
        a = d.deal()
        #print(a)
        dealer_hand.hit(a)
        b = d.deal()
        #print(b)
        dealer_hand.hit(b)
        c = d.deal()
        #print(c)
        player_hand.hit(c)
        e = d.deal()
        #print(e)
        player_hand.hit(e)
        last = dealer_hand.last()
        print("Dealer's last card: " + str(last))
        print("Users Hand: " + str(player_hand))

    def player_play(self):
        global s1
        s1 = player_hand.evaluate_hand()
        if s1 == 21:
            global game_state
            game_state = "over"
            global wins
            wins += 1
            print("You win!")
            return ()
        again = input("Hit? (y or n)")
        while again == "y":
            a = d.deal()
            print(a)
            player_hand.hit(a)
            s1 = player_hand.evaluate_hand()
            print("Current sum: " + str(s1))
            if s1 == 21:
                game_state = "over"
                wins += 1
                print("You win!")
                return()
            elif s1 > 21:
                game_state = "over"
                print("You busted! Game over")
                global losses
                losses += 1
                return()
            again = input("Hit? (y or n)")
        print("Dealers turn")

    def dealer_play(self):
        sd = dealer_hand.evaluate_hand()
        while sd < 16:
            a = d.deal()
            print("Dealer received the:")
            print(a)
            dealer_hand.hit(a)
            sd = dealer_hand.evaluate_hand()
        print("Dealer total: " + str(sd))
        if sd > 21:
            global wins
            wins += 1
            print("Dealer Busted. You win!")
            return()
        sp = player_hand.evaluate_hand()
        print("Your sum was " + str(sp))
        if sp > sd:
            wins += 1
            print("You win!")
        else:
            global losses
            losses += 1
            print("You lose")


def play():
    response = "y"
    global wins
    wins = 0
    global losses
    losses = 0
    while response == "y":
        g = BlackJackGame()
        g.player_play()
        if game_state != "over":
            g.dealer_play()
        response = input("Play again? (y or n)")
    print("Thanks for playing! You had " + str(wins) + " wins and " + str(losses) + " losses.")


play()
