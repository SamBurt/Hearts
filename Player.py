from Card import Card
from Deck import Deck

class Player:

    short_val={
        "2":2,
        "3":3,
        "4":4,
        "5":5,
        "6":6,
        "7":7,
        "8":8,
        "9":9,
        "10":10,
        "J":11,
        "Q":12,
        "K":13,
        "A":14
    }

    short_suit={
        "H":"Heart",
        "D":"Diamond",
        "S":"Spade",
        "C":"Club"
    }

    def __init__(self, name):
        self.name = name
        self.score = 0
        self.hand = []
        self.num_hearts = 0
        self.num_spades = 0
        self.num_diamonds = 0
        self.num_clubs = 0
        self.point_in_round = 0

    def __repr__(self):
        return self.name + " has " + str(self.score) + " points"

    def computer_score(self, points):
        self.score = self.score + points

    def add_card(self, card):
        self.hand.append(card)
        if card.suit == "Heart":
            self.num_hearts += 1
        elif card.suit == "Spade":
            self.num_spades += 1
        elif card.suit == "Diamond":
            self.num_diamonds += 1
        elif card.suit == "Club":
            self.num_clubs += 1

    def remove_card(self, card):
        suit = card.suit
        val = card.value
        for card in self.hand:
            if card.value == val and card.suit == suit:
                self.hand.remove(card)
                if card.suit == "Heart":
                    self.num_hearts -= 1
                elif card.suit == "Spade":
                    self.num_spades -= 1
                elif card.suit == "Diamond":
                    self.num_diamonds -= 1
                elif card.suit == "Club":
                    self.num_clubs -= 1
                return
        else:
            EnvironmentError()

    def card_in_hand(self, card_string):
        card = map(lambda x: x.upper(), list(card_string))
        if len(card) == 3:
            card[0] = card[0] + card[1]
            card[1] = card[2]
        if card[1] in self.short_suit:
            suit = self.short_suit[card[1]]
        else:
            return False
        if card[0] in self.short_val:
            value = self.short_val[card[0]]
        else:
            return False
        for card in self.hand:
            if card.value == value and card.suit == suit:
                return True
        return False


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
