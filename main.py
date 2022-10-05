import random
import collections

# Define hand types

# Rank frequency hands:
# 1. Five of a kind (N. B. Can only occur with wild cards)
# 2. Four of a kind
# 3. Three of a kind
# 4. Two pair
# 5. One pair
# 6. Full house
# 7. High card

# Rank value hands:
# 1. Straight

# Suit based hands:
# 1. Flush

# Combo hands:
# 1. Straight flush

# Hands, strongest to weakest:
# 1. Five of a kind: only possible with wild cards
# 2. Straight flush: five cards of the same suit in sequence
# 3. Four of a kind: four cards of the same rank
# 4. Full house: three of a kind and a pair. Builds on logic for one pair and three of a kind
# 5. Flush: five cards of the same suit
# 6. Straight: five cards in rank sequence
# 7. Three of a kind: three cards of the same rank. Builds on one pair
# 8. Two pairs: two cards of the same rank and two cards of the same different rank
# 9. One pair: two cards of the same rank
# 10. High card: card with the highest rank

# Determine the highest hand someone has
def determine_hands(cards): #player_cards, common_cards):
    # Determine rank frequency hand

    # Find multiples of a rank
    print([card.rank for card in cards])
    counts = collections.Counter([card.rank for card in cards])

    rank_frequency = counts.most_common()

    most_common_rank = rank_frequency[0]

    # 3/4/5 of a kind or full house
    if most_common_rank[1]>=3:
        # 5 of a kind
        # TODO: Implement wild card logic
        if most_common_rank[1] == 5:
            pass
        # 4 of a kind
        elif most_common_rank[1] == 4:
            pass
        # 3 of a kind
        else:
            # TODO: Which is the better 3 of a kind?
            if rank_frequency[1][1] == 3:
                pass
            # Full house
            elif rank_frequency[1][1] == 2:
                # TODO: Which pair is the better pair?
                if rank_frequency[2][1]== 2:
                    pass
    # One pair, two pair, or high card
    else:
        # One pair or two pair
        if most_common_rank[1]==2:
            # Two pair
            if rank_frequency[1][1] == 2:
                # TODO: Which two pair are the best two pair?
                if rank_frequency[2][1] == 2:
                    pass
            # One pair
            else:
                pass
        # High card
        else:
            pass

    # Determine suit based hands

    # Find multiples of a suit
    print([card.suit for card in cards])
    suits = collections.Counter([card.suit for card in cards])

    suits_frequency = suits.most_common()

    most_common_suit = suits_frequency[0]

    # Flush
    if most_common_suit[1] == 5:
        pass

class Card():
    def __init__(self) -> None:
        self.suit = None
        self.rank = None

class Player():
    def __init__(self) -> None:
        self.cards = []
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
        newP.cards.append(pulls[i*2])
        newP.cards.append(pulls[(i*2)+1])
        table.append(newP)

    determine_hands(pulls)

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