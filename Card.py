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

    short_val={
        2:"2",
        3:"3",
        4:"4",
        5:"5",
        6:"6",
        7:"7",
        8:"8",
        9:"9",
        10:"10",
        11:"J",
        12:"Q",
        13:"K",
        14:"A"
    }

    short_suit={
        "Heart":"H",
        "Diamond":"D",
        "Spade":"S",
        "Club":"C"
    }

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    # def __repr__(self):
    #     return self.values[self.value] + " of " + self.suit + "s"

    def __repr__(self):
        return self.short_val[self.value] + self.short_suit[self.suit]

    def __getitem__(self, key):
        if key == 0:
            return self.suit
        elif key == 1:
            return self.value
