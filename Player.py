from Card import Card
from Deck import Deck

class Player:

    def __init__(self, name):
        self.name = name
        self.score = 0
        self.hand = []

    def __repr__(self):
        return self.name + " has " + str(self.score) + " points"

    def computer_score(self, points):
        self.score = self.score + points

    def add_card(self, card):
        self.hand.append(card)

    def remove_card(self, card):
        if card in self.hand:
            self.hand.remove(card)
        else:
            EnvironmentError()
