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

    def sort_hand(self):
        self.hand = sorted(self.hand, key=lambda card: (card.suit, card.value))

    def print_hand(self):
        print(self.name + " has cards --> ")
        for card in self.hand:
            print(card)

# if __name__ == '__main__':
#     testPerson = Player("Sam")
#     card1 = Card("Spade", 2)
#     card2 = Card("Heart", 2)
#     card3 = Card("Spade", 2)
#     card4 = Card("Club", 4)
#     testPerson.add_card(card1)
#     testPerson.add_card(card2)
#     testPerson.add_card(card3)
#     testPerson.add_card(card4)
#     testPerson.sort_hand()
