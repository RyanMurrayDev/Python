faces = ("Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King")
suits = ("Clubs", "Spades", "Diamonds", "Hearts")
colors = ("black", "red")


def get_face(card_number):
    n = card_number % 13
    return faces[n]


def get_suit(card_number):
    n = card_number//13
    return suits[n]


def get_color(card_number):
    n = card_number//26
    return colors[n]
