import cardinfo


class Card:
    def __init__(self, card_number):
        self.card_number = card_number

    def get_face(self):
        return cardinfo.get_face(self.card_number)

    def get_suit(self):
        return cardinfo.get_suit(self.card_number)

    def get_color(self):
        return cardinfo.get_color(self.card_number)

    def __str__(self):
        return self.get_face() + " of " + self.get_suit()

    def get_value(self):
        return self.card_number % 13

    def get_val(self):
        if self.card_number == 0 or self.card_number == 13 or self.card_number == 26 or self.card_number == 39:
            return 11
        if self.card_number == 1 or self.card_number == 14 or self.card_number == 27 or self.card_number == 40:
            return 2
        if self.card_number == 2 or self.card_number == 15 or self.card_number == 28 or self.card_number == 41:
            return 3
        if self.card_number == 3 or self.card_number == 16 or self.card_number == 29 or self.card_number == 42:
            return 4
        if self.card_number == 4 or self.card_number == 17 or self.card_number == 30 or self.card_number == 43:
            return 5
        if self.card_number == 5 or self.card_number == 18 or self.card_number == 31 or self.card_number == 44:
            return 6
        if self.card_number == 6 or self.card_number == 19 or self.card_number == 32 or self.card_number == 45:
            return 7
        if self.card_number == 7 or self.card_number == 20 or self.card_number == 33 or self.card_number == 46:
            return 8
        if self.card_number == 8 or self.card_number == 21 or self.card_number == 34 or self.card_number == 47:
            return 9
        if self.card_number == 9 or self.card_number == 22 or self.card_number == 35 or self.card_number == 48:
            return 10
        if self.card_number == 10 or self.card_number == 23 or self.card_number == 36 or self.card_number == 49:
            return 10
        if self.card_number == 11 or self.card_number == 24 or self.card_number == 37 or self.card_number == 50:
            return 10
        if self.card_number == 12 or self.card_number == 25 or self.card_number == 38 or self.card_number == 51:
            return 10


'''card = Card(23)
print(card)
print(card.card_number)
print(card.get_color())
'''
