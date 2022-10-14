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

# Suit based hands:
# 1. Flush

# Rank value hands:
# 1. Straight

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

def determine_flush(suit_count):
    if suit_count[1] >= 5:
        return suit_count
    else:
        return False

def determine_straight(cards):
    # Put card ranks in ascending order
    ordered = sorted(cards)

    straight = []  # Initialize straight

    # Straight requires at least five different ranks
    if len(ordered) >= 5:
        straight = [ordered[0]]  # Initial value for straight

        for i in range(1, len(ordered)):
            current_number = ordered[i]
            previous_number = ordered[i-1]

            # Add next number in straight to list
            if current_number-previous_number==1:
                straight.append(current_number)
            else:
                # Straight already detected, break from for loop
                if len(straight) >= 5:
                    print(straight)
                    break
                # Reset straight
                else:
                    straight = [current_number]

    if len(straight)<5:
        return False
    else:
        return straight

# Determine the highest hand someone has
def determine_hands(player_cards, common_cards):
    # Combine player cards and common cards into single list
    pool = player_cards+common_cards

    # Determine rank frequency hand

    # Find multiples of a rank
    print([card.rank for card in pool])
    counts = collections.Counter([card.rank for card in pool])

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
    print([card.suit for card in pool])
    suits = collections.Counter([card.suit for card in pool])

    suits_frequency = suits.most_common()

    most_common_suit = suits_frequency[0]

    # Flush
    is_flush = determine_flush(most_common_suit)

    # Determine rank value hands
    is_straight = determine_straight(counts)

    # Determine combo hands

    # Flush present
    if is_flush:
        # Search cards of flush suit for straight
        cards_in_suit = sorted([card.rank for card in pool if card.suit==is_flush[0]])
        straight_flush = determine_straight(cards_in_suit)
    # TODO: Compare flushes/straights to each other

class Card():
    def __init__(self) -> None:
        self.suit = None
        self.rank = None

class Player():
    def __init__(self) -> None:
        self.cards = []
        self.hand = []
        self.money = 100


class Table():
    def __init__(self) -> None:
        self.players = []
        self.cards = []
        self.pot = 0
        self.dealer = None
        self.big_blind = None
        self.small_blind = None


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
        table.players.append(newP)

    table.cards = pulls[-5:]


# Blinds pay into pot
def pay_blinds(small_blind, big_blind, pot):
    small = 2.5
    big = 5

    # Check to make sure blinds have enough money
    if small_blind.money < small:
        pot = pot + small_blind.money  # Add whatever money small blind does have
        small_blind.money = 0
    else:
        pot = pot + small
        small_blind.money = small_blind.money - small

    if big_blind.money < big:
        pot = pot + big_blind.money  # Add whatever money big blind does have
        big_blind.money = 0
    else:
        pot = pot + big
        big_blind.money = big_blind.money - big

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

    table = Table()

    # Initialize players
    players = 3
    for i in range(0, players):
        newP = Player()
        table.players.append(newP)

    # Set initial dealer and blinds
    table.dealer = table.players[0]
    table.small_blind = table.players[1]
    table.big_blind = table.players[2]

    # Small blind and big blind pay into pot
    pay_blinds(table.small_blind, table.big_blind, table.pot)
    deal(cards, table)

    for player in table.players:
        determine_hands(player.cards, table.cards)

    print(table)