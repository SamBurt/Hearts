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
        self.first_to_go = 0

    def create_players(self):
        players = []
        valid = False
        while not valid:
            try:
                self.num_players = int(raw_input("How many people are playing? (2-6) --> "))
            except:
                 print("Not a valid number")
                 continue
            if ((self.num_players >= 2) and (self.num_players <= 6)):
                valid = True
            else:
                print("Not a valid number")
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
            i = 0
            for player in self.players:
                card = self.deck.deal_card()
                player.add_card(card)
                if card.value == 2 and card.suit == "Club":
                    self.first_to_go = i
                i += 1
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
            card1_temp = list(raw_input("What is the first card you would like to trade? "))
            while True:
                if not player.card_in_hand(card1_temp):
                    card1_temp = list(raw_input
                    ("Card not in hand (must be in form \"8D\")"))
                else:
                    break
            card2_temp = list(raw_input("What is the second card you would like to trade? "))
            while True:
                if not player.card_in_hand(card2_temp):
                    card2_temp = list(raw_input
                    ("Card not in hand (must be in form \"8D\")"))
                else:
                    break
            card1_temp = map(lambda x: x.upper(), card1_temp)
            card2_temp = map(lambda x: x.upper(), card2_temp)
            if len(card1_temp) == 3:
                card1_temp[0] = card1_temp[0] + card1_temp[1]
                card1_temp[1] = card1_temp[2]
            if len(card2_temp) == 3:
                card2_temp[0] = card2_temp[0] + card2_temp[1]
                card2_temp[1] = card2_temp[2]
            card1 = Card(self.short_suit[card1_temp[1]], self.short_val[card1_temp[0]])
            card2 = Card(self.short_suit[card2_temp[1]], self.short_val[card2_temp[0]])
            to_trade = [card1, card2]
            sets_of_cards.append(to_trade)
            player.remove_card(card1)
            player.remove_card(card2)
        # Trade cards (as of now, always trades left)
        for player in self.players:
            incoming_cards = sets_of_cards.pop(-1)
            for i_card in incoming_cards:
                player.hand.append(i_card)
            player.sort_hand()
        self.cardSwapNumber += 1

    def losing_player(self, cards_played, first_suit):
        highest = 1
        player_num = 0
        i = 0
        for card in cards_played:
            if card.suit == first_suit and card.value > highest:
                player_num = i
                highest = card.value
            i += 1
        self.first_to_go = (self.first_to_go + player_num) % len(self.players)
        return self.players[self.first_to_go]

    def points_gained(self, cards_played):
        points = 0
        for card in cards_played:
            if card.suit == "Heart":
                points += 1
            elif card.suit == "Club" and card.value == 12:
                points += 13
        return points

    def play_hand(self):
        self.heartBroken = False
        for player in self.players:
            player.point_in_round = 0
        for i in range(52/len(self.players)):
            cards_played = []
            first_suit = None
            for i in range(self.first_to_go, len(self.players) + self.first_to_go):
                player = self.players[i%len(self.players)]
                print(player.name + "'s hand -> '", end="")
                print(player.hand)
                print("Cards played -> ", end="")
                print(cards_played)
                card_input = list(raw_input(player.name + "'s turn -> "))
                card_input = map(lambda x: x.upper(), card_input)
                while True:
                    if not player.card_in_hand(card_input):
                        card_input = list(raw_input
                        ("Card not in hand, try again (must be in form \"8D\"): "))
                        card_input = map(lambda x: x.upper(), card_input)
                    else:
                        break
                if len(card_input) == 3:
                    card_input[0] = card_input[0] + card_input[1]
                    card_input[1] = card_input[2]
                while True:
                    if first_suit == None:
                        if self.short_suit[card_input[1]] == "Heart" and self.heartBroken == False:
                            card_input = list(raw_input("Try again, Hearts have not been broken -> "))
                            card_input = map(lambda x: x.upper(), card_input)
                            #Checks if new card selection is in the players hand before checking if it's valid
                            while True:
                                if not player.card_in_hand(card_input):
                                    card_input = list(raw_input
                                    ("Card not in hand, try again (must be in form \"8D\"): "))
                                    card_input = map(lambda x: x.upper(), card_input)
                                    if len(card_input) == 3:
                                        card_input[0] = card_input[0] + card_input[1]
                                        card_input[1] = card_input[2]
                                else:
                                    break
                            continue
                        first_suit = self.short_suit[card_input[1]]
                        break
                    elif self.short_suit[card_input[1]] == first_suit:
                        break
                    elif first_suit == "Heart" and player.num_hearts == 0:
                        break
                    elif first_suit == "Spade" and player.num_spades == 0:
                        break
                    elif first_suit == "Club" and player.num_clubs == 0:
                        break
                    elif first_suit == "Diamond" and player.num_diamonds == 0:
                        break
                    card_input = list(raw_input("Try again, must play same suit -> "))
                    card_input = map(lambda x: x.upper(), card_input)
                    while True:
                        if not player.card_in_hand(card_input):
                            card_input = list(raw_input
                            ("Card not in hand, try again (must be in form \"8D\"): "))
                            card_input = map(lambda x: x.upper(), card_input)
                            if len(card_input) == 3:
                                card_input[0] = card_input[0] + card_input[1]
                                card_input[1] = card_input[2]
                        else:
                            break
                if self.short_suit[card_input[1]] == "Heart":
                    self.heartBroken = True
                card = Card(self.short_suit[card_input[1]], self.short_val[card_input[0]])
                cards_played.append(card)
                player.remove_card(card)
            l_player = self.losing_player(cards_played, first_suit)
            p_gained = self.points_gained(cards_played)
            l_player.point_in_round += p_gained
            #print(l_player.name + " got the trick and gained " + str(p_gained) + " points")
            print(l_player.name + " got the trick")
            print("---- Next Trick ----")

    def calculate_scores(self):
        shoot_the_moon = False
        for player in self.players:
            if player.point_in_round == 26:
                shoot_the_moon = True
                break
        for player in players:
            if shoot_the_moon:
                if player.point_in_round != 26:
                    player.score += 26
            else:
                player.score += player.point_in_round

    def play_game(self):
        gameOver = False
        while not gameOver:
            #print("Dealing Cards")
            self.deal_cards()
            #print("Trade Cards")
            self.trade_cards()
            self.play_hand()
            self.calulate_scores()
            print("End of hand, scores --> ")
            for player in self.players:
                if player.score >= 100:
                    gameOver = True
                print(player)


if __name__ == '__main__':
    print("Starting")
    game = Game()
    game.print_players()
    game.play_game()
