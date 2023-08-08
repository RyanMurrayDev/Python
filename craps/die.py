import random


class Die:
    def __init__(self):
        self.face = 1

    def __str__(self):
        return str(self.face)

    def __iter__(self):
        self.it_count = 0
        return self

    def roll(self):
        self.face = random.randint(1, 6)
        return self.face

    def get_face(self):
        return self.face


'''die1 = Die()
die2 = Die()
print(die1)
print(die2)
die1.roll()
die2.roll()
print(die1)
print(die2)'''
