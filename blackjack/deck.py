import card
import random


class Deck:
    def __init__(self):
        self.deck = []

        for i in range(0,52):
            c = card.Card(i)
            self.deck.append(c)

    def __iter__(self):
        self.it_count = 0
        return self

    def __next__(self):
        x = self.deck[self.it_count]
        self.it_count += 1
        return x

    def __str__(self):
        s = ''
        for i in range(0,len(self.deck)):
            s += str(self.deck[i]) + ", "
        return s

    def shuffle(self):
        random.shuffle(self.deck)

    def is_empty(self):
        return len(self.deck) == 0

    def deal(self):
        if self.is_empty():
            return False
        card = self.deck.pop(0)
        return card


'''deck = Deck()
print(deck)
deck.shuffle()
print(deck)
for i in range(0,5):
    print(deck.deal())
print(deck)
for card in deck:
    print("it: " + str(card))
'''
