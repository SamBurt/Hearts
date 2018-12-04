class Card:

    # Card values are associated with cards in the deck, 2-10 represent
    # the same card value while 11-14 represent Jack - Ace with Ace being
    # the high card(14)

    values={
        2:"Two",
        3:"Three",
        4:"Four",
        5:"Five",
        6:"Six",
        7:"Seven",
        8:"Eight",
        9:"Nine",
        10:"Ten",
        11:"Jack",
        12:"Queen",
        13:"King",
        14:"Ace"
    }

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return self.values[self.value] + " of " + self.suit + "s"

    def __getitem__(self, key):
        if key == 0:
            return self.suit
        elif key == 1:
            return self.value
