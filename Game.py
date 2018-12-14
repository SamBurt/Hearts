from __future__ import print_function
from Card import Card
from Deck import Deck
from Player import Player


class Game:

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

    def __init__(self):
        self.players = self.create_players()
        self.deck = Deck()
        self.heartBroken = False
        self.cardSwapNumber = 1
        self.num_players = 0

    def create_players(self):
        players = []
        valid = False
        while not valid:
            self.num_players = int(raw_input("How many people are playing? (2-6) --> "))
            if ((self.num_players >= 2) and (self.num_players <= 6)):
                valid = True
            else:
                print("Number not valid")
        for i in range(self.num_players):
            name = raw_input("What is the name of player " + str(i+1) + "? --> ")
            players.append(Player(name))
        return players

    def print_players(self):
        for player in self.players:
            print(player)

    def deal_cards(self):
        self.deck = Deck()
        rounds = 52/len(self.players)
        for i in range(rounds):
            for player in self.players:
                card = self.deck.deal_card()
                player.add_card(card)
        for player in self.players:
            player.sort_hand()

    def trade_cards(self):
        # if self.cardSwapNumber % 3 == 0:
        #     return
        sets_of_cards = []
        # Find out white cards every player could like to trade
        # and remove those cards from their hand
        for player in self.players:
            print(player.name + "'s cards are -> [", end="")
            for card in player.hand:
                print(card, end=" ")
            print("]")
            # Add function to check if card is valid
            card1_temp = list(raw_input("What is the first card you would like to trade? "))
            card2_temp = list(raw_input("What is the second card you would like to trade? "))
            card1 = Card(self.short_suit[card1_temp[1]], self.short_val[card1_temp[0]])
            card2 = Card(self.short_suit[card2_temp[1]], self.short_val[card2_temp[0]])
            to_trade = [card1, card2]
            sets_of_cards.append(to_trade)
            player.remove_card(card1)
            player.remove_card(card2)
        # Trade cards (as of now, always trades left)
        for player in self.players:
            incoming_cards = sets_of_cards.pop(-1)
            print(incoming_cards)
            for i_card in incoming_cards:
                player.hand.append(i_card)
            player.sort_hand()
            print(player.hand)




        self.cardSwapNumber += 1

    def play_game(self):
        gameOver = False
        while not gameOver:
            print("Dealing Cards")
            self.deal_cards()
            # for person in self.players:
            #     person.print_hand()
            print("Trade Cards")
            self.trade_cards()


            gameOver = True


if __name__ == '__main__':
    print("Starting")
    game = Game()
    game.print_players()
    game.play_game()
