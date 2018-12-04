from Card import Card
import random

class Deck:

    suits = [
        "Heart",
        "Diamond",
        "Spade",
        "Club"
    ]

    values = list(range(2,15))

    def __init__(self):
        self.cards = self.generate_deck()

    def generate_deck(self):
        cards = []
        for suit in self.suits:
            for value in self.values:
                cards.append(Card(suit, value))
        random.shuffle(cards)
        return cards

    def print_deck(self):
        for card in self.cards:
            print(card)

    def deal_card(self):
        return self.cards.pop()
