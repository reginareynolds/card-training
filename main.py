import random

# Define hand types



class Card():
    def __init__(self) -> None:
        self.suit = None
        self.rank = None

class Player():
    def __init__(self) -> None:
        self.hand = []

def deal(deck, table):
    players = 4
    decks = 1

    hole_pulls = players * 2

    board = 3

    fourth = 1

    fifth = 1

    total = hole_pulls + board + fourth + fifth

    pulls = random.sample(list(deck), total)
    print(pulls)

    for i in range(0, players):
        newP = Player()
        newP.hand.append(pulls[i*2])
        newP.hand.append(pulls[(i*2)+1])
        table.append(newP)

if __name__ == '__main__':
    deck = {
        "Spades":[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], 
        "Clubs":[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
        "Hearts":[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], 
        "Diamonds":[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    }

    cards = []
    for suit in deck:
        for val in deck[suit]:
            new = Card()
            new.suit=suit
            new.rank=val
            cards.append(new)

    table = []
    deal(cards, table)

    print(table)