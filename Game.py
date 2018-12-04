from Card import Card
from Deck import Deck
from Player import Player

class Game:

    def __init__(self):
        self.players = self.create_players()
        deck = Deck()

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

    def playGame(self):
        


if __name__ == '__main__':
    print("Starting")
    game = Game()
    game.print_players()
    # game.playGame()
