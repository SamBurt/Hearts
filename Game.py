from Card import Card
from Deck import Deck
from Player import Player

class Game:

    def __init__(self):
        self.players = self.create_players()
        self.deck = Deck()
        self.heartBroken = False

    def create_players(self):
        players = []
        valid = False
        num_players = 0;
        while not valid:
            num_players = int(raw_input("How many people are playing? (2-6) --> "))
            if ((num_players >= 2) and (num_players <= 6)):
                valid = True
            else:
                print("Number not valid")
        for i in range(num_players):
            name = raw_input("What is the name of player " + str(i+1) + "? --> ")
            players.append(Player(name))
        return players

    def print_players(self):
        for player in self.players:
            print(player)

    def deal_cards(self):
        self.deck = Deck()
        num_players = len(self.players)
        rounds = 52/num_players
        for i in range(rounds):
            for player in self.players:
                card = self.deck.deal_card()
                player.add_card(card)
        for player in self.players:
            player.sort_hand()

    def play_game(self):
        gameOver = False
        while not gameOver:
            print("Dealing Cards")
            self.deal_cards()
            # for person in self.players:
            #     person.print_hand()
            

            gameOver = True


if __name__ == '__main__':
    print("Starting")
    game = Game()
    game.print_players()
    game.play_game()
