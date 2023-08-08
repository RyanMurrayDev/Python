import card


class BlackJackHand:
    def __init__(self):
        self.hand = []

    def __str__(self):
        s = ''
        for i in range(0, len(self.hand)):
            s += str(self.hand[i]) + ", "
        return s

    def __iter__(self):
        self.it_count = 0
        return self

    def last(self):
        xyz = len(self.hand)
        return self.hand[xyz-1]

    def size(self):
        x = len(self.hand)
        return x

    def number_of_aces(self):
        aces = 0
        size = len(self.hand)
        for i in range(0, size):
            val = self.hand[i]
            value = val.get_val()
            if value == 11:
                aces += 1
        return aces

    def evaluate_hand(self):
        total = 0
        xy = self.number_of_aces()
        size = len(self.hand)
        for i in range(0, size):
                val = self.hand[i]
                value = val.get_val()
                # print(value)
                total += value
                if total > 21 and xy > 0:
                    total = total - 10
                    xy = xy-1
        return total

    def hit(self, card):
        self.hand.append(card)


'''black = BlackJackHand()
black.hit(card.Card(0))
black.hit(card.Card(10))
black.hit(card.Card(11))
black.hit(card.Card(12))
black.hit(card.Card(2))
x = black.number_of_aces()
s = black.evaluate_hand()
print(black.__str__())
w = black.size()
print("Number of Aces: " + str(x) + " Sum: " + str(s))
print("Size of hand: " + str(w))'''
